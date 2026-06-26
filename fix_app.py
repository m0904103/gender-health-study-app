import os
import json

app_old_path = r"C:\Users\manpo\.gemini\antigravity\scratch\gender-health-study-app\app_old.js"
app_path = r"C:\Users\manpo\.gemini\antigravity\scratch\gender-health-study-app\app.js"
summary_path = r"C:\Users\manpo\.gemini\antigravity\brain\0838ad42-99fb-48fc-a1b9-6bcec603ee2d\artifacts\textbook_summary.md"

# 1. Load the markdown summary and serialize it properly for Javascript
with open(summary_path, 'r', encoding='utf-8') as f:
    summary_data = f.read()

# Encode dictionaryData as a JSON string so it safely handles backticks, quotes, newlines, etc.
dictionaryData_js = "const dictionaryData = " + json.dumps(summary_data, ensure_ascii=False) + ";\n\n"

# 2. Read app_old.js
with open(app_old_path, 'r', encoding='utf-8') as f:
    app_old = f.read()

# 3. Create the final app.js
final_app_js = dictionaryData_js + app_old

# 4. Add the rendering logic for dictionary Content if it's missing
marked_logic = """
    const dictionaryContent = document.getElementById('dictionary-content');
    if (dictionaryContent && typeof marked !== 'undefined') {
        dictionaryContent.innerHTML = marked.parse(dictionaryData);
    }
"""

if "dictionaryContent.innerHTML = marked.parse(dictionaryData);" not in final_app_js:
    final_app_js = final_app_js.replace(
        "sprintContent.innerHTML = marked.parse(sprintData);\n    }",
        "sprintContent.innerHTML = marked.parse(sprintData);\n    }\n" + marked_logic
    )

# 5. Write to app.js
with open(app_path, 'w', encoding='utf-8') as f:
    f.write(final_app_js)

print("app.js rewritten successfully!")
