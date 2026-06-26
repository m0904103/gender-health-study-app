import re
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()
questions = re.findall(r'question:\s*[\'\"`]+(.*?)[\'\"`]+,', app_js)
with open('app_qs.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(questions))
