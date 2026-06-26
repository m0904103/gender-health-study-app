import json
import os
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont

# Load JSON data
with open('audio_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Optional: try to find a nice font, or fallback to default
font_path = "C:\\Windows\\Fonts\\msjh.ttc"  # Microsoft JhengHei
try:
    font_title = ImageFont.truetype(font_path, 80)
    font_subtitle = ImageFont.truetype(font_path, 40)
except Exception:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()

clips = []

print("Generating video clips...")
for idx, chapter in enumerate(data):
    title = chapter['title']
    content = chapter['content']
    
    print(f"Processing {title}...")
    
    # Generate TTS Audio
    audio_file = f"audio_{idx}.mp3"
    tts = gTTS(text=content, lang='zh-tw', slow=False)
    tts.save(audio_file)
    
    # Create Audio Clip to get duration
    audio_clip = AudioFileClip(audio_file)
    duration = audio_clip.duration
    
    # Create an image using PIL
    img = Image.new('RGB', (1920, 1080), color=(30, 30, 40))
    draw = ImageDraw.Draw(img)
    
    # Draw text (centered)
    # PIL draw.textbbox instead of textsize for newer PIL versions
    try:
        bbox = draw.textbbox((0, 0), title, font=font_title)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
    except AttributeError:
        text_w, text_h = draw.textsize(title, font=font_title)
        
    x = (1920 - text_w) / 2
    y = (1080 - text_h) / 2 - 100
    draw.text((x, y), title, font=font_title, fill=(255, 255, 255))
    
    subtitle = "114下學期 期末考終極衝刺"
    try:
        bbox2 = draw.textbbox((0, 0), subtitle, font=font_subtitle)
        sub_w = bbox2[2] - bbox2[0]
    except AttributeError:
        sub_w, _ = draw.textsize(subtitle, font=font_subtitle)
    
    draw.text(((1920 - sub_w)/2, y + 150), subtitle, font=font_subtitle, fill=(200, 200, 200))
    
    img_path = f"img_{idx}.png"
    img.save(img_path)
    
    # Create MoviePy ImageClip
    # set_duration makes it a static video clip of the same length as the audio
    video_clip = ImageClip(img_path).set_duration(duration)
    # attach the audio
    video_clip = video_clip.set_audio(audio_clip)
    
    clips.append(video_clip)

print("Concatenating clips...")
final_video = concatenate_videoclips(clips, method="compose")

output_file = "final_study_video.mp4"
print(f"Writing {output_file}...")
# fps=1 is fine since it's just static images with audio! Very fast to render.
final_video.write_videofile(output_file, fps=1, codec="libx264", audio_codec="aac")

# Cleanup
for idx in range(len(data)):
    try:
        os.remove(f"audio_{idx}.mp3")
        os.remove(f"img_{idx}.png")
    except:
        pass

print("Done!")
