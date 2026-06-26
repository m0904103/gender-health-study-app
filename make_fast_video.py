import json
import os
import glob
import re
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import shutil
import subprocess

# Load JSON data
with open('audio_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

font_path = "C:\\Windows\\Fonts\\msjh.ttc"
bg_patterns = [
    "bg_medical_*.png",
    "bg_culture_*.png",
    "bg_psychology_*.png",
    "bg_campus_*.png",
    "bg_family_*.png",
    "bg_global_*.png"
]
brain_dir = r"C:\Users\manpo\.gemini\antigravity\brain\0838ad42-99fb-48fc-a1b9-6bcec603ee2d"

clips = []
print("Generating 1.3x FAST dynamic video clips...")

for idx, chapter in enumerate(data):
    title = chapter['title']
    content = chapter['content']
    
    sentences = re.split(r'([。！？])', content)
    sentences_paired = []
    for i in range(0, len(sentences)-1, 2):
        s = sentences[i] + sentences[i+1]
        if s.strip():
            sentences_paired.append(s.strip())
    if len(sentences) % 2 == 1 and sentences[-1].strip():
        sentences_paired.append(sentences[-1].strip())
    
    pattern = os.path.join(brain_dir, bg_patterns[idx])
    bg_matches = glob.glob(pattern)
    if bg_matches:
        bg_path = bg_matches[0]
    else:
        img = Image.new('RGB', (1920, 1080), color=(40, 40, 50))
        img.save(f"fallback_bg_{idx}.png")
        bg_path = f"fallback_bg_{idx}.png"
        
    chapter_clips = []
    
    for s_idx, sentence in enumerate(sentences_paired):
        audio_file = f"audio_{idx}_{s_idx}.mp3"
        fast_audio_file = f"audio_fast_{idx}_{s_idx}.mp3"
        
        # 1. Generate normal TTS
        tts = gTTS(text=sentence, lang='zh-tw', slow=False)
        tts.save(audio_file)
        
        # 2. Speed up audio using ffmpeg without changing pitch (atempo=1.35)
        # Using 1.35x for punchy, fast-paced Tiktok style
        subprocess.run(['ffmpeg', '-y', '-i', audio_file, '-filter:a', 'atempo=1.35', fast_audio_file], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        audio_clip = AudioFileClip(fast_audio_file)
        duration = audio_clip.duration
        
        # Background
        bg_img = Image.open(bg_path).resize((1920, 1080)).convert('RGBA')
        dark_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 150))
        bg_dark = Image.alpha_composite(bg_img, dark_layer).convert('RGB')
        
        draw = ImageDraw.Draw(bg_dark)
        try:
            font_title = ImageFont.truetype(font_path, 60)
            font_sub = ImageFont.truetype(font_path, 80)
        except:
            font_title = ImageFont.load_default()
            font_sub = ImageFont.load_default()
            
        draw.text((100, 100), title, font=font_title, fill=(255, 215, 0))
        
        def wrap_text(text, font, max_width):
            lines = []
            words = list(text)
            current_line = ""
            for char in words:
                test_line = current_line + char
                try:
                    w = draw.textbbox((0,0), test_line, font=font)[2] - draw.textbbox((0,0), test_line, font=font)[0]
                except:
                    w = draw.textsize(test_line, font=font)[0]
                if w > max_width:
                    lines.append(current_line)
                    current_line = char
                else:
                    current_line = test_line
            lines.append(current_line)
            return lines
            
        wrapped = wrap_text(sentence, font_sub, 1600)
        y_offset = 400
        for line in wrapped:
            try:
                w = draw.textbbox((0,0), line, font=font_sub)[2] - draw.textbbox((0,0), line, font=font_sub)[0]
            except:
                w = draw.textsize(line, font=font_sub)[0]
            x = (1920 - w) / 2
            draw.text((x, y_offset), line, font=font_sub, fill=(255, 255, 255))
            y_offset += 120
            
        frame_path = f"frame_{idx}_{s_idx}.png"
        bg_dark.save(frame_path)
        
        v_clip = ImageClip(frame_path).set_duration(duration).set_audio(audio_clip)
        chapter_clips.append(v_clip)
        
    clips.extend(chapter_clips)

final_video = concatenate_videoclips(clips, method="compose")
output_file = "C:\\Users\\manpo\\OneDrive\\桌面\\114下學期期末考_高倍速衝刺版影片.mp4"
final_video.write_videofile(output_file, fps=5, codec="libx264", audio_codec="aac")

for idx, chapter in enumerate(data):
    for s_idx in range(50):
        try:
            os.remove(f"audio_{idx}_{s_idx}.mp3")
            os.remove(f"audio_fast_{idx}_{s_idx}.mp3")
            os.remove(f"frame_{idx}_{s_idx}.png")
        except:
            pass
print("Done! Fast Video Generated.")
