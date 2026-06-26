const gameData = [
    {
        id: 'pcos',
        title: '第一型糖尿病與 PCOS',
        icon: 'fa-venus',
        blocks: [
            { order: 1, type: '起', text: '不是老胖專利', detail: '破除刻板印象，點出性別差異' },
            { order: 2, type: '承', text: '年輕女性挑戰', detail: '第一型糖尿病女性面臨內分泌失調' },
            { order: 3, type: '轉', text: '治療反而致病', detail: '注射外源性胰島素誘發高胰島素血症' },
            { order: 4, type: '合', text: '卵巢誘發PCOS', detail: 'IDF 提倡糖尿病性別敏感度' }
        ]
    },
    {
        id: 'global',
        title: '全球化 vs. 全球在地化',
        icon: 'fa-globe',
        blocks: [
            { order: 1, type: '起', text: '外來衝擊', detail: '全球化帶來一體化與同質性' },
            { order: 2, type: '承', text: '保有本土', detail: '面對衝擊，重新尋找在地差異性' },
            { order: 3, type: '轉', text: '揉合新面貌', detail: '拒絕單向入侵，展現文化自信' },
            { order: 4, type: '合', text: '麥當勞薯來堡', detail: '全球在地化 Glocalization' }
        ]
    },
    {
        id: 'ngo',
        title: 'NGO 同志諮詢熱線',
        icon: 'fa-hands-helping',
        blocks: [
            { order: 1, type: '起', text: '弱勢遭污名', detail: '主流體制僵化，多元族群被邊緣化' },
            { order: 2, type: '承', text: 'NGO接住你', detail: '成為社會安全網，如同志諮詢熱線' },
            { order: 3, type: '轉', text: '多元化服務', detail: '服務擴及家庭，如同志父母下午茶' },
            { order: 4, type: '合', text: '實質法援出櫃', detail: '提供醫療法令與出櫃實質協助' }
        ]
    },
    {
        id: 'cedaw',
        title: 'CEDAW 公約與性別主流化',
        icon: 'fa-balance-scale',
        blocks: [
            { order: 1, type: '起', text: '看見差異', detail: '推動性別主流化，重視性別統計' },
            { order: 2, type: '承', text: '國際標準', detail: 'CEDAW 國內法化，定期發表國家報告' },
            { order: 3, type: '轉', text: '超越形式', detail: '打破齊頭式平等，追求「實質平等」' },
            { order: 4, type: '合', text: '三大核心', detail: '不歧視、實質平等、國家義務' }
        ]
    }
];

let currentTopic = null;
let sortableInstance = null;
let completedTopics = new Set();

const screens = {
    selection: document.getElementById('topic-selection'),
    play: document.getElementById('play-screen')
};

function switchScreen(screenName) {
    Object.values(screens).forEach(s => s.classList.remove('active'));
    screens[screenName].classList.add('active');
}

function initGame() {
    const grid = document.getElementById('topic-grid');
    grid.innerHTML = '';
    
    gameData.forEach(topic => {
        const isCompleted = completedTopics.has(topic.id);
        const card = document.createElement('div');
        card.className = `topic-card ${isCompleted ? 'completed' : ''}`;
        card.innerHTML = `
            <i class="fas ${topic.icon}"></i>
            <h3>${topic.title}</h3>
        `;
        card.addEventListener('click', () => startTopic(topic));
        grid.appendChild(card);
    });

    document.getElementById('success-count').textContent = completedTopics.size;
}

function startTopic(topic) {
    currentTopic = topic;
    document.getElementById('current-topic-title').textContent = topic.title;
    
    // Shuffle blocks
    const shuffled = [...topic.blocks].sort(() => Math.random() - 0.5);
    
    const list = document.getElementById('sortable-list');
    list.innerHTML = '';
    
    shuffled.forEach(block => {
        const el = document.createElement('div');
        el.className = 'sortable-block';
        el.dataset.order = block.order;
        el.innerHTML = `
            <i class="fas fa-grip-lines drag-handle"></i>
            <div class="block-content">
                <div class="block-text">${block.text}</div>
                <div class="block-detail">${block.detail}</div>
            </div>
        `;
        list.appendChild(el);
    });

    if (sortableInstance) {
        sortableInstance.destroy();
    }

    sortableInstance = new Sortable(list, {
        animation: 150,
        ghostClass: 'sortable-ghost',
        dragClass: 'sortable-drag'
    });

    switchScreen('play');
}


// --- Web Audio API Sound Effects ---
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playSuccessSound() {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    
    // Pleasant chime (C5, E5, G5, C6)
    const notes = [523.25, 659.25, 783.99, 1046.50]; 
    const now = audioCtx.currentTime;
    
    notes.forEach((freq, i) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + i * 0.1);
        
        gain.gain.setValueAtTime(0, now + i * 0.1);
        gain.gain.linearRampToValueAtTime(0.3, now + i * 0.1 + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.01, now + i * 0.1 + 0.5);
        
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        osc.start(now + i * 0.1);
        osc.stop(now + i * 0.1 + 0.5);
    });
}

function playErrorSound() {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    
    // Discordant low buzzer
    const osc1 = audioCtx.createOscillator();
    const osc2 = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    
    const now = audioCtx.currentTime;
    
    osc1.type = 'sawtooth';
    osc1.frequency.setValueAtTime(150, now);
    
    osc2.type = 'square';
    osc2.frequency.setValueAtTime(155, now);
    
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.2, now + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);
    
    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(audioCtx.destination);
    
    osc1.start(now);
    osc2.start(now);
    osc1.stop(now + 0.4);
    osc2.stop(now + 0.4);
}
// ------------------------------------

document.getElementById('check-btn').addEventListener('click', () => {

    const blocks = document.querySelectorAll('.sortable-block');
    let isCorrect = true;
    
    blocks.forEach((block, index) => {
        const correctOrder = index + 1;
        const actualOrder = parseInt(block.dataset.order);
        
        if (actualOrder !== correctOrder) {
            isCorrect = false;
            if(index === 0) playErrorSound(); // only play once per check
            // Shake effect for wrong blocks
            block.classList.add('shake');
            setTimeout(() => block.classList.remove('shake'), 500);
        } else {
            // Glow effect for correct blocks
            block.classList.add('success-glow');
        }
    });

    if (isCorrect) {
        triggerSuccess();
    }
});

function triggerSuccess() {
    playSuccessSound();
    completedTopics.add(currentTopic.id);
    
    // Confetti!
    const duration = 2000;
    const end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 5,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: ['#6366f1', '#10b981', '#fcd34d']
        });
        confetti({
            particleCount: 5,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: ['#6366f1', '#10b981', '#fcd34d']
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    }());

    setTimeout(() => {
        document.getElementById('success-overlay').classList.remove('hidden');
    }, 500);
}

document.getElementById('next-topic-btn').addEventListener('click', () => {
    document.getElementById('success-overlay').classList.add('hidden');
    initGame();
    switchScreen('selection');
});

// Initialize on load
initGame();
