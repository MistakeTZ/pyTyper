let startTime = null;
let totalTypedChars = 0;
let wpmInterval = null;

function updateWPM() {
    if (!startTime) return;

    const elapsedMinutes = (Date.now() - startTime) / 60000; // в минутах
    const wordsTyped = totalTypedChars / 5;
    const wpm = Math.round(wordsTyped / elapsedMinutes);

    document.getElementById("wpmDisplay").textContent = `WPM: ${wpm}`;
}
