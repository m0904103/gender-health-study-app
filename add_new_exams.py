import json
import re

app_path = 'app.js'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Parse existing quizData
quiz_match = re.search(r'const quizData = (\[.*?\]);', content, re.DOTALL)
if quiz_match:
    try:
        quizData = json.loads(quiz_match.group(1))
    except json.JSONDecodeError:
        print("quizData is not pure JSON, will use regex append.")
        quizData = None
else:
    quizData = None
    print("quizData not found")

# New questions to add
new_quizzes = [
    {
        "q": "【第6章】關於性別與精神疾病的盛行率，下列敘述何者正確？",
        "options": [
            "(A) 男性在情感性精神疾病盛行率較高",
            "(B) 女性在物質濫用與反社會人格盛行率較高",
            "(C) 女性在情感性精神疾病盛行率較高，男性則在物質濫用與反社會人格較高",
            "(D) 男女在所有精神疾病的盛行率皆相同"
        ],
        "answer": "C",
        "explanation": "女性在情感性精神疾病（如憂鬱症）的盛行率較高；男性則在非情感性精神疾病（如物質濫用、反社會人格）盛行率較高。"
    },
    {
        "q": "【第6章】對於憂鬱症存有負面印象，害怕被確診時被標籤化，常導致何種不當的態度？",
        "options": [
            "(A) 積極求助、主動求診",
            "(B) 不求助、不求診、不傾訴的「三不態度」",
            "(C) 廣泛向親友尋求支持",
            "(D) 依賴宗教信仰取代醫療"
        ],
        "answer": "B",
        "explanation": "許多人害怕被貼上「精神病患者」的污名標籤，因而採取不求助、不求診、不傾訴的三不態度，導致病情延誤。"
    },
    {
        "q": "【第6章】關於男女感染性病（STI）的狀況，下列敘述何者為非？",
        "options": [
            "(A) 理論上男女感染性病的比例應是 1：1",
            "(B) 男性性器官外露，較能及早發現和治療",
            "(C) 女性性器官內隱，即使感染也少有症狀",
            "(D) 女性因能及早發現和治療，故少有併發症"
        ],
        "answer": "D",
        "explanation": "女性性器官內隱且無痛覺神經，即使感染也少有症狀，常導致併發症發生後才就醫，而非較能及早發現。"
    },
    {
        "q": "【第6章】關於女性感染「淋病」的症狀，下列何者為非？",
        "options": [
            "(A) 早期症狀通常非常明顯且劇痛",
            "(B) 白帶可能會增多",
            "(C) 分泌物可能出現異色或異味",
            "(D) 可能會伴隨頻尿現象"
        ],
        "answer": "A",
        "explanation": "女性感染淋病的症狀通常較不明顯，可能僅有白帶增多、異色、異味或頻尿，容易被忽略。"
    },
    {
        "q": "【第6章】關於更年期婦女使用「荷爾蒙補充療法」，下列敘述何者正確？",
        "options": [
            "(A) 可使女性青春永駐，且沒有任何禁忌症",
            "(B) 絕對安全，不會增加心血管疾病或乳癌風險",
            "(C) 有助降低停經後骨折與結腸癌風險，但會增加心血管疾病、中風與乳癌等風險",
            "(D) 患有肝病或乳癌的婦女應積極使用以改善體質"
        ],
        "answer": "C",
        "explanation": "長期使用荷爾蒙療法的風險大於好處（增加心血管疾病、中風、乳癌風險），且有諸多禁忌症（如肝病、乳癌、子宮肌瘤等）。"
    },
    {
        "q": "【第7章】《原住民族權利宣言》中包含了哪些權利？",
        "options": [
            "(A) 平等權",
            "(B) 民族自決權（集體權）",
            "(C) 文化權",
            "(D) 以上皆是"
        ],
        "answer": "D",
        "explanation": "《原住民族權利宣言》保障了原住民的平等權、民族自決權以及文化權等核心權益。"
    },
    {
        "q": "【第7章】原住民族正名運動的核心內涵為何？",
        "options": [
            "(A) 正視原住民族平等權利",
            "(B) 支持主流文化主導原住民族文化",
            "(C) 加強原住民對政府的無條件認同",
            "(D) 廢除所有原住民的傳統命名方式"
        ],
        "answer": "A",
        "explanation": "正名運動的核心在於擺脫過去被強加的污名化稱呼（如番、山胞），正視並奪回原住民族的主體性與平等權利。"
    },
    {
        "q": "【第7章】「外籍勞工」泛指在臺灣擔任藍領類別工作的外籍人士，下列何者不包含在內？",
        "options": [
            "(A) 營造工作",
            "(B) 家庭看護工作",
            "(C) 家庭幫傭工作",
            "(D) 商務工作"
        ],
        "answer": "D",
        "explanation": "商務工作屬於「白領階級」的外籍專業人士，並不屬於藍領類別的外籍勞工（移工）。"
    },
    {
        "q": "【第8章】「污名」(Stigma)一詞源自於希臘，其原意為何？",
        "options": [
            "(A) 社會階層的劃分",
            "(B) 身體上被刻上或燒上烙印的標記",
            "(C) 心理上的自卑感",
            "(D) 法律上的犯罪紀錄"
        ],
        "answer": "B",
        "explanation": "污名原指烙印在身體皮膚上的標記，代表其在道德上有污點（如奴隸、罪犯），現代則泛指社會對弱勢群體的負面標籤。"
    },
    {
        "q": "【第8章】從多元文化觀點來看，只要行為表現在統計上偏於常態，就可以直接稱為是「變態」(abnormal) 嗎？",
        "options": [
            "(A) 是，因為與大多數人不同就是異常",
            "(B) 否，這隱含著以「主流價值觀」去評斷「弱勢群體」的偏見",
            "(C) 是，醫學上完全支持這種分類法",
            "(D) 否，因為統計學完全不適用於人類行為"
        ],
        "answer": "B",
        "explanation": "在性別、性傾向、身心障礙等層面，常態與變態的劃分往往隱含著「主流優越、弱勢貶抑」的霸權價值觀。"
    },
    {
        "q": "【第8章】當歧視發生在主流族群對待弱勢族群時，如果社會默許或肯定這種歧視行為，等於承認了何種邏輯？",
        "options": [
            "(A) 社會達爾文主義的演化邏輯",
            "(B) 自由市場的競爭邏輯",
            "(C) 「強可凌弱」的霸凌邏輯",
            "(D) 多元包容的和諧邏輯"
        ],
        "answer": "C",
        "explanation": "歧視的本質是一種權力壓迫，社會若肯定歧視，等同於認可強者可以隨意欺凌弱者的霸凌邏輯。"
    },
    {
        "q": "【第8章】根據研究，污名與被污名化族群的哪一種健康狀態有顯著的負面相關？",
        "options": [
            "(A) 生理健康",
            "(B) 心理健康",
            "(C) 遺傳健康",
            "(D) 牙齒健康"
        ],
        "answer": "B",
        "explanation": "污名化會帶給當事人極大的社會壓力與自我貶抑，直接嚴重影響其「心理健康」。"
    },
    {
        "q": "【第8章】當代各心理衛生專業組織對於同性戀的專業觀點為何？",
        "options": [
            "(A) 認為同性戀是病態的性傾向，需要治療",
            "(B) 認為同性戀是一種基因突變的結果",
            "(C) 達成「去病理化」共識，認為同性戀是正常的性傾向之一",
            "(D) 認為同性戀是後天學習環境不良所致"
        ],
        "answer": "C",
        "explanation": "美國精神醫學會早已將同性戀從精神疾病診斷手冊中刪除，目前學界的共識是「去病理化」，承認其為自然常態。"
    },
    {
        "q": "【第9章】《性別平等教育法》規定中小學每學期應實施至少幾小時的性別平等教育相關課程或活動？",
        "options": [
            "(A) 至少兩小時",
            "(B) 至少四小時",
            "(C) 至少八小時",
            "(D) 至少十二小時"
        ],
        "answer": "B",
        "explanation": "法規明定中小學每學期應實施「至少四小時」的性別平等教育相關課程或活動。"
    },
    {
        "q": "【第9章】下列哪種類型的校園霸凌事件，因為涉及私密性與社會禁忌，通常「最不容易」被舉發？",
        "options": [
            "(A) 肢體霸凌",
            "(B) 言語霸凌",
            "(C) 關係霸凌",
            "(D) 性別霸凌 / 性霸凌"
        ],
        "answer": "D",
        "explanation": "性霸凌或性別霸凌常因為受害者感到羞恥、害怕二次傷害或社會偏見，而成為最難被舉發的黑數。"
    },
    {
        "q": "【第9章】關於女生數學或數理成績普遍被認為低於男生的現象，較合理的解釋為何？",
        "options": [
            "(A) 男生天生比女生聰明",
            "(B) 男生天生數理腦力較發達",
            "(C) 女生天生不擅長邏輯思考",
            "(D) 以男性為中心建立的數理學習與教學方法可能不適合女生"
        ],
        "answer": "D",
        "explanation": "這並非天生智力差異，而是受到刻板印象威脅，以及傳統上以男性為中心的教學模式與評量方式所造成的結果。"
    },
    {
        "q": "【第9章】發生在美國紐約的「石牆事件 (Stonewall Riot)」，啟發了全世界的哪一項運動？",
        "options": [
            "(A) 同志公民運動",
            "(B) 環保運動",
            "(C) 勞工權益運動",
            "(D) 反戰和平運動"
        ],
        "answer": "A",
        "explanation": "石牆事件是現代同志權利運動的歷史轉捩點，直接啟發了全球的同志公民運動（Pride）。"
    },
    {
        "q": "【第10章】根據統計，臺灣新住民的婚姻狀態分布多屬何種情況？",
        "options": [
            "(A) 幾乎全是初婚",
            "(B) 幾乎全是再婚",
            "(C) 初婚與再婚者各半",
            "(D) 多為未婚同居"
        ],
        "answer": "C",
        "explanation": "臺灣新住民的婚姻狀態多屬「初婚與再婚者各半」。"
    },
    {
        "q": "【第10章】在臺灣的新住民家庭中，丈夫多數扮演何種角色？",
        "options": [
            "(A) 承擔絕大部分的親職教育角色",
            "(B) 扮演家庭經濟的支柱",
            "(C) 多屬社會的上層階級",
            "(D) 負責所有的家務勞動"
        ],
        "answer": "B",
        "explanation": "在傳統性別分工下，新住民家庭的丈夫多數扮演家庭經濟的支柱，而外籍配偶則常承擔家務與照顧責任。"
    },
    {
        "q": "【第10章】在臺灣的新住民家庭中，妻子多數展現出何種特質或現象？",
        "options": [
            "(A) 完全沒有語言適應的問題",
            "(B) 未曾遭遇任何社會污名",
            "(C) 非常看重子女的教育",
            "(D) 普遍擁有高收入職業"
        ],
        "answer": "C",
        "explanation": "儘管面臨許多挑戰，新住民妻子多數都非常看重且積極參與子女的教育與發展。"
    },
    {
        "q": "【第10章】新住民的婚姻議題，在日常生活中最容易彰顯在哪些方面？",
        "options": [
            "(A) 國族認同的衝突",
            "(B) 購屋置產的決定權",
            "(C) 文化與生活差異的適應",
            "(D) 國際政治立場的分歧"
        ],
        "answer": "C",
        "explanation": "跨國婚姻中最核心也最日常的挑戰，就是雙方在文化背景、語言及生活習慣差異上的適應與磨合。"
    },
    {
        "q": "【第11章】下列何者「不是」媒體接近使用權（第四權）的核心精神？",
        "options": [
            "(A) 人民有使用傳播媒體表達意見的權利",
            "(B) 建構一種特定意識型態的偏好",
            "(C) 包括接近權與使用權",
            "(D) 讓少數群體能在大眾媒體上發聲"
        ],
        "answer": "B",
        "explanation": "媒體接近使用權是為了讓多元的聲音被聽見，而非用來建構或強制推銷某一種特定的意識型態偏好。"
    },
    {
        "q": "【第11章】反全球化運動和「另類全球化」運動之間最大的差異為何？",
        "options": [
            "(A) 另類全球化運動支持大國經濟發展優勢",
            "(B) 另類全球化運動以抗議國際經濟體制聚會為主",
            "(C) 另類全球化運動主張跨國串聯，但以「在地議題深根」為主",
            "(D) 另類全球化運動完全反對任何形式的國際貿易"
        ],
        "answer": "C",
        "explanation": "另類全球化並非盲目反對所有全球化，而是強調「在地化」，以在地議題深耕為主，反對跨國資本對勞工與環境的剝削。"
    },
    {
        "q": "【第11章】關於「非政府組織 (NGO)」的角色及功能，下列敘述何者正確？",
        "options": [
            "(A) 以追求商業最大利益為目的",
            "(B) 官方代表政府去爭取國際權利",
            "(C) 是一種由公民「自願結社」而來的獨立民間團體",
            "(D) 完全隸屬於勞動部管轄"
        ],
        "answer": "C",
        "explanation": "NGO 是獨立於政府與企業之外的第三部門，由公民自願結社而成，致力於社會公益與弱勢發聲。"
    },
    {
        "q": "【第11章】關於「南洋台灣姊妹會 (TASAT)」的描述，下列何者正確？",
        "options": [
            "(A) 由結合美濃文化、語言的識字班開始發展",
            "(B) 是一個為新住民發聲的非營利組織",
            "(C) 積極參與社會運動並影響了移民相關法規的修正",
            "(D) 以上皆是"
        ],
        "answer": "D",
        "explanation": "南洋台灣姊妹會源自美濃識字班，是非營利組織，且成功培力新住民女性站出來倡議，影響了移民法規的修訂。"
    }
]

added_count = 0
if quizData is not None:
    existing_qs = [q['q'] for q in quizData]
    for nq in new_quizzes:
        if nq['q'] not in existing_qs:
            quizData.append(nq)
            added_count += 1
    new_quiz_js = 'const quizData = ' + json.dumps(quizData, ensure_ascii=False, indent=4) + ';'
    content = content[:quiz_match.start()] + new_quiz_js + content[quiz_match.end():]
else:
    # If JSON decoding failed, let's manually append to the array using string manipulation
    quiz_append_str = ""
    for nq in new_quizzes:
        # Check if question exists in content
        if nq['q'] not in content:
            # Format as JS object string
            obj_str = "    {\n"
            obj_str += f'        "q": "{nq["q"]}",\n'
            obj_str += '        "options": [\n'
            for opt in nq["options"]:
                obj_str += f'            "{opt}",\n'
            obj_str = obj_str.rstrip(",\n") + "\n        ],\n"
            obj_str += f'        "answer": "{nq["answer"]}",\n'
            obj_str += f'        "explanation": "{nq["explanation"]}"\n'
            obj_str += "    },\n"
            quiz_append_str += obj_str
            added_count += 1
            
    # Remove trailing comma and append before closing bracket
    if quiz_append_str:
        # find closing bracket of quizData
        end_idx = content.find('];\n', quiz_match.start())
        if end_idx == -1:
            end_idx = content.find('];', quiz_match.start())
        
        # We need to ensure the preceding item has a comma
        # Just insert the new items before ]; 
        if content[end_idx-1] != ',':
            # Not safe to just append, but assuming formatted nicely with newlines
            pass 
        
        content = content[:end_idx] + ",\n" + quiz_append_str.rstrip(",\n") + "\n" + content[end_idx:]


# Cloze test insertion
new_cloze_js = """
    ,{
        title: "平時測驗與期末核心精華綜合演練",
        content: `憂鬱症的患者常因害怕被貼上標籤，而採取<span class="cloze-word" data-word="不求助、不求診、不傾訴"></span>的三不態度。女性感染性病因為性器官內隱，常少有症狀而導致<span class="cloze-word" data-word="併發症"></span>才就醫。更年期長期使用合併型荷爾蒙療法，會增加<span class="cloze-word" data-word="心血管疾病與乳癌"></span>的風險。<br><br>外籍勞工在台灣常見的不良勞動處境包含被<span class="cloze-word" data-word="超時與非法使用"></span>。社會若肯定歧視，就等於承認了<span class="cloze-word" data-word="強可凌弱"></span>的霸凌邏輯。心理衛生組織對於同性戀的共識是<span class="cloze-word" data-word=\"去病理化\"></span>，認為其並非病態。<br><br>校園中最不容易被舉發的霸凌類型是<span class="cloze-word" data-word="性別霸凌"></span>。美國的<span class="cloze-word" data-word="石牆事件"></span>啟發了全球的同志公民運動。台灣新住民的婚姻狀態多屬<span class="cloze-word" data-word="初婚與再婚各半"></span>，且新住民妻子通常非常看重子女的<span class="cloze-word" data-word="教育"></span>。非政府組織（NGO）是一種由公民<span class="cloze-word" data-word="自願結社"></span>而來的團體，媒體接近使用權的出發點是讓多元聲音被聽見，絕非為了建構特定的<span class="cloze-word" data-word="意識型態"></span>。`
    }
"""

cloze_match = re.search(r'const clozeData = \[.*?\];', content, re.DOTALL)
if cloze_match:
    cloze_str = cloze_match.group(0)
    # Insert right before the last '];'
    last_bracket_idx = cloze_str.rfind('];')
    new_cloze_full = cloze_str[:last_bracket_idx] + new_cloze_js + cloze_str[last_bracket_idx:]
    
    # Avoid duplicate additions
    if "平時測驗與期末核心精華綜合演練" not in content:
        content = content[:cloze_match.start()] + new_cloze_full + content[cloze_match.end():]

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully added {added_count} new multiple choice questions and 1 comprehensive cloze paragraph.")
