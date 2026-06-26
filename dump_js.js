const fs = require('fs');
const content = fs.readFileSync('app.js', 'utf-8');
const match = content.match(/const quizData = (\[[\s\S]*?\]);\s*const clozeData/);

if (match) {
    eval('var quizData = ' + match[1]);
    console.log("Total length:", quizData.length);
    quizData.forEach((q, i) => {
        console.log(`${i+1}. ${q.q || q.question}`);
    });
} else {
    console.log("Match not found");
}
