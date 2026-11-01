import streamlit as st
import streamlit.components.v1 as components

# הגדרת העמוד לרוחב מלא
st.set_page_config(page_title="משחק ניחוש נקודות NBA", layout="wide")

# ה-HTML המלא כולל העיצוב וה-JavaScript
html_code = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>משחק ניחוש נקודות NBA</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts - Rubik -->
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            font-family: 'Rubik', sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
            min-height: 100vh;
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .glow-orange {
            box-shadow: 0 0 25px rgba(249, 115, 22, 0.35);
        }
    </style>
</head>
<body class="text-slate-100 flex flex-col justify-between min-h-screen p-4 sm:p-6">

    <div class="max-w-2xl mx-auto w-full space-y-6 my-auto">
        
        <!-- Header & Stats -->
        <header class="text-center space-y-2">
            <div class="inline-flex items-center justify-center p-3 bg-orange-500/20 text-orange-400 rounded-full mb-2">
                <i class="fa-solid fa-basketball fa-2x animate-bounce"></i>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-amber-200">
                משחק ניחוש נקודות NBA
            </h1>
            <p class="text-slate-400 text-sm sm:text-base">
                נסו לנחש את מודל הליניארי הלומד (גובה ומשקל) עד למספר השלם הקרוב ביותר!
            </p>
        </header>

        <!-- Scoreboard Bar -->
        <div class="grid grid-cols-3 gap-3 glass-card rounded-2xl p-4 text-center">
            <div class="border-l border-slate-700/50">
                <div class="text-slate-400 text-xs sm:text-sm font-medium">ניקוד מצטבר</div>
                <div id="score" class="text-2xl sm:text-3xl font-black text-amber-400">0</div>
            </div>
            <div class="border-l border-slate-700/50">
                <div class="text-slate-400 text-xs sm:text-sm font-medium">רצף ניצחונות</div>
                <div id="streak" class="text-2xl sm:text-3xl font-black text-orange-500">0 🔥</div>
            </div>
            <div>
                <div class="text-slate-400 text-xs sm:text-sm font-medium">סיבובים</div>
                <div id="rounds" class="text-2xl sm:text-3xl font-black text-indigo-400">0</div>
            </div>
        </div>

        <!-- Main Game Card -->
        <div class="glass-card glow-orange rounded-3xl p-6 sm:p-8 space-y-6">
            
            <!-- Target Player Stats -->
            <div class="bg-slate-900/60 rounded-2xl p-5 border border-slate-700/40 text-center space-y-4">
                <div class="flex justify-between items-center text-xs font-semibold uppercase tracking-wider text-slate-400">
                    <span>נתוני השחקן בסיבוב הזה</span>
                    <button id="randomize-btn" class="text-orange-400 hover:text-orange-300 transition-colors flex items-center gap-1">
                        <i class="fa-solid fa-shuffle"></i> שחקן אקראי חדש
                    </button>
                </div>

                <div class="grid grid-cols-2 gap-4 pt-1">
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                        <span class="block text-slate-400 text-xs mb-1">גובה (ס"מ)</span>
                        <div class="flex items-center justify-center gap-2">
                            <input type="number" id="height-input" class="w-full text-center bg-transparent text-2xl font-bold text-white focus:outline-none" value="198" min="150" max="230">
                        </div>
                    </div>
                    <div class="bg-slate-800/80 p-4 rounded-xl border border-slate-700">
                        <span class="block text-slate-400 text-xs mb-1">משקל (ק"ג)</span>
                        <div class="flex items-center justify-center gap-2">
                            <input type="number" id="weight-input" class="w-full text-center bg-transparent text-2xl font-bold text-white focus:outline-none" value="95" min="50" max="160">
                        </div>
                    </div>
                </div>
            </div>

            <!-- Guess Input Area -->
            <div class="space-y-4">
                <label for="guess-input" class="block text-center text-slate-300 font-medium">
                    כמה נקודות למשחק לדעתכם המודל יחזה לשחקן זה?
                </label>
                
                <div class="flex items-center gap-3">
                    <input type="number" id="guess-input" placeholder="הכנס את ניחושך (מספר שלם)" 
                        class="w-full px-5 py-4 bg-slate-900/90 border-2 border-slate-700 focus:border-orange-500 rounded-xl text-center text-xl font-bold text-white placeholder-slate-500 focus:outline-none transition-all">
                    
                    <button id="submit-btn" class="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-slate-950 font-black text-lg rounded-xl shadow-lg transition-all transform active:scale-95 flex items-center justify-center gap-2 whitespace-nowrap">
                        <i class="fa-solid fa-bullseye"></i> בדוק ניחוש
                    </button>
                </div>
            </div>

            <!-- Feedback Result Box -->
            <div id="result-box" class="hidden p-5 rounded-2xl text-center space-y-2 transition-all">
                <div id="result-title" class="text-xl font-extrabold"></div>
                <div id="result-details" class="text-sm sm:text-base text-slate-300"></div>
            </div>

        </div>

        <!-- Formula Info Collapsible / Footer info -->
        <div class="glass-card rounded-2xl p-4 text-xs text-slate-400 space-y-2">
            <div class="font-bold text-slate-300 flex items-center gap-2">
                <i class="fa-solid fa-calculator text-orange-400"></i> הפרמטרים של המודל לפי הקוד שלך:
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 font-mono text-[11px] dir-ltr text-left bg-slate-900/50 p-2.5 rounded-lg border border-slate-800">
                <div>w1 = -0.07072935</div>
                <div>w2 = 0.03051941</div>
                <div>b = 19.33773748</div>
            </div>
            <p class="text-center pt-1 text-slate-500">
                נוסחת החיזוי: <span class="font-mono text-slate-400">round(גובה × w1 + משקל × w2 + b)</span>
            </p>
        </div>

    </div>

    <script>
        const W1 = -0.07072934956142785;
        const W2 = 0.03051940672845106;
        const B = 19.337737482061055;

        let score = 0;
        let streak = 0;
        let rounds = 0;

        const heightInput = document.getElementById('height-input');
        const weightInput = document.getElementById('weight-input');
        const guessInput = document.getElementById('guess-input');
        const submitBtn = document.getElementById('submit-btn');
        const randomizeBtn = document.getElementById('randomize-btn');
        const resultBox = document.getElementById('result-box');
        const resultTitle = document.getElementById('result-title');
        const resultDetails = document.getElementById('result-details');
        
        const scoreEl = document.getElementById('score');
        const streakEl = document.getElementById('streak');
        const roundsEl = document.getElementById('rounds');

        function calculatePrediction(height, weight) {
            const rawPrediction = (height * W1) + (weight * W2) + B;
            return Math.round(rawPrediction);
        }

        function generateRandomPlayer() {
            const randomHeight = Math.floor(Math.random() * 41) + 180;
            const randomWeight = Math.floor(Math.random() * 56) + 75;

            heightInput.value = randomHeight;
            weightInput.value = randomWeight;
            guessInput.value = '';
            resultBox.classList.add('hidden');
        }

        function checkGuess() {
            const height = parseFloat(heightInput.value);
            const weight = parseFloat(weightInput.value);
            const userGuess = parseInt(guessInput.value, 10);

            if (isNaN(height) || isNaN(weight)) {
                alert('אנא הזן ערכי גובה ומשקל תקינים.');
                return;
            }

            if (isNaN(userGuess)) {
                alert('אנא הזן את ניחוש הנקודות שלך.');
                return;
            }

            const exactPrediction = calculatePrediction(height, weight);
            const diff = Math.abs(userGuess - exactPrediction);

            rounds++;
            resultBox.classList.remove('hidden');

            if (diff === 0) {
                score += 100;
                streak++;
                resultBox.className = "p-5 rounded-2xl text-center space-y-2 bg-emerald-500/20 border border-emerald-500/40 text-emerald-300";
                resultTitle.innerHTML = '<i class="fa-solid fa-trophy text-amber-400"></i> ניחוש מושלם! (100+ נקודות)';
                resultDetails.textContent = `התוצאה המדויקת של המודל היא בדיוק ${exactPrediction} נקודות.`;
            } else if (diff <= 2) {
                const pointsWon = Math.max(10, 50 - (diff * 15));
                score += pointsWon;
                streak++;
                resultBox.className = "p-5 rounded-2xl text-center space-y-2 bg-amber-500/20 border border-amber-500/40 text-amber-300";
                resultTitle.innerHTML = `<i class="fa-solid fa-fire"></i> קרוב מאוד! (+${pointsWon} נקודות)`;
                resultDetails.textContent = `נחשת ${userGuess}. התוצאה של המודל היא ${exactPrediction} (היית רחוק ב-${diff} בלבד).`;
            } else {
                streak = 0;
                resultBox.className = "p-5 rounded-2xl text-center space-y-2 bg-rose-500/20 border border-rose-500/40 text-rose-300";
                resultTitle.innerHTML = '<i class="fa-solid fa-xmark"></i> לא מדויק...';
                resultDetails.textContent = `נחשת ${userGuess}, אך תוצאת המודל השלמה היא ${exactPrediction}. (הפרש של ${diff}).`;
            }

            scoreEl.textContent = score;
            streakEl.textContent = `${streak} 🔥`;
            roundsEl.textContent = rounds;
        }

        submitBtn.addEventListener('click', checkGuess);
        randomizeBtn.addEventListener('click', generateRandomPlayer);
        
        guessInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                checkGuess();
            }
        });

        window.onload = generateRandomPlayer;
    </script>
</body>
</html>
"""

# הרצת ה-HTML בתוך ה-Streamlit
components.html(html_code, height=850, scrolling=True)
