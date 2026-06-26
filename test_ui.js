const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('index.html', 'utf-8');
const scriptContent = fs.readFileSync('app.js', 'utf-8');

const dom = new JSDOM(html, { runScripts: "dangerously" });

// Mock marked
dom.window.marked = { parse: (text) => `<p>${text}</p>` };

// Mock speechSynthesis
dom.window.speechSynthesis = {
    getVoices: () => [],
    addEventListener: () => {}
};

// Inject the script manually to ensure it runs
const scriptEl = dom.window.document.createElement("script");
scriptEl.textContent = scriptContent;
dom.window.document.body.appendChild(scriptEl);

// Wait a tiny bit for DOMContentLoaded equivalents (app.js uses document.addEventListener('DOMContentLoaded', ...))
// Since we injected after parsing, we need to trigger the event manually
const event = dom.window.document.createEvent('Event');
event.initEvent('DOMContentLoaded', true, true);
dom.window.document.dispatchEvent(event);

setTimeout(() => {
    try {
        const quizTitle = dom.window.document.getElementById('quiz-q-title');
        const quizCounter = dom.window.document.getElementById('quiz-counter');
        const quizOptions = dom.window.document.getElementById('quiz-options');
        
        console.log("--- QUIZ RENDER TEST ---");
        console.log("Title Element:", quizTitle ? quizTitle.textContent : "Not Found");
        console.log("Counter Element:", quizCounter ? quizCounter.textContent : "Not Found");
        
        if (quizOptions) {
            console.log(`Number of options rendered: ${quizOptions.children.length}`);
            for(let i=0; i<quizOptions.children.length; i++){
                console.log(` Option ${i+1}: ${quizOptions.children[i].textContent}`);
            }
        } else {
            console.log("quizOptions container Not Found");
        }

        // Test clicking next
        const nextBtn = dom.window.document.getElementById('next-quiz');
        if (nextBtn) {
            console.log("\n--- CLICKING NEXT ---");
            nextBtn.click();
            console.log("Title after click:", dom.window.document.getElementById('quiz-q-title').textContent);
            console.log("Counter after click:", dom.window.document.getElementById('quiz-counter').textContent);
        }

    } catch (e) {
        console.log("Error during test:", e);
    }
}, 100);
