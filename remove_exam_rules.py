import re
import json

app_path = 'app.js'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const sprintData = (".*?");', content, re.DOTALL)
if match:
    sprint_str = json.loads(match.group(1))
    
    # Remove lines using regex
    sprint_str = re.sub(r'3\.\s*\*\*線上測驗機制\*\*：.*?(?=\n)', '', sprint_str)
    sprint_str = re.sub(r'4\.\s*\*\*作答設備\*\*：.*?(?=\n)', '', sprint_str)

    # Remove the sentence if it was unnumbered
    sprint_str = re.sub(r'\*\*\s*線上測驗機制\s*\*\*：.*?(?=\n)', '', sprint_str)
    sprint_str = re.sub(r'\*\*\s*作答設備\s*\*\*：.*?(?=\n)', '', sprint_str)

    # Clean up empty lines
    sprint_str = re.sub(r'\n\n+', '\n\n', sprint_str)
    
    new_sprint_js = 'const sprintData = ' + json.dumps(sprint_str, ensure_ascii=False) + ';'
    
    content = content[:match.start()] + new_sprint_js + content[match.end():]
    
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Removals successful.')
else:
    print('sprintData not found!')
