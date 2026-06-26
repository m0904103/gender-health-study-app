import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'const quizData = (\[.*?\]);', content, re.DOTALL)
if m:
    data_str = m.group(1)
    print("Length of matched quizData string:", len(data_str))
    print("Number of 'q':", data_str.count('"q"'))
    print("Number of q:", data_str.count('q:'))
    print("Number of question:", data_str.count('question:'))
    print("First 500 chars:")
    print(data_str[:500])
    
    # Try to parse it and get length
    import json
    try:
        # Need to fix unquoted keys for json
        json_str = re.sub(r'([{,]\s*)([a-zA-Z0-9_]+)\s*:', r'\1"\2":', data_str)
        # Fix trailing commas
        json_str = re.sub(r',\s*([\]}])', r'\1', json_str)
        # Parse
        data = json.loads(json_str)
        print("Parsed length:", len(data))
    except Exception as e:
        print("Error parsing:", e)
else:
    print("not found")
