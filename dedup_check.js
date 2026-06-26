const fs = require('fs');
const content = fs.readFileSync('app.js', 'utf-8');

const match = content.match(/const quizData = (\[[\s\S]*?\]);\s*const flashcardData/);
if (!match) process.exit(1);

let quizData;
eval('quizData = ' + match[1]);

function normalize(str) {
    if (!str) return '';
    let s = String(str);
    s = s.replace(/\(.*?[年年].*?考題\)/g, '');
    s = s.replace(/【.*?】/g, '');
    s = s.replace(/[^\w\u4e00-\u9fa5]/g, '');
    return s;
}

const normalizedQs = quizData.map(q => normalize(q.q || q.question || ''));

let output = '';

// simple LCS length
function lcsLength(s1, s2) {
    const dp = Array(s1.length + 1).fill(0).map(() => Array(s2.length + 1).fill(0));
    let maxLen = 0;
    for (let i = 1; i <= s1.length; i++) {
        for (let j = 1; j <= s2.length; j++) {
            if (s1[i-1] === s2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
                maxLen = Math.max(maxLen, dp[i][j]);
            } else {
                dp[i][j] = 0;
            }
        }
    }
    return maxLen;
}

for (let i = 0; i < quizData.length; i++) {
    for (let j = i + 1; j < quizData.length; j++) {
        const q1 = normalizedQs[i];
        const q2 = normalizedQs[j];
        if (q1.length > 5 && q2.length > 5) {
            const common = lcsLength(q1, q2);
            const ratio = common / Math.max(q1.length, q2.length);
            if (ratio > 0.50 || common > 10) {
                output += `[${i+1}] ${quizData[i].q}\n[${j+1}] ${quizData[j].q}\nRatio: ${ratio.toFixed(2)}, Common: ${common}\n\n`;
            }
        }
    }
}

fs.writeFileSync('matches.txt', output, 'utf-8');
