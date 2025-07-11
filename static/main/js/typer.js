const inputField = document.getElementById("inputField");
const textContainer = document.getElementById("textContainer");
const restartBtn = document.getElementById("restartBtn");
const newTextBtn = document.getElementById("newTextBtn");

let text = ["Быстрая коричневая лиса перепрыгнула через ленивую собаку."];
let currentLine = 0;
let currentInput = "";

function newText() {
    fetch("http://127.0.0.1:8000/text", {
        method: "POST",
    })
    .then(response => response.json())
    .then(data => {
        text = data.text;
        renderText();
    })
    .catch(error => console.error(error));
}

function renderText() {
    textContainer.innerHTML = "";

    text.forEach((line, index) => {
        const lineDiv = document.createElement("div");
        lineDiv.classList.add("line");

        if (index === currentLine) {
            for (let i = 0; i < line.length; i++) {
            const span = document.createElement("span");
            span.textContent = line[i];
            if (i < currentInput.length) {
                span.className = currentInput[i] === line[i] ? "correct" : "incorrect";
            }
            if (i === currentInput.length) {
                span.classList.add("current");
            }
            lineDiv.appendChild(span);
            }
        } else {
            lineDiv.textContent = line;
        }

        textContainer.appendChild(lineDiv);
    });
}

inputField.addEventListener("input", () => {
    currentInput = inputField.value;
    renderText();
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
