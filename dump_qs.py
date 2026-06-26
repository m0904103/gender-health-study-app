import re, json

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const quizData = (\[[\s\S]*?\]);\s*const clozeData', content)
if m:
    data_str = m.group(1)
    json_str = re.sub(r'([{,]\s*)([a-zA-Z0-9_]+)\s*:', r'\1"\2":', data_str)
    json_str = re.sub(r',\s*([\]}])', r'\1', json_str)
    try:
        data = json.loads(json_str)
        with open('qs.txt', 'w', encoding='utf-8') as out:
            for i, q in enumerate(data):
                out.write(f"{i+1}. {q.get('q', q.get('question', 'UNKNOWN'))}\n")
    except Exception as e:
        with open('qs.txt', 'w', encoding='utf-8') as out:
            out.write(f"Error parsing: {e}\n")
            out.write(json_str[:500])
