const hintsBox = document.getElementById("hintsBox");
let hints = [];
let context = {};
let activeHintIndex = 0;

async function getHints() {
    // пример — можно заменить на fetch по API
    const word = currentInput.trim().split(" ").pop();
    if (!word) {
        hideHints();
        return;
    }

    hints = hints.filter(h => h.startsWith(word));

    if (hints.length > 0) {
        showHints();
    } else {
        hideHints();
    }

    await fetch('/api/hints', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "word": word, "inputs": inputs, "context": context })
    })
    .then(response => response.json())
    .then(data => {
        context = data.context;
        hints = data.hints.filter(h => h.startsWith(word));
        if (hints.length > 0) {
            activeHintIndex = 0;
            showHints();
        }
    })
    .catch(error => console.error(error));
}

function showHints() {
    hintsBox.innerHTML = "";

    hints.forEach((hint, i) => {
        const div = document.createElement("div");
        div.classList.add("hint");
        if (i === activeHintIndex) div.classList.add("active");
        div.textContent = hint;
        div.addEventListener("mousedown", () => selectHint(i));
        hintsBox.appendChild(div);
    });

    const currentSpan = document.querySelector(".current");
    if (currentSpan) {
        const rect = currentSpan.getBoundingClientRect();
        hintsBox.style.left = `${rect.left}px`;
        hintsBox.style.top = `${rect.bottom + window.scrollY + 5}px`;
        hintsBox.style.display = "block";
    }
}

function hideHints() {
    hintsBox.style.display = "none";
    hints = [];
    activeHintIndex = 0;
}

function selectHint(index) {
    const words = currentInput.split(" ");
    words[words.length - 1] = hints[index]; // заменяем последнее слово
    const newInput = words.join(" ");
    inputField.value = newInput;
    currentInput = newInput;
    inputs[currentLine] = currentInput;
    hideHints();
    renderText();
    inputField.focus();
}