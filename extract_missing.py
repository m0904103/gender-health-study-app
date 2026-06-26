import json
import re
import difflib
import collections

# Load current app.js questions
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

m = re.search(r'const quizData = (\[[\s\S]*?\]);\s*const flashcardData', app_js)
if not m: exit(1)
current_questions = json.loads(m.group(1))

def normalize_q(q_str):
    if not q_str: return ''
    q = re.sub(r'\(.*?[年年].*?考題\)', '', q_str)
    q = re.sub(r'【.*?】', '', q)
    q = re.sub(r'[^\w\u4e00-\u9fa5]', '', q)
    return q

current_normalized = [normalize_q(q['q']) for q in current_questions]

# Load past exams
past_exams_file = r'C:\Users\manpo\.gemini\antigravity\brain\0838ad42-99fb-48fc-a1b9-6bcec603ee2d\scratch\past_exams.txt'
try:
    with open(past_exams_file, 'r', encoding='big5') as f:
        past_exams_text = f.read()
except UnicodeDecodeError:
    with open(past_exams_file, 'r', encoding='cp950', errors='ignore') as f:
        past_exams_text = f.read()

raw_qs = re.split(r'\n\s*\d+\.\s+', '\n' + past_exams_text)[1:]
print(f"Total raw questions parsed from past exams: {len(raw_qs)}")

missing_qs = []
for q_text in raw_qs:
    # First line is usually the question
    lines = q_text.strip().split('\n')
    question_part = lines[0].split('(A)')[0].strip()
    question_part = re.split(r'\([A-D1-4]\)|①|甲', question_part)[0].strip()
    
    q_norm = normalize_q(question_part)
    if len(q_norm) < 5: continue
    
    # Check if this question is in current_normalized
    is_in_app = False
    for curr_q in current_normalized:
        ratio = difflib.SequenceMatcher(None, q_norm, curr_q).ratio()
        if ratio > 0.65 or q_norm in curr_q or curr_q in q_norm:
            is_in_app = True
            break
    
    if not is_in_app:
        missing_qs.append(question_part)

counter = collections.Counter()
for mq in missing_qs:
    mq_norm = normalize_q(mq)
    found = False
    for key in counter.keys():
        if difflib.SequenceMatcher(None, mq_norm, normalize_q(key)).ratio() > 0.65:
            counter[key] += 1
            found = True
            break
    if not found:
        counter[mq] = 1

print("\nMost common MISSING questions from past exams:")
for q, count in counter.most_common(20):
    if count >= 2:
        print(f"[{count} times] {q}")
