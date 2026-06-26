import json
import re

def clean_for_speech(text):
    # Remove markdown symbols
    text = re.sub(r'[*#>`\-]', '', text)
    # Clean up multiple spaces or newlines
    text = re.sub(r'\n+', '。', text)
    text = re.sub(r'\s+', ' ', text)
    # Make multiple choice read better
    text = text.replace('(A)', '選項A：')
    text = text.replace('(B)', '選項B：')
    text = text.replace('(C)', '選項C：')
    text = text.replace('(D)', '選項D：')
    text = text.replace('解答：', '。正確答案是：')
    text = text.replace('解析：', '。解析說明：')
    text = text.replace('【🌟必考】', '這題必考！請特別注意：')
    return text.strip()

# Read app.js
with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract sprintData string
match = re.search(r'const sprintData = "(.*?)";\n\n// --- 資料區', content, re.DOTALL)
if not match:
    print("Could not find sprintData")
    exit(1)

sprint_text = match.group(1)
# Handle escaped newlines
sprint_text = sprint_text.replace('\\n', '\n')

chapters = [
    "第六章：性別醫學之議題初探",
    "第七章：臺灣多元族群處境",
    "第八章：社會污名與心理健康",
    "第九章：性別教育與弱勢族群處境",
    "第十章：新住民的婚姻輔導與諮商",
    "第十一章：多元文化公民社會參與",
    "考前 10 分鐘：必考名詞解釋"
]

split_text = re.split(r'##\s+第.*?章：.*?|##\s+🎯\s+考前 10 分鐘：必考名詞解釋', sprint_text)
# split_text[0] is the intro, split_text[1] is chap 6, etc.

audio_data = []

# Intro
intro = clean_for_speech(split_text[0])
if intro:
    audio_data.append({
        "title": "期末考終極衝刺導讀",
        "content": intro
    })

for i in range(1, len(split_text)):
    ch_text = split_text[i]
    if i-1 < len(chapters):
        ch_title = chapters[i-1]
    else:
        ch_title = f"章節 {i}"
        
    cleaned_ch = clean_for_speech(ch_text)
    
    # Let's break the cleaned_ch into slightly smaller chunks if it's too huge, 
    # but the moviepy script handles sentence breaking anyway.
    if cleaned_ch:
        audio_data.append({
            "title": ch_title,
            "content": cleaned_ch
        })

with open('audio_data_full.json', 'w', encoding='utf-8') as f:
    json.dump(audio_data, f, ensure_ascii=False, indent=2)

print("Created audio_data_full.json successfully.")
