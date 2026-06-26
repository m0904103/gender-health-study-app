import re
import json

app_path = 'app.js'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const sprintData = (".*?");', content, re.DOTALL)
if match:
    sprint_str = json.loads(match.group(1))
    
    # Text replacements
    sprint_str = sprint_str.replace('字體經過特別放大處理（內文14號字、標題18號字），並且大量補充了課本的完整前因後果與故事脈絡，絕對不偷工減料！', '為幫助理解，講義內容補充了課本的前因後果與脈絡。')
    sprint_str = sprint_str.replace('老師已直接附上【完美擬答】', '已附上【參考擬答】')
    sprint_str = sprint_str.replace('【完美擬答 (直接背誦用)】', '【參考擬答】')
    sprint_str = sprint_str.replace('【完美擬答】', '【參考擬答】')
    sprint_str = sprint_str.replace('，請直接背誦！', '。')
    sprint_str = sprint_str.replace('，請直接背誦', '。')
    sprint_str = sprint_str.replace('作答秘訣：當簡答題問到以下名詞時，請直接將這段標準定義寫上去，再配上一兩句您自己的舉例（如字數不足時），保證能拿到完整配分。', '作答秘訣：當簡答題問到以下名詞時，可以參考這段定義，並適度搭配自己的舉例來豐富內容。')
    
    new_sprint_js = 'const sprintData = ' + json.dumps(sprint_str, ensure_ascii=False) + ';'
    
    content = content[:match.start()] + new_sprint_js + content[match.end():]
    
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replacements successful.')
else:
    print('sprintData not found!')
