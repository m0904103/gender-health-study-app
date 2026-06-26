const fs = require('fs');
const content = fs.readFileSync('app.js', 'utf-8');
const match = content.match(/const readAloudData = (\[[\s\S]*?\]);\s*const quizData/);
if (match) {
    fs.writeFileSync('audio_data.json', match[1]);
    console.log("Extracted audio_data.json");
} else {
    console.log("Failed to match readAloudData");
}
