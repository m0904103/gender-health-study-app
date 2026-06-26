const fs = require('fs');
const content = fs.readFileSync('app.js', 'utf-8');

const match = content.match(/const quizData = (\[[\s\S]*?\]);\s*const flashcardData/);
if (!match) process.exit(1);

const dataStr = match[1];
let quizData;
eval('quizData = ' + dataStr);

const toDelete = new Set([7, 16, 23, 25]);
const newQuizData = quizData.filter((_, idx) => !toDelete.has(idx));
console.log("New length:", newQuizData.length);

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
console.log("Successfully removed manual duplicates.");
