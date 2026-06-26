import json
import re
import difflib

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const quizData = (\[[\s\S]*?\]);\s*const flashcardData', content)
if not m: exit(1)

questions = json.loads(m.group(1))

def normalize_q(q_str):
    if not q_str: return ''
    q = re.sub(r'\(.*?[年年].*?考題\)', '', q_str)
    q = re.sub(r'【.*?】', '', q)
    q = re.sub(r'[^\w\u4e00-\u9fa5]', '', q)
    return q

normalized_qs = [normalize_q(q.get('q', '')) for q in questions]

for i in range(len(questions)):
    for j in range(i + 1, len(questions)):
        q1 = normalized_qs[i]
        q2 = normalized_qs[j]
        if len(q1) > 5 and len(q2) > 5:
            ratio = difflib.SequenceMatcher(None, q1, q2).ratio()
            # Also check if one contains a large part of another
            # e.g., if longest common substring is > 10 chars
            s = difflib.SequenceMatcher(None, q1, q2)
            match = s.find_longest_match(0, len(q1), 0, len(q2))
            
            if ratio > 0.50 or match.size > 10:
                print(f"[{i+1}] {questions[i]['q']}\n[{j+1}] {questions[j]['q']}\nRatio: {ratio:.2f}, Common: {match.size}\n")
