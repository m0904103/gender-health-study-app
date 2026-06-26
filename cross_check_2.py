import re

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Extract questions from app.js using regex
questions = re.findall(r'question:\s*[\'\"`]+(.*?)[\'\"`]+,', app_js)
existing_questions = [q.replace(' ', '') for q in questions]

with open(r'C:\Users\manpo\.gemini\antigravity\brain\0838ad42-99fb-48fc-a1b9-6bcec603ee2d\scratch\past_exams.txt', 'r', encoding='utf-8') as f:
    past_exams = f.read()

mcq_pattern = re.compile(r'\d+\.\s+(.*?)\s+A\s*(.*?)\s+B\s*(.*?)\s+C\s*(.*?)\s+D\s*(.*?)\((.*?)\)', re.DOTALL)
matches = mcq_pattern.findall(past_exams)

new_questions = []

for match in matches:
    q_text = match[0].replace('\n', '').strip()
    q_text_compact = q_text.replace(' ', '')
    
    is_new = True
    for eq in existing_questions:
        if q_text_compact[:10] in eq or eq[:10] in q_text_compact:
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

with open('new_questions.txt', 'w', encoding='utf-8') as f:
    f.write(f"Found {len(new_questions)} new questions.\n")
    for nq in new_questions:
        f.write(f"Q: {nq['question']}\n")
        f.write(f"A: {nq['options'][0]} | B: {nq['options'][1]} | C: {nq['options'][2]} | D: {nq['options'][3]}\n")
        f.write(f"Ans: {nq['ans']}\n")
        f.write("-" * 40 + "\n")
