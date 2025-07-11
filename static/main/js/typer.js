const inputField = document.getElementById("inputField");
const textContainer = document.getElementById("textContainer");
const restartBtn = document.getElementById("restartBtn");
const newTextBtn = document.getElementById("newTextBtn");

let text = ["Быстрая коричневая лиса", "перепрыгнула через ленивую собаку", "и скрылась в лесу."];
let currentInput = "";

let inputs = [];
let currentLine = 0;

function newText() {
    fetch("http://127.0.0.1:8000/text", {
        method: "POST",
    })
    .then(response => response.json())
    .then(data => {
        text = data.text;
        inputs = Array(text.length).fill(""); // сбрасываем ввод
        currentLine = 0;
        currentInput = "";
        inputField.value = "";
        renderText();
    })
    .catch(error => console.error(error));
}

function renderText() {
    textContainer.innerHTML = "";

    const start = Math.max(0, currentLine - 1);
    const end = Math.min(text.length, start === 0 ? 6 : currentLine + 5); // 1 до, текущая, 5 после

    for (let index = start; index < end; index++) {
        const lineDiv = document.createElement("div");
        lineDiv.classList.add("line");

        const line = text[index];
        const input = inputs[index] || "";

        if (index === currentLine || index === currentLine - 1) {
            for (let i = 0; i < Math.max(line.length, input.length + 1); i++) {
                const span = document.createElement("span");
                if (i < input.length) {
                    span.textContent = input[i];
                    if (input[i] !== line[i]) {
                        if (input[i] === " ") span.textContent = "_";
                        span.className = "incorrect";
                    } else {
                        span.className = "correct";
                    }
                } else {
                    span.textContent = line[i];
                }

                if (index === currentLine - 1 && i === input.length) {
                    span.className = "incorrect";
                }
                if (index === currentLine && i === input.length) {
                    span.classList.add("current");
                    span.textContent = line[i] && line[i].trim() ? line[i] : " ";
                }
                lineDiv.appendChild(span);
            }
        } else {
            lineDiv.textContent = line;
        }

        textContainer.appendChild(lineDiv);
    }
}

inputField.addEventListener("input", async (e) => {
    if (!startTime) {
        startTime = Date.now();
        wpmInterval = setInterval(updateWPM, 1000);
    }

    currentInput = inputField.value;
    inputs[currentLine] = currentInput;
    totalTypedChars = inputs.reduce((sum, line) => sum + line.length, 0);

    renderText();
    if (e.data !== " ") {
        await getHints();
    } else {
        hideHints();
    }
});

inputField.addEventListener("keydown", (e) => {
    if (hints.length > 0) {
        if (e.key === "Tab") {
            e.preventDefault();
            selectHint(activeHintIndex);
        } else if (e.key === "ArrowDown") {
            e.preventDefault();
            activeHintIndex = (activeHintIndex + 1) % hints.length;
            showHints();
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            activeHintIndex = (activeHintIndex - 1 + hints.length) % hints.length;
            showHints();
        }
    } else if (e.key === "Tab") {
        inputField.value += "    ";
        e.preventDefault();
        currentInput = inputField.value;
        inputs[currentLine] = currentInput;
        renderText();
        hideHints();
    }
    
    if (e.key === "Backspace") {
        if (inputField.value === "") {
            e.preventDefault();
            if (currentLine > 0) {
                currentLine--;
                inputField.value = inputs[currentLine] || "";
                currentInput = inputField.value;
                renderText();
            }
            return;
        } else if (inputField.value.endsWith("    ")) {
            inputField.value = inputField.value.slice(0, -3);
        }
    } else if (e.key === "Enter") {
        if (e.ctrlKey) {
            // TODO: end typing
            return;
        }
        let tabs = 0;
        for (let i = 0; i < currentInput.length; i++) {
            if (currentInput[i] === " ") {
                tabs++;
            } else {
                break;
            }
        }
        if (currentInput.trim().endsWith(":")) {
            tabs += 4;
        }
        currentLine++;
        currentInput = " ".repeat(tabs);
        inputField.value = currentInput;
        inputs[currentLine] = currentInput;

        if (currentLine >= text.length) {
            alert("Готово!");
            inputField.blur();
            return;
        }

        hideHints();
        renderText();
        e.preventDefault();
    }
});

restartBtn.addEventListener("click", () => {
    startTime = null;
    totalTypedChars = 0;
    clearInterval(wpmInterval);
    document.getElementById("wpmDisplay").textContent = "Скорость: 0 WPM";

    inputField.value = "";
    currentLine = 0;
    currentInput = "";
    renderText();
    inputField.focus();
});

newTextBtn.addEventListener("click", () => {
    newText();
    currentLine = 0;
    currentInput = "";
    inputField.focus();
});

document.addEventListener("DOMContentLoaded", () => {
    newText();
    inputField.focus();
});
