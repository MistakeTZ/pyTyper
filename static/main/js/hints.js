const hintsBox = document.getElementById("hintsBox");
let hints = [];
let context = {};
let activeHintIndex = 0;

async function getHints() {
    // пример — можно заменить на fetch по API
    const word = currentInput.trim().split(" ").pop();
    let splitted = word.split("(")[word.split("(").length - 1];
    splitted = splitted.split("=")[word.split("=").length - 1];
    if (!splitted && splitted === word) {
        hideHints();
        return;
    }
    let afterDot = null;
    const dotCount = splitted.split(".").length - 1;
    if (dotCount) {
        afterDot = splitted.split(".")[dotCount];
    }

    if (afterDot) {
        hints = hints.filter(h => h.startsWith(afterDot));
    } else {
        hints = hints.filter(h => h.startsWith(splitted));
    }

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
        body: JSON.stringify({ inputs })
    })
    .then(response => response.json())
    .then(data => {
        if (afterDot !== null) {
            hints = data.hints.filter(h => h.startsWith(afterDot));
        } else {
            hints = data.hints.filter(h => h.startsWith(splitted));
        }

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
    const word = words[words.length - 1];
    let lastIndex = -1;

    ["(", "=", "."].forEach(symbol => {
        if (word.includes(symbol)) {
            lastIndex = Math.max(lastIndex, word.lastIndexOf(symbol));
        }
    })

    words[words.length - 1] = word.substring(0, lastIndex + 1) + hints[index];

    const newInput = words.join(" ");
    inputField.value = newInput;
    currentInput = newInput;
    inputs[currentLine] = currentInput;
    hideHints();
    renderText();
    inputField.focus();
}