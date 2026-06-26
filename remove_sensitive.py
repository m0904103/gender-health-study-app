import re
import json

app_path = r"C:\Users\manpo\.gemini\antigravity\scratch\gender-health-study-app\app.js"

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find sprintData string
match = re.search(r'const sprintData = (".*?");', content, re.DOTALL)
if match:
    # Deserialize
    sprint_str = json.loads(match.group(1))
    
    # Perform replacements on the actual python string
    sprint_str = sprint_str.replace('0609 面授課老師考前獨家洩題', '期末考核心重點總覽')
    sprint_str = sprint_str.replace('出題老師於 0609 最後一次面授課中，親自提點了以下必考方向與測驗說明', '以下為課程核心必考方向與測驗說明')
    
    # Reserialize
    new_sprint_js = 'const sprintData = ' + json.dumps(sprint_str, ensure_ascii=False) + ';'
    
    # Replace in file content
    content = content[:match.start()] + new_sprint_js + content[match.end():]
    
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replacements successful.")
else:
    print("sprintData not found!")
