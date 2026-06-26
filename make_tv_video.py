"""
這個腳本負責生成期末考衝刺影片。
改進版：使用 FFmpeg 的 concat demuxer 分離音訊和視訊軌道，
確保音訊 100% 無縫連接，徹底消除段落間的微小停頓！
"""
import json
import os
import re
import sys
import time
import subprocess
import logging
from PIL import Image, ImageDraw, ImageFont

# 建立獨立的 Logger，解決 Windows 中文編碼問題
log = logging.getLogger("VideoMaker")
log.setLevel(logging.INFO)
file_handler = logging.FileHandler("make_tv_video.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
console_handler = logging.StreamHandler(sys.stdout)
log.addHandler(file_handler)
log.addHandler(console_handler)

skip_log = open("tv_skipped_sentences.txt", "w", encoding="utf-8")
error_log = open("tv_error_log.txt", "w", encoding="utf-8")

try:
    from gtts import gTTS
except ImportError:
    log.error("請先安裝 gTTS：pip install gTTS")
    sys.exit(1)

def text_to_speech(text, filename):
    for attempt in range(3):
        try:
            tts = gTTS(text=text, lang='zh-tw')
            tts.save(filename)
            return True
        except Exception as e:
            log.warning("gTTS 失敗 (嘗試 %d/3): %s", attempt+1, str(e))
            time.sleep(2)
    
    # gTTS 完全失敗，改用 pyttsx3 (確保安裝 pip install pyttsx3)
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.save_to_file(text, filename)
        engine.runAndWait()
        return True
    except Exception as e:
        log.error("TTS 完全失敗 [%s]: %s", text[:20], str(e))
        error_log.write(f"TTS 失敗: {text}\n")
        return False

# ── 資料載入 ──────────────────────────────────────────────────────────────
with open('audio_data_natural.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

font_path = "C:\\Windows\\Fonts\\msjh.ttc"
if not os.path.exists(font_path):
    font_path = "C:\\Windows\\Fonts\\arial.ttf"

audio_list_file = "concat_audio.txt"
video_list_file = "concat_video.txt"

with open(audio_list_file, "w", encoding="utf-8") as fa:
    pass
with open(video_list_file, "w", encoding="utf-8") as fv:
    pass

def get_audio_duration(file_path):
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', 
           '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        return float(result.stdout.strip())
    except:
        return 0.0

audio_files = []
frame_files = []
durations = []

# ── 生成每段的音訊與畫面 ──────────────────────────────────────────────────
for idx, chapter in enumerate(data):
    title = chapter['title']
    content = chapter['content']
    log.info("處理章節: %s", title)

    # 清理並斷句
    content = content.replace("(", "（").replace(")", "）")
    sentences = re.split(r'([。！？])', content)
    sentences_paired = []
    group = ""
    for i in range(0, len(sentences) - 1, 2):
        s = sentences[i] + sentences[i + 1]
        group += s.strip() + " "
        if (i / 2 + 1) % 3 == 0:
            sentences_paired.append(group.strip())
            group = ""
    if group.strip():
        sentences_paired.append(group.strip())

    for s_idx, sentence in enumerate(sentences_paired):
        sentence = sentence.strip()
        if not sentence:
            continue

        audio_file = f"audio_tv_{idx}_{s_idx}.mp3"
        frame_path = f"frame_tv_{idx}_{s_idx}.png"

        # 1. 生成 TTS 語音
        if not os.path.exists(audio_file):
            success = text_to_speech(sentence, audio_file)
            if not success:
                continue

        # 2. 生成背景圖片
        import glob
        # 對應各章節專屬精美背景
        bg_keywords = [
            "bg_ch6_medicine", "bg_ch7_ethnicity", "bg_ch8_stigma", 
            "bg_ch9_education", "bg_ch10_marriage", "bg_ch11_civic", "bg_ch9_education"
        ]
        kw = bg_keywords[idx] if idx < len(bg_keywords) else "bg_ch6_medicine"
        bg_images = glob.glob(f"{kw}*.png") + glob.glob(f"{kw}*.jpg")
        bg_path = bg_images[0] if bg_images else None

        try:
            if bg_path:
                bg_img = Image.open(bg_path).convert('RGBA').resize((1920, 1080))
            else:
                bg_img = Image.new('RGBA', (1920, 1080), (20, 20, 30, 255))
        except Exception as e:
            log.warning("無法開啟背景圖片 %s: %s，改用純色背景", bg_path, e)
            bg_img = Image.new('RGBA', (1920, 1080), (20, 20, 30, 255))

        # 建立一個與背景等大的透明圖層，用來畫半透明圓角背板與文字
        overlay = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        try:
            font_title = ImageFont.truetype(font_path, 60)
            font_sub   = ImageFont.truetype(font_path, 65)
        except Exception:
            font_title = ImageFont.load_default()
            font_sub   = ImageFont.load_default()

        # 標題加陰影
        draw.text((104, 84), title, font=font_title, fill=(0, 0, 0, 200))
        draw.text((100, 80), title, font=font_title, fill=(255, 230, 100))

        def wrap_text(text, font, max_width):
            lines = []
            current_line = ""
            for char in text:
                test_line = current_line + char
                try:
                    w = draw.textbbox((0, 0), test_line, font=font)[2] - \
                        draw.textbbox((0, 0), test_line, font=font)[0]
                except Exception:
                    w = len(test_line) * 65
                if w > max_width:
                    lines.append(current_line)
                    current_line = char
                else:
                    current_line = test_line
            if current_line:
                lines.append(current_line)
            return lines

        wrapped = wrap_text(sentence, font_sub, 1600)
        total_text_height = len(wrapped) * 90
        
        # 畫半透明質感黑底背板，讓底圖可以透出來，但文字依舊清晰
        box_width = 1700
        box_height = total_text_height + 100
        box_x1 = (1920 - box_width) / 2
        box_y1 = (1080 - box_height) / 2
        box_x2 = box_x1 + box_width
        box_y2 = box_y1 + box_height
        
        draw.rounded_rectangle((box_x1, box_y1, box_x2, box_y2), radius=30, fill=(0, 0, 0, 170))
        
        y_offset = box_y1 + 50

        for line in wrapped:
            try:
                w = draw.textbbox((0, 0), line, font=font_sub)[2] - \
                    draw.textbbox((0, 0), line, font=font_sub)[0]
            except Exception:
                w = len(line) * 65
            x = (1920 - w) / 2
            # 陰影
            draw.text((x + 4, y_offset + 4), line, font=font_sub, fill=(0, 0, 0, 255))
            # 內文
            draw.text((x, y_offset), line, font=font_sub, fill=(255, 255, 255, 255))
            y_offset += 90

        # 合成背景與文字圖層
        final_frame = Image.alpha_composite(bg_img, overlay).convert('RGB')
        final_frame.save(frame_path)

        # 3. 音檔去空白並加快 1.3 倍，並轉成 WAV (保證無縫拼接不留白)
        fast_audio = f"audio_tv_{idx}_{s_idx}_fast.wav"
        
        # 移除頭尾及中間超過0.3秒的靜音
        audio_filter = "silenceremove=start_periods=1:start_duration=0:start_threshold=-50dB:stop_periods=-1:stop_duration=0.3:stop_threshold=-50dB,atempo=1.3"
        
        ret_speed = subprocess.run([
            'ffmpeg', '-y', '-i', audio_file,
            '-filter:a', audio_filter,
            fast_audio
        ], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        
        if ret_speed.returncode != 0 or not os.path.exists(fast_audio):
            log.warning("加速音頻失敗，使用原速")
            subprocess.run(['ffmpeg', '-y', '-i', audio_file, fast_audio], stdout=subprocess.DEVNULL)

        dur = get_audio_duration(fast_audio)
        if dur > 0:
            audio_files.append(fast_audio)
            frame_files.append(frame_path)
            durations.append(dur)
            log.info("生成片段 [%d_%d]: duration=%.2fs", idx, s_idx, dur)

# ── 無縫合併所有片段 ──────────────────────────────────────────────────────────
log.info("開始無縫合併音軌與視訊...")

# 產生 video concat 檔案
with open(video_list_file, "w", encoding="utf-8") as fv:
    for i in range(len(frame_files)):
        fv.write(f"file '{frame_files[i]}'\n")
        fv.write(f"duration {durations[i]}\n")
    # ffmpeg concat demuxer 規定最後一張圖片需要再出現一次 (無 duration)
    if frame_files:
        fv.write(f"file '{frame_files[-1]}'\n")

# 產生 audio concat 檔案
with open(audio_list_file, "w", encoding="utf-8") as fa:
    for af in audio_files:
        fa.write(f"file '{af}'\n")

# 1. 產生純音軌 (從 wav 合併，保證 100% 無空隙)
temp_audio = "temp_full_audio.aac"
subprocess.run([
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', audio_list_file,
    '-c:a', 'aac', '-b:a', '192k', temp_audio
])

# 2. 產生純視訊 (根據每段精確時間)
temp_video = "temp_full_video.mp4"
subprocess.run([
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', video_list_file,
    '-vsync', 'vfr', '-pix_fmt', 'yuv420p', temp_video
])

# 3. 完美合併音視訊
output_file = "C:\\Users\\manpo\\OneDrive\\桌面\\114下期末考衝刺_性別健康多元文化_全考點21分鐘.mp4"
subprocess.run([
    'ffmpeg', '-y', '-i', temp_video, '-i', temp_audio,
    '-c', 'copy', output_file
])

log.info("影片合併完成！清除暫存檔案...")

# ── 清除暫存 ─────────────────────────────────────────────────────────────
import glob
for f in glob.glob("audio_tv_*.mp3") + glob.glob("audio_tv_*.wav") + glob.glob("frame_tv_*.png"):
    try:
        os.remove(f)
    except:
        pass
for f in [audio_list_file, video_list_file, temp_audio, temp_video]:
    try:
        os.remove(f)
    except:
        pass

skip_log.close()
error_log.close()
log.info("Done! TV Full Video Generated completely gapless.")
