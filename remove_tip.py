import re
import json

app_path = 'app.js'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace both in dictionaryData and sprintData if it exists
match1 = re.search(r'const dictionaryData = (".*?");', content, re.DOTALL)
if match1:
    dict_str = json.loads(match1.group(1))
    dict_str = dict_str.replace('> [!TIP]\n', '')
    dict_str = dict_str.replace('[!TIP]', '')
    new_dict_js = 'const dictionaryData = ' + json.dumps(dict_str, ensure_ascii=False) + ';'
    content = content[:match1.start()] + new_dict_js + content[match1.end():]

match2 = re.search(r'const sprintData = (".*?");', content, re.DOTALL)
if match2:
    sprint_str = json.loads(match2.group(1))
    sprint_str = sprint_str.replace('> [!TIP]\n', '')
    sprint_str = sprint_str.replace('[!TIP]', '')
    new_sprint_js = 'const sprintData = ' + json.dumps(sprint_str, ensure_ascii=False) + ';'
    content = content[:match2.start()] + new_sprint_js + content[match2.end():]

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Removed [!TIP] successfully.')
