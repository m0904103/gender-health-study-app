// --- 資料區：涵蓋所有終極講義考點 ---

const readAloudData = [
    {
        title: "第六章：性別醫學之議題初探",
        content: `脈絡說書：傳統的「生物醫學模式」把人體當成機器，生病只看器官故障。但本課程提倡的「社會心理模式」認為，健康受生理、心理與社會環境交互影響。以憂鬱症為例，女性盛行率是男性的兩倍，這不是因為女性天生脆弱，而是社會角色的重擔（如無酬家庭照顧、職場雙重班別）害的。而性傳染病更殘酷，女性因為生理構造內隱，子宮頸易受感染卻無痛覺神經，往往成為「沈默帶原者」，直到發生嚴重併發症（不孕、子宮外孕）才就醫。
        
        核心概念：女性憂鬱常表現為「退縮、孤立、失去興趣」；男性受刻板印象影響不願示弱，常以「動怒生氣、酗酒、家暴」掩蓋。婚姻對「男性」精神健康具保護效果；但對「女性」則相反。更年期轉變期特徵為月經週期不規則或無月經超過60天。賀爾蒙補充療法(HRT)會增加心血管疾病與乳癌風險。大豆異黃酮無法緩解陰道萎縮引起的性交疼痛。愛滋病本國籍感染者男性占93%，女性常因異性間性行為被配偶感染。`
    },
    {
        title: "第七章：臺灣多元族群處境",
        content: `脈絡說書：早期政府採取「同化（漢化）政策」，實行國語一元化、全面禁止母語，導致原住民族文化與認同嚴重流失。直到 1980 年代原住民族發起正名與母語復興運動，才逐漸爭回主體性。而外籍移工是臺灣不可或缺的藍領基層，但目前的法律政策仍對他們有許多限制（如禁止自由轉換雇主），使其處於不自由的勞動體制中。
        
        核心概念：原住民山地教育三方針核心在於建立單一的國家認同。1953年《促進山地行政建設計畫大綱》核心為「山地平地化」的漢化政策。聯合國原住民族權利宣言確立平等權、民族自決權、文化權。1994年修憲將「山胞」正名為「原住民」。移工政策視其為「客工」，藍領移工不得任意轉換雇主。移工不良勞動類型包含：降低與扣除工資、強迫扣押護照與儲蓄、強迫加班、任意解雇與強制遣返、超時與非法使用。高達半數以上外籍看護工完全無例假日。`
    },
    {
        title: "第八章：社會污名與心理健康",
        content: `脈絡說書：大腦為了快速分類記憶，會形成「基模」。當基模變成固定且僵化的「刻板印象」時，就會對特定群體造成傷害。「污名」是主流社會賦予弱勢群體的巨大負面標籤。污名不僅會引發「自我實現預言」讓弱勢者處境更糟，更會形成「微攻擊」，在日常生活中以看似無辜的言行不斷貶低、傷害性別多樣化（LGBTQ）或特定疾病患者。
        
        核心概念：基模是用以分類處理與記憶的結構信念。自我實現預言指刻板印象引發他人相應行為，最終肯定了最初的刻板印象。刻板印象威脅指負面刻板印象被活化時引發當事人焦慮，損害實際表現。Goffman 污名包含「明顯遭受貶抑者」（如顏面傷殘）與「可能遭受貶抑者」（如同性戀）。Goffman 三大污名類型為：身體缺陷、個人失序行為、部族污名（不包含貧富差距）。微攻擊是隱晦、細微的貶低行為。美國精神醫學學會於1973年正式將同性戀去病化。`
    },
    {
        title: "第九章：性別教育與弱勢族群處境",
        content: `脈絡說書：臺灣性別教育的深化，是歷史上無數玫瑰少年的眼淚換來的。過去的「兩性教育」只看男女生理差異；現代的「性別教育」則探討社會權力運作與多元性別特質。《性別平等教育法》的推動，就是要打破「男理工、女人文」的性別分流刻板印象，並透過同志教育消除校園中的性霸凌。
        
        核心概念：2000年葉永鋕事件促使《兩性平等教育法》改制為《性別平等教育法》，將性傾向、性別特質、性別認同正式納入保障。性平教育三大法定內涵包含情感、性、同志教育。數理與科學領域教師在融入性別議題教學上最待充實。舉止娘娘腔的男生與同志學生是校園霸凌高危險群，且目睹者最無意願提供協助的就是「性霸凌」。北美同志運動里程碑為1969年石牆事件。哈維·繆克是美國首位出櫃政治人物。`
    },
    {
        title: "第十章：跨國婚姻與新住民",
        content: `脈絡說書：1980年代東南亞女性透過婚配大量移入臺灣。大眾常帶偏見看待「商品化婚姻」。但實證研究打破汙名，新住民家庭衝突關鍵往往是「經濟弱勢」與結構壓迫，而非「外籍身分」。婚姻輔導應聚焦在弱勢家庭的賦權。
        
        核心概念：婚姻斜坡理論指女性從貧困遷移至富庶區域。實證數據顯示，新住民女性所生子女在健康指標甚至優於本籍配偶，心智與學習行為無顯著差異。新住民女性遠嫁動機多為改善原生家庭經濟，初來台最大障礙為語言溝通隔閡。臺灣丈夫壓力源為經濟重擔、文化歧視與掌控衝突。`
    },
    {
        title: "第十一章：全球化、公民社會與多元文化",
        content: `脈絡說書：在全球化世界，一個國家的決策會跨國界影響全球。傳統只掃門前雪的冷漠會引發「草原的悲劇」。現代「多元文化公民社會參與」強調不分種族、性傾向站出來支持平權，善用媒體接近使用權與網路媒介為弱勢發聲，打破主流文化霸權。
        
        核心概念：草原的悲劇指過度擴張私利對公益冷漠，終將導致公共資源枯竭危及自身。第三世界國家在全球化面臨困境，因小國利益在多數決中喪失。媒體接近使用權是少數族群挑戰主流文化霸權的工具。南洋臺灣姊妹會是臺灣首個新住民姊妹自行組織的NPO。臺灣國際勞工協會(TIWA)長期組織移工遊行。跨國倡議網絡不需單一跨國認同，而是彈性跨國界連結多元社會運動。`
    }
];

const flashcardData = [
    {
        q: "題型一：請詳細說明社會心理學中「偏見（Prejudice）」與「歧視（Discrimination）」的定義，並請針對兩者的差異，各舉一個生活中的實例說明之。",
        a: `<ul>
                <li><b>偏見（認知與態度）：</b>指根據不足夠或不正確的證據，對特定族群團體的成員，所採取的一種負面的「內在態度與想法」。<br><i>實例：在路上看到行車慢的車輛，便產生「女人果然都不會開車」的刻板偏見。</i></li>
                <li><b>歧視（行為）：</b>指基於個人的性別、種族等特徵，在公共領域或日常互動中，給予不平等的「差別待遇或排斥」的「外在不公行為」。<br><i>實例：房東拒絕將房屋出租給外籍移工或同志群體。</i></li>
            </ul>`
    },
    {
        q: "題型二：Goffman 將「污名（Stigma）」定義為主流社會成員對弱勢群體給予負面標籤的歷程。請列述 Goffman 所提出的三種不同污名類型，並各舉一病理或社會現象說明之。",
        a: `<ul>
                <li><b>身體上令人厭惡的缺陷：</b>外表上明顯可被辨識的身體殘缺或外觀特異。例如：顏面傷殘者、漢生病造成的肢體變形。</li>
                <li><b>個人特質與失序行為的污名：</b>個人的精神狀態、過去紀錄或違反常規的行為。例如：思覺失調症患者、愛滋病感染者、吸毒成癮者、同性戀。</li>
                <li><b>人種、民族國籍與宗教的部族污名 (Tribal Stigma)：</b>與出身背景有關，且常透過世襲傳遞。例如：對原住民族的漢化歧視、對東南亞新住民的種族刻板偏見。</li>
            </ul>
            <p style="color: #f43f5e; font-size: 0.9em; margin-top: 10px;">⚠️ 注意：經濟階級的貧富差距不屬於這三大污名類型。</p>`
    },
    {
        q: "題型三：請從歷史脈絡詳細說明，《性別平等教育法》是由哪一個校園關鍵事件所催生？並請說明傳統的「兩性教育」與現代的「性別教育」在核心關懷上有何本質上的差異？",
        a: `<ul>
                <li><b>關鍵事件：</b>2000年屏東高樹國中「葉永鋕事件」。葉永鋕因陰柔性別氣質遭校園霸凌，不敢在下課上廁所，終因意外致死。此事件促使《兩性平等教育法》擴張為《性別平等教育法》。</li>
                <li><b>兩性教育：</b>侷限於生理「男與女」二元變項，著重男女生理差異，追求形式上的對等與一視同仁。</li>
                <li><b>性別教育：</b>引進「社會性別」批判視角。將「性傾向、性別特質、性別認同」納入保障，解構權力運作與刻板印象造成的隱形霸凌，追求「實質平權」。</li>
            </ul>`
    },
    {
        q: "題型四：跨國婚姻家庭在臺灣常面臨多重弱勢結構。請列述諮商心理師在對新住民家庭進行婚姻輔導與諮商時，應採取哪四項核心諮商策略或基本要領？",
        a: `<ol>
                <li>以<b>正面眼光</b>看待並發現新住民夫妻的優勢（如跨海遠嫁的勇氣與丈夫的努力）。</li>
                <li>協助夫妻建立生活的<b>共同體意識</b>，停止內化外界歧視。</li>
                <li>支持並鼓勵妻子<b>學習中文與追求知識</b>，擴展生活自主權。</li>
                <li>打破控制與服從的互補位階，建立<b>權力平衡</b>的互動關係（如家庭決策自主權）。</li>
                <li>鼓勵丈夫共同參與<b>家務分工</b>與學習親職技巧。</li>
                <li>尊重並鼓勵新住民配偶的<b>工作意願與能力</b>。</li>
            </ol>`
    }
];

const clozeData = [
    {
        title: "第六章 避坑指南與核心",
        content: `女性憂鬱常表現為退縮孤立，男性則常以<span class="cloze-word" data-word="動怒、酗酒或家暴"></span>來掩蓋憂鬱。婚姻對<span class="cloze-word" data-word="男性"></span>的精神健康具備保護效果，對女性則相反。更年期轉變期特徵為月經週期<span class="cloze-word" data-word="不規則"></span>或無月經超過<span class="cloze-word" data-word="60天"></span>。大豆異黃酮無法緩解陰道萎縮引起的<span class="cloze-word" data-word="性交疼痛"></span>。愛滋病只要有<span class="cloze-word" data-word="高危險行為"></span>就有風險，女性常因異性間性行為被配偶感染。`
    },
    {
        title: "第七章 避坑指南與核心",
        content: `1994年修憲正式將歧視性的「山胞」正名為<span class="cloze-word" data-word="原住民"></span>。移工政策視其為客工，藍領移工不得任意<span class="cloze-word" data-word="轉換雇主"></span>。外籍看護工面臨高達半數以上<span class="cloze-word" data-word="完全沒有例假日"></span>。原住民族教育的各項研究，法規明文規定必須有<span class="cloze-word" data-word="原住民代表參加"></span>。就業服務法對白領與藍領採取<span class="cloze-word" data-word="白領從寬、藍領從嚴"></span>的雙重標準。`
    },
    {
        title: "第八章 避坑指南與核心",
        content: `Goffman的污名雙重屬性包含「明顯遭受貶抑者」與<span class="cloze-word" data-word="「可能遭受貶抑者」"></span>。日常生活中以隱晦、細微形式傳達敵意貶低的行為稱為<span class="cloze-word" data-word="微攻擊"></span>。當群體的負面刻板印象被提醒活化時，引發當事人焦慮並損害表現，稱為<span class="cloze-word" data-word="刻板印象威脅"></span>。經濟階級的貧富差距<span class="cloze-word" data-word="不屬於"></span>Goffman定義的污名類型。`
    },
    {
        title: "第九章 避坑指南與核心",
        content: `《性別平等教育法》將性傾向、性別特質與<span class="cloze-word" data-word="性別認同"></span>正式納入法律保障。在融入性別教學上最待充實的是<span class="cloze-word" data-word="數理與科學"></span>領域教師。當目睹校園霸凌時，學生最無意願提供協助的類型是<span class="cloze-word" data-word="性霸凌"></span>。北美同志運動的全球起點是1969年的<span class="cloze-word" data-word="石牆事件"></span>。學校實施同志教育的目的是營造友善環境，絕非引導學生<span class="cloze-word" data-word="改變性傾向"></span>。`
    },
    {
        title: "第十章 避坑指南與核心",
        content: `新住民女性來台最大的初始障礙是<span class="cloze-word" data-word="語言溝通的隔閡"></span>。臺灣丈夫最大的壓力源是獨自扛起<span class="cloze-word" data-word="經濟重擔"></span>。實證研究顯示，新住民家庭子女在心智與學習行為發展上，與本國籍子女<span class="cloze-word" data-word="並無顯著差異"></span>。為了尊重其主體性，社會稱謂從帶有貶抑色彩的<span class="cloze-word" data-word="外籍新娘"></span>正名為新住民。`
    },
    {
        title: "第十一章 避坑指南與核心",
        content: `人們過度擴張私人利益，對公共事務冷漠，最終導致資源枯竭危及自身，稱為<span class="cloze-word" data-word="草原的悲劇"></span>。第三世界國家在全球化中面臨剝削，主因是小國利益在<span class="cloze-word" data-word="多數決"></span>過程中喪失。少數族群挑戰主流文化霸權、實踐文化平權的實質工具是<span class="cloze-word" data-word="媒體接近使用權"></span>。全球化下消費者權利最大的特色是<span class="cloze-word" data-word="只有權利，沒有義務"></span>，透過拒買能發揮巨大制衡力量。`
    }
];

// --- 介面控制邏輯 ---

document.addEventListener('DOMContentLoaded', () => {
    // Tab Switching
    const tabs = document.querySelectorAll('.mode-selector .btn');
    const sections = document.querySelectorAll('.content-section');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));
            
            tab.classList.add('active');
            const targetId = tab.getAttribute('data-mode');
            document.getElementById(targetId).classList.add('active');
        });
    });

    // 1. Read Aloud Logic
    const readerContent = document.getElementById('reader-content');
    readAloudData.forEach((item, index) => {
        const div = document.createElement('div');
        div.innerHTML = `<h3>${item.title}</h3><p id="read-p-${index}">${item.content.replace(/\n/g, '<br>')}</p>`;
        readerContent.appendChild(div);
    });

    const synth = window.speechSynthesis;
    let voices = [];
    const voiceSelect = document.getElementById('voice-select');

    function populateVoiceList() {
        voices = synth.getVoices().filter(voice => voice.lang.includes('zh'));
        voiceSelect.innerHTML = '';
        voices.forEach((voice, i) => {
            const option = document.createElement('option');
            option.textContent = `${voice.name} (${voice.lang})`;
            option.value = i;
            voiceSelect.appendChild(option);
        });
    }

    populateVoiceList();
    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = populateVoiceList;
    }

    let utterance = null;

    document.getElementById('play-btn').addEventListener('click', () => {
        if (synth.paused) {
            synth.resume();
            return;
        }
        synth.cancel();
        
        const fullText = readAloudData.map(d => d.title + "。" + d.content).join("。");
        utterance = new SpeechSynthesisUtterance(fullText);
        const selectedVoice = voices[voiceSelect.value];
        if(selectedVoice) utterance.voice = selectedVoice;
        utterance.rate = 1.0;
        synth.speak(utterance);
    });

    document.getElementById('pause-btn').addEventListener('click', () => {
        if (synth.speaking && !synth.paused) {
            synth.pause();
        }
    });

    document.getElementById('stop-btn').addEventListener('click', () => {
        synth.cancel();
    });

    // 2. Flashcard Logic
    let currentCardIndex = 0;
    const cardQTitle = document.getElementById('card-q-title');
    const cardQText = document.getElementById('card-q-text');
    const cardAText = document.getElementById('card-a-text');
    const counterText = document.getElementById('card-counter');
    const flashcard = document.querySelector('.flashcard');

    function loadCard(index) {
        flashcard.classList.remove('flipped');
        setTimeout(() => {
            cardQTitle.textContent = `問答題 Q${index + 1}`;
            cardQText.innerHTML = flashcardData[index].q;
            cardAText.innerHTML = flashcardData[index].a;
            counterText.textContent = `${index + 1} / ${flashcardData.length}`;
        }, 200); // Wait for unflip animation
    }

    flashcard.addEventListener('click', () => {
        flashcard.classList.toggle('flipped');
    });

    document.getElementById('prev-card').addEventListener('click', () => {
        if (currentCardIndex > 0) {
            currentCardIndex--;
            loadCard(currentCardIndex);
        }
    });

    document.getElementById('next-card').addEventListener('click', () => {
        if (currentCardIndex < flashcardData.length - 1) {
            currentCardIndex++;
            loadCard(currentCardIndex);
        }
    });

    loadCard(0);

    // 3. Cloze Logic
    const clozeContent = document.getElementById('cloze-content');
    
    clozeData.forEach(item => {
        const div = document.createElement('div');
        div.className = 'glass cloze-card';
        div.innerHTML = `<h3>${item.title}</h3><p>${item.content}</p>`;
        clozeContent.appendChild(div);
    });

    // Add click events to cloze words
    const clozeWords = document.querySelectorAll('.cloze-word');
    clozeWords.forEach(word => {
        const answer = word.getAttribute('data-word');
        word.textContent = answer; 
        
        word.addEventListener('click', function() {
            this.classList.toggle('revealed');
        });
    });

    document.getElementById('reveal-all').addEventListener('click', () => {
        clozeWords.forEach(word => {
            word.classList.add('revealed');
        });
    });
});
