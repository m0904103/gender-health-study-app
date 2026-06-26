import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# I will just write the correctly formatted JS array and replace the old block
# Wait, I can just replace the whole "// === 歷屆考古題精選擴充 ===" block.

correct_block = """
    // === 歷屆考古題精選擴充 ===
    {
        "q": "以下有關女性更年期敘述，何者為非？",
        "options": ["(A) 是正常的卵巢功能逐漸衰退至不具功能的過渡期", "(B) 是生命過程中可以避免的生理現象", "(C) 可能有血管運動控制失調症狀", "(D) 可能有生殖泌尿道表皮萎縮現象"],
        "answer": "B",
        "explanation": "更年期是女性生命過程中自然且無法避免的生理現象，代表卵巢功能逐漸衰退。"
    },
    {
        "q": "下列何者不是聯合國通過原住民族權利宣言所規定之權利？",
        "options": ["(A) 平等權", "(B) 民族自決權", "(C) 立法權", "(D) 文化權"],
        "answer": "C",
        "explanation": "原住民族權利宣言規定了平等權、民族自決權與文化權等，但不包含獨立的「立法權」。"
    },
    {
        "q": "學者指出臺灣的外籍勞工政策特性，下列何者「不是」其中之一？",
        "options": ["(A) 保護", "(B) 排除", "(C) 篩選", "(D) 限制"],
        "answer": "A",
        "explanation": "台灣外勞政策主要特性為「排除」、「篩選」與「限制」，往往缺乏對外籍勞工的實質「保護」。"
    },
    {
        "q": "下列何者是促發「刻板印象」的主要來源？",
        "options": ["(A) 聽覺媒介", "(B) 視覺媒介", "(C) 觸覺媒介", "(D) 嗅覺媒介"],
        "answer": "B",
        "explanation": "促發刻板印象的主要來源是視覺媒介（如電視、電影、網路等大眾媒體呈現的固定形象）。"
    },
    {
        "q": "下列何者「不是」歧視中「微攻擊 (Microaggression)」的種類？",
        "options": ["(A) 微譴責", "(B) 微羞辱", "(C) 微掠奪", "(D) 微納入"],
        "answer": "D",
        "explanation": "微攻擊的形式通常包括微譴責、微羞辱、微掠奪與微排除，並沒有「微納入」這個種類。"
    },
    {
        "q": "根據郭麗安等人(2014)的研究，校園中哪一種學生最容易成為霸凌的受害者？",
        "options": ["(A) 肢體障礙者", "(B) 性別特質不合主流期待或同志", "(C) 女性", "(D) 矮小者"],
        "answer": "B",
        "explanation": "研究指出，校園內同志學生或性別特質不符合主流期待（如氣質陰柔的男學生）最容易成為霸凌的受害者。"
    },
    {
        "q": "在臺灣對於外籍配偶的稱呼中，下列何者最能代表社會對於她們主體性的尊重？",
        "options": ["(A) 外籍新娘", "(B) 新住民（新移民女性）", "(C) 陸配", "(D) 印尼新娘"],
        "answer": "B",
        "explanation": "從「外籍新娘」轉變為「新住民」或「新移民女性」，代表社會朝向更尊重並肯認她們主體性的轉變。"
    },
    {
        "q": "近年台灣冬季受境外移入霾害嚴重，此現象代表現代民主社會應該重視什麼？",
        "options": ["(A) 只需考量國家內的公共利益", "(B) 應結合多元文化公民社會參與，重視區域與全球的公共利益", "(C) 加強中央集權管理", "(D) 經濟發展優先於環境保護"],
        "answer": "B",
        "explanation": "跨國界的環境問題（如霾害、傳染病）凸顯了現代公民社會不能只看國內利益，也必須考量全球或區域的公共利益。"
    },
    {
        "q": "「我可以接納我的朋友是同志，只要他不要表現得太娘就好」，這句話可能帶有何種偏見？",
        "options": ["(A) 微攻擊", "(B) 性別平等", "(C) 性別友善", "(D) 多元包容"],
        "answer": "A",
        "explanation": "這是一種「微攻擊」，表面上似乎接納，實際上卻在語言中給予輕視或限制對方展現自我的框架。"
    },
    {
        "q": "國際上的反性騷擾「ME TOO」運動，在社會學上可視為何種力量的展現？",
        "options": ["(A) 提倡多元文化", "(B) 落實性別平等教育法", "(C) 跨國倡議與社會運動", "(D) 反全球化"],
        "answer": "C",
        "explanation": "「ME TOO」運動是透過網路社群與全球串聯，對抗性別暴力的跨國倡議與社會運動。"
    }
"""

# replace everything from "// === 歷屆考古題精選擴充 ===" to the end of the array, with correct_block
# Note that my previous block ended right before the closing bracket of quizData
pattern = r'// === 歷屆考古題精選擴充 ===.*?\}\s*\];'
new_content = re.sub(pattern, correct_block + "\n];", content, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
