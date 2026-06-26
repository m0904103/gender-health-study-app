import os
import re

app_path = r"C:\Users\manpo\.gemini\antigravity\scratch\gender-health-study-app\app.js"

with open(app_path, 'r', encoding='utf-8') as f:
    app_js = f.read()

quiz_logic = """
    // 2. Quiz Logic
    let currentQuizIndex = 0;
    const quizTitle = document.getElementById('quiz-q-title');
    const quizOptions = document.getElementById('quiz-options');
    const quizExplanation = document.getElementById('quiz-explanation');
    const quizExplanationText = document.getElementById('quiz-explanation-text');
    const quizCounter = document.getElementById('quiz-counter');
    const prevQuizBtn = document.getElementById('prev-quiz');
    const nextQuizBtn = document.getElementById('next-quiz');

    function loadQuiz(index) {
        if (!quizData || quizData.length === 0 || !quizTitle) return;
        const qData = quizData[index];
        quizTitle.textContent = `Q${index + 1}: ${qData.q}`;
        quizCounter.textContent = `${index + 1} / ${quizData.length}`;
        quizExplanation.style.display = 'none';
        
        quizOptions.innerHTML = '';
        const answerLetter = qData.answer; // e.g., 'C'

        qData.options.forEach((optText) => {
            const btn = document.createElement('button');
            btn.className = 'quiz-option glass';
            btn.textContent = optText;
            
            btn.addEventListener('click', () => {
                // disable all options
                const allOpts = quizOptions.querySelectorAll('.quiz-option');
                allOpts.forEach(b => b.disabled = true);
                
                // check answer
                if (optText.startsWith(`(${answerLetter})`) || optText.startsWith(`${answerLetter})`)) {
                    btn.classList.add('correct');
                } else {
                    btn.classList.add('incorrect');
                    // highlight correct one
                    allOpts.forEach(b => {
                        if (b.textContent.startsWith(`(${answerLetter})`) || b.textContent.startsWith(`${answerLetter})`)) {
                            b.classList.add('correct');
                        }
                    });
                }
                
                quizExplanationText.innerHTML = qData.explanation;
                quizExplanation.style.display = 'block';
            });
            
            quizOptions.appendChild(btn);
        });
        
        prevQuizBtn.disabled = index === 0;
        nextQuizBtn.disabled = index === quizData.length - 1;
    }

    if (quizData && quizData.length > 0 && quizTitle) {
        loadQuiz(0);
    }

    if (prevQuizBtn && nextQuizBtn) {
        prevQuizBtn.addEventListener('click', () => {
            if (currentQuizIndex > 0) {
                currentQuizIndex--;
                loadQuiz(currentQuizIndex);
            }
        });

        nextQuizBtn.addEventListener('click', () => {
            if (currentQuizIndex < quizData.length - 1) {
                currentQuizIndex++;
                loadQuiz(currentQuizIndex);
            }
        });
    }
"""

if "function loadQuiz(index)" not in app_js:
    # Insert right before Cloze Logic
    target_str = "    // 3. Cloze Logic"
    if target_str in app_js:
        app_js = app_js.replace(target_str, quiz_logic + "\n" + target_str)
    else:
        # fallback, just insert before clozeContent
        target_str2 = "    const clozeContent = document.getElementById('cloze-content');"
        app_js = app_js.replace(target_str2, quiz_logic + "\n" + target_str2)

    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(app_js)
    print("Quiz logic added.")
else:
    print("Quiz logic already exists.")
