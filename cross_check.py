import json
import re

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Extract quizData JSON string
quiz_data_match = re.search(r'const quizData = (\[.*?\]);', app_js, re.DOTALL)
if not quiz_data_match:
    print("Could not find quizData")
    exit(1)

try:
    quiz_data = json.loads(quiz_data_match.group(1))
    existing_questions = [q['question'].replace(' ', '') for q in quiz_data]
except Exception as e:
    print(f"Error parsing JSON: {e}")
    exit(1)

with open('past_exams.txt', 'r', encoding='utf-8') as f:
    past_exams = f.read()

mcq_pattern = re.compile(r'\d+\.\s+(.*?)\s+A\s*(.*?)\s+B\s*(.*?)\s+C\s*(.*?)\s+D\s*(.*?)\((.*?)\)', re.DOTALL)
matches = mcq_pattern.findall(past_exams)

new_questions = []

for match in matches:
    q_text = match[0].replace('\n', '').strip()
    q_text_compact = q_text.replace(' ', '')
    
    # Check if already in existing
    is_new = True
    for eq in existing_questions:
        if q_text_compact[:10] in eq or eq[:10] in q_text_compact:
            # Check length of similarity
            common_len = len(set(q_text_compact).intersection(set(eq)))
            if len(q_text_compact) > 0 and common_len / len(q_text_compact) > 0.7:
                is_new = False
                break
                
    if is_new:
        new_questions.append({
            'question': q_text,
            'options': [match[1].replace('\n', '').strip(), match[2].replace('\n', '').strip(), match[3].replace('\n', '').strip(), match[4].replace('\n', '').strip()],
            'ans': match[5]
        })

print(f"Found {len(new_questions)} new questions.")
for nq in new_questions:
    print(f"Q: {nq['question']}")
    print(f"A: {nq['options'][0]} | B: {nq['options'][1]} | C: {nq['options'][2]} | D: {nq['options'][3]}")
    print(f"Ans: {nq['ans']}")
    print("-" * 40)
