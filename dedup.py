import re
import json
import difflib

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the quizData array
m = re.search(r'const quizData = (\[[\s\S]*?\]);\s*const flashcardData', content)
if not m:
    print("Could not find quizData")
    exit(1)

data_str = m.group(1)
json_str = re.sub(r'([{,]\s*)([a-zA-Z0-9_]+)\s*:', r'\1"\2":', data_str)
json_str = re.sub(r',\s*([\]}])', r'\1', json_str)

try:
    questions = json.loads(json_str)
except Exception as e:
    print("JSON parsing failed:", e)
    exit(1)

duplicates_to_remove = []

# Let's find duplicates based on the question text (ignoring whitespace and punctuation, and ignoring the "(104, 106, 113年考題)" parts)
def normalize_q(q_str):
    # remove the past exam tags
    q = re.sub(r'\(.*?[年年].*?考題\)', '', q_str)
    # remove everything that is not alphanumeric or chinese chars
    q = re.sub(r'[^\w\u4e00-\u9fa5]', '', q)
    return q

normalized_qs = [normalize_q(q.get('q', '')) for q in questions]

# We want to keep the one that has the richer text? Or just keep the earlier one.
# Wait, for the past exam questions (the 10 I just added at the end), they have the tags like "(104, 106, 113年考題)".
# If there is a duplicate between an earlier question and a later question with tags, maybe we want to keep the tags?
# Let's just find the duplicates first.
to_delete = []

for i in range(len(questions)):
    for j in range(i + 1, len(questions)):
        q1 = normalized_qs[i]
        q2 = normalized_qs[j]
        # if string similarity is high
        if len(q1) > 5 and len(q2) > 5:
            ratio = difflib.SequenceMatcher(None, q1, q2).ratio()
            if ratio > 0.8:
                print(f"Duplicate found:\n  [{i+1}] {questions[i]['q']}\n  [{j+1}] {questions[j]['q']}\n  Ratio: {ratio:.2f}\n")
                # Keep the one with the tags (which are the later ones, j). So we delete i.
                if i not in to_delete:
                    to_delete.append(i)

print("Indices to delete:", sorted(to_delete))

# Generate the new array keeping only non-deleted
new_questions = [q for idx, q in enumerate(questions) if idx not in to_delete]
print(f"Original length: {len(questions)}, New length: {len(new_questions)}")

# Convert the new array back to JS string
# The json.dumps will format it nicely, but we want to retain the 'answer' instead of 'ans', etc.
# Wait, I just want to replace the whole quizData block.
new_js_array = json.dumps(new_questions, ensure_ascii=False, indent=4)
# remove quotes around keys to match the style (optional, but good)
new_js_array = re.sub(r'"([a-zA-Z0-9_]+)":', r'\1:', new_js_array)

new_content = content.replace(data_str, new_js_array)
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Successfully deduplicated app.js")
