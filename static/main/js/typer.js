const inputField = document.getElementById("inputField");
const textContainer = document.getElementById("textContainer");
const restartBtn = document.getElementById("restartBtn");
const newTextBtn = document.getElementById("newTextBtn");

let text = ["Быстрая коричневая лиса", "перепрыгнула через ленивую собаку", "и скрылась в лесу."];
let inputs = [];
let currentLine = 0;
let currentInput = "";

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
            for (let i = 0; i < line.length; i++) {
                const span = document.createElement("span");
                span.textContent = line[i];
                if (i < input.length) {
                    span.className = input[i] === line[i] ? "correct" : "incorrect";
                }
                if (index === currentLine - 1 && i === input.length) {
                    span.className = "incorrect";
                }
                if (index === currentLine && i === input.length) {
                    span.classList.add("current");
                }
                lineDiv.appendChild(span);
            }
        } else {
            lineDiv.textContent = line;
        }

        textContainer.appendChild(lineDiv);
    }
}

inputField.addEventListener("input", () => {
    currentInput = inputField.value;
    inputs[currentLine] = currentInput;
    renderText();
});

inputField.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        currentLine++;
        currentInput = "";
        inputField.value = "";

        if (currentLine >= text.length) {
            alert("Готово!");
            inputField.blur();
            return;
        }

        renderText();
        e.preventDefault();
    }
});

restartBtn.addEventListener("click", () => {
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
