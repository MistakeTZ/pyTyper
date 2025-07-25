const hintsBox = document.getElementById("hintsBox");
let hints = [];
let context = {};
let activeHintIndex = 0;
let afterDot = null;
let splitted = null;

const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
const socket = new WebSocket(`${protocol}${window.location.host}/ws/hints/`);

socket.onopen = () => {
    console.log("WebSocket connected");
    socket.send(JSON.stringify({ query: "test" }));
};

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    if (afterDot !== null) {
        hints = data.hints.filter(h => h.toLowerCase().startsWith(afterDot.toLowerCase()));
    } else {
        hints = data.hints.filter(h => h.toLowerCase().startsWith(splitted.toLowerCase()));
    }

    if (hints.length > 0) {
        activeHintIndex = 0;
        showHints();
    }
};

socket.onerror = (error) => {
    console.error("WebSocket error:", error);
};

async function getHints(force=false) {
    // пример — можно заменить на fetch по API
    const word = currentInput.trim().split(" ").pop();
    splitted = word;
    afterDot = null;

    ["(", "[", ":", "=", "<", "#"].forEach(symbol => {
        if (splitted.includes(symbol)) {
            splitted = splitted.split(symbol)[splitted.split(symbol).length - 1];
        }
    })

    const dotCount = splitted.split(".").length - 1;
    if (dotCount) {
        afterDot = splitted.split(".")[dotCount];
        if (afterDot.length == 0) {
            hints = [];
            force = true;
        } else {
            hints = hints.filter(h => h.toLowerCase().startsWith(afterDot.toLowerCase()));
        }
    } else {
        if (splitted.length == 1 && !splitted.endsWith("\"") && !splitted.endsWith("'")) {
            hints = [];
            force = true;
        } else {
            hints = hints.filter(h => h.toLowerCase().startsWith(splitted.toLowerCase()));
        }
    }

    if (hints.length > 0) {
        showHints();
    } else {
        hideHints();
    }

    if (force) {
        socket.send(JSON.stringify({ "inputs": inputs, "lang": prolang }));
    }
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

    ["(", "=", ".", "<"].forEach(symbol => {
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