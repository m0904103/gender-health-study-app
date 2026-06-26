import re

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

new_questions_js = """
    // === 歷屆考古題精選擴充 ===
    {
        question: "以下有關女性更年期敘述，何者為非？",
        options: ["是正常的卵巢功能逐漸衰退至不具功能的過渡期", "是生命過程中可以避免的生理現象", "可能有血管運動控制失調症狀", "可能有生殖泌尿道表皮萎縮現象"],
        ans: 1,
        explanation: "更年期是女性生命過程中自然且無法避免的生理現象，代表卵巢功能逐漸衰退。"
    },
    {
        question: "下列何者不是聯合國通過原住民族權利宣言所規定之權利？",
        options: ["平等權", "民族自決權", "立法權", "文化權"],
        ans: 2,
        explanation: "原住民族權利宣言規定了平等權、民族自決權與文化權等，但不包含獨立的「立法權」。"
    },
    {
        question: "學者指出臺灣的外籍勞工政策特性，下列何者「不是」其中之一？",
        options: ["保護", "排除", "篩選", "限制"],
        ans: 0,
        explanation: "台灣外勞政策主要特性為「排除」、「篩選」與「限制」，往往缺乏對外籍勞工的實質「保護」。"
    },
    {
        question: "下列何者是促發「刻板印象」的主要來源？",
        options: ["聽覺媒介", "視覺媒介", "觸覺媒介", "嗅覺媒介"],
        ans: 1,
        explanation: "促發刻板印象的主要來源是視覺媒介（如電視、電影、網路等大眾媒體呈現的固定形象）。"
    },
    {
        question: "下列何者「不是」歧視中「微攻擊 (Microaggression)」的種類？",
        options: ["微譴責", "微羞辱", "微掠奪", "微納入"],
        ans: 3,
        explanation: "微攻擊的形式通常包括微譴責、微羞辱、微掠奪與微排除，並沒有「微納入」這個種類。"
    },
    {
        question: "根據郭麗安等人(2014)的研究，校園中哪一種學生最容易成為霸凌的受害者？",
        options: ["肢體障礙者", "性別特質不合主流期待或同志", "女性", "矮小者"],
        ans: 1,
        explanation: "研究指出，校園內同志學生或性別特質不符合主流期待（如氣質陰柔的男學生）最容易成為霸凌的受害者。"
    },
    {
        question: "在臺灣對於外籍配偶的稱呼中，下列何者最能代表社會對於她們主體性的尊重？",
        options: ["外籍新娘", "新住民（新移民女性）", "陸配", "印尼新娘"],
        ans: 1,
        explanation: "從「外籍新娘」轉變為「新住民」或「新移民女性」，代表社會朝向更尊重並肯認她們主體性的轉變。"
    },
    {
        question: "近年台灣冬季受境外移入霾害嚴重，此現象代表現代民主社會應該重視什麼？",
        options: ["只需考量國家內的公共利益", "應結合多元文化公民社會參與，重視區域與全球的公共利益", "加強中央集權管理", "經濟發展優先於環境保護"],
        ans: 1,
        explanation: "跨國界的環境問題（如霾害、傳染病）凸顯了現代公民社會不能只看國內利益，也必須考量全球或區域的公共利益。"
    },
    {
        question: "「我可以接納我的朋友是同志，只要他不要表現得太娘就好」，這句話可能帶有何種偏見？",
        options: ["微攻擊", "性別平等", "性別友善", "多元包容"],
        ans: 0,
        explanation: "這是一種「微攻擊」，表面上似乎接納，實際上卻在語言中給予輕視或限制對方展現自我的框架。"
    },
    {
        question: "國際上的反性騷擾「ME TOO」運動，在社會學上可視為何種力量的展現？",
        options: ["提倡多元文化", "落實性別平等教育法", "跨國倡議與社會運動", "反全球化"],
        ans: 2,
        explanation: "「ME TOO」運動是透過網路社群與全球串聯，對抗性別暴力的跨國倡議與社會運動。"
    }
"""

if "以下有關女性更年期敘述，何者為非？" not in app_js:
    # Append to quizData array
    # Find the end of quizData array
    match = re.search(r'const quizData = \[(.*?)\];\s*const clozeData', app_js, re.DOTALL)
    if match:
        old_array_content = match.group(1)
        new_array_content = old_array_content + ",\n" + new_questions_js
        new_app_js = app_js.replace(match.group(1), new_array_content)
        
        with open('app.js', 'w', encoding='utf-8') as f:
            f.write(new_app_js)
        print("Successfully added 10 past exam questions.")
    else:
        print("Could not find quizData array bounds.")
else:
    print("Past exam questions already present.")
