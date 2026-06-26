import re
import json

app_path = 'app.js'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const sprintData = (".*?");', content, re.DOTALL)
if match:
    sprint_str = json.loads(match.group(1))
    
    # Remove the sentence: 採用專業公職考試用書的編排邏輯
    sprint_str = sprint_str.replace('採用專業公職考試用書的編排邏輯。', '')
    sprint_str = sprint_str.replace('採用專業公職考試用書的編排邏輯，', '')
    sprint_str = sprint_str.replace('採用專業公職考試用書的編排邏輯', '')
    
    new_sprint_js = 'const sprintData = ' + json.dumps(sprint_str, ensure_ascii=False) + ';'
    
    content = content[:match.start()] + new_sprint_js + content[match.end():]
    
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replacements successful.')
else:
    print('sprintData not found!')
