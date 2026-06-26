import json
import re
import difflib

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const quizData = (\[[\s\S]*?\]);\s*const flashcardData', content)
if not m:
    print("Could not find quizData")
    exit(1)

data_str = m.group(1)
try:
    questions = json.loads(data_str)
except Exception as e:
    print("JSON parsing failed:", e)
    exit(1)

def normalize_q(q_str):
    if not q_str: return ''
    q = re.sub(r'\(.*?[年年].*?考題\)', '', q_str)
    q = re.sub(r'[^\w\u4e00-\u9fa5]', '', q)
    return q

normalized_qs = [normalize_q(q.get('q', '')) for q in questions]
to_delete = []

for i in range(len(questions)):
    for j in range(i + 1, len(questions)):
        q1 = normalized_qs[i]
        q2 = normalized_qs[j]
        if len(q1) > 5 and len(q2) > 5:
            ratio = difflib.SequenceMatcher(None, q1, q2).ratio()
            if ratio > 0.80:
                print(f"Fuzzy duplicate found:\n  [{i+1}] {questions[i]['q']}\n  [{j+1}] {questions[j]['q']}\n  Ratio: {ratio:.2f}\n")
                if i not in to_delete:
                    to_delete.append(i)

print("Indices to delete:", sorted(to_delete))

new_questions = [q for idx, q in enumerate(questions) if idx not in to_delete]
print(f"Original length: {len(questions)}, New length: {len(new_questions)}")

new_js_array = json.dumps(new_questions, ensure_ascii=False, indent=4)
# Optional: reformat slightly to match preference (unquoted keys)
new_js_array = re.sub(r'"([a-zA-Z0-9_]+)":', r'\1:', new_js_array)

new_content = content.replace(data_str, new_js_array)
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Successfully fuzzy deduplicated app.js")
