const fs = require('fs');
const content = fs.readFileSync('app.js', 'utf-8');

const match = content.match(/const quizData = (\[[\s\S]*?\]);\s*const flashcardData/);
if (!match) {
    console.log("Could not find quizData");
    process.exit(1);
}

const dataStr = match[1];
let quizData;
eval('quizData = ' + dataStr);

console.log("Original length:", quizData.length);

function normalize(str) {
    if (!str) return '';
    let s = String(str);
    s = s.replace(/\(.*?[年年].*?考題\)/g, ''); // remove (104, 106年考題)
    s = s.replace(/[^\w\u4e00-\u9fa5]/g, ''); // keep only alphanumeric and chinese
    return s;
}

const normalizedQs = quizData.map(q => normalize(q.q || q.question || ''));

const toDelete = new Set();

for (let i = 0; i < quizData.length; i++) {
    for (let j = i + 1; j < quizData.length; j++) {
        const q1 = normalizedQs[i];
        const q2 = normalizedQs[j];
        
        if (q1.length > 5 && q2.length > 5 && q1 === q2) {
            console.log(`Duplicate found:\n  [${i+1}] ${quizData[i].q}\n  [${j+1}] ${quizData[j].q}\n`);
            toDelete.add(i); // Delete the earlier one to keep the one with tags (which is usually later)
        } else if (q1.length > 5 && q2.length > 5 && (q1.includes(q2) || q2.includes(q1))) {
            console.log(`Partial duplicate found:\n  [${i+1}] ${quizData[i].q}\n  [${j+1}] ${quizData[j].q}\n`);
            toDelete.add(i);
        }
    }
}

const newQuizData = quizData.filter((_, idx) => !toDelete.has(idx));
console.log("New length:", newQuizData.length);

// Format output nicely
let newArrayStr = "[\n";
newQuizData.forEach((q, idx) => {
    newArrayStr += "    {\n";
    newArrayStr += `        "q": ${JSON.stringify(q.q || q.question)},\n`;
    newArrayStr += `        "options": [\n`;
    q.options.forEach((opt, oIdx) => {
        newArrayStr += `            ${JSON.stringify(opt)}${oIdx < q.options.length - 1 ? ',' : ''}\n`;
    });
    newArrayStr += `        ],\n`;
    newArrayStr += `        "answer": ${JSON.stringify(q.answer || q.ans)},\n`;
    newArrayStr += `        "explanation": ${JSON.stringify(q.explanation || '')}\n`;
    newArrayStr += `    }${idx < newQuizData.length - 1 ? ',' : ''}\n`;
});
newArrayStr += "]";

const newContent = content.replace(dataStr, newArrayStr);
fs.writeFileSync('app.js', newContent, 'utf-8');
console.log("Successfully deduplicated app.js");
