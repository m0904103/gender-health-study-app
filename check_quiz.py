import sys, io
import json, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content = open('app.js', encoding='utf-8').read()
m = re.search(r'const quizData = (\[.*?\]);', content, re.DOTALL)
if m:
    data_str = m.group(1)
    # The array might not be valid JSON because it uses unquoted keys or single quotes
    # Let's just print the first 300 characters to inspect it
    print(data_str[:300])
else:
    print('Not found')
