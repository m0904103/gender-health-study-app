const fs = require('fs');
const execSync = require('child_process').execSync;

// Get the content of app.js from the good commit
const oldContent = execSync('git show 6a3d809:app.js', {encoding: 'utf-8'});

// Extract quizData from oldContent
const matchOld = oldContent.match(/const quizData = (\[[\s\S]*?\]);\s*const flashcardData/);
if (!matchOld) {
    console.log("Failed to find quizData in the old commit.");
    process.exit(1);
}
const quizDataStr = matchOld[1];

// Now load the current app.js
const currentContent = fs.readFileSync('app.js', 'utf-8');

// The current app.js has:
// const readAloudData = [...]
// const flashcardData = [...]
// We need to re-insert quizData right before readAloudData, or at the top of the file.
// Originally, the order was: readAloudData, quizData, flashcardData?
// Let's check oldContent array declarations
const lines = oldContent.split('\n');
lines.forEach((l, i) => { if(l.includes('const ') && l.includes('Data = [')) console.log(i + ': ' + l.trim()); });

// Actually, I can just append `const quizData = ` + quizDataStr + `;\n` right before `const flashcardData = [`
const newContent = currentContent.replace('const flashcardData = [', 'const quizData = ' + quizDataStr + ';\n\nconst flashcardData = [');
fs.writeFileSync('app.js', newContent, 'utf-8');
console.log("Successfully restored quizData!");
