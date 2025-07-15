const inputField = document.getElementById("inputField");
const textContainer = document.getElementById("textContainer");
const restartBtn = document.getElementById("restartBtn");
const newTextBtn = document.getElementById("newTextBtn");

let text = ["If you see this - then something went wrong"];
let test_id = 0;
let programming_language = "python";

let currentInput = "";
let inputs = [];
let currentLine = 0;


function newText(test, lang) {
    fetch("/text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector("meta[name=csrf-token]").getAttribute("content"),
        },
        body: JSON.stringify({ "test_id": test, "lang": lang }),
    })
    .then(response => response.json())
    .then(data => {
        text = data.text;
        test_id = data.test_id;
        programming_language = data.programming_language;

        inputs = Array(text.length).fill(""); // сбрасываем ввод
        currentLine = 0;
        currentInput = "";
        inputField.value = "";
        renderText();
    })
    .catch(error => console.error(error));
}


function endTest() {
    fetch("/end", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector("meta[name=csrf-token]").getAttribute("content"),
        },
        body: JSON.stringify({
            "test_id": test_id,
            "inputs": inputs,
            "start_time": startTime,
            "end_time": Date.now()
        }),
    })
    .then(response => response.text())
    .then(html => {
        document.body.innerHTML = html;
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
        } else if (e.key === "Escape") {
            e.preventDefault();
            hideHints();
        }
    } else if (e.key === "Tab") {
        inputField.value += "    ";
        e.preventDefault();
        currentInput = inputField.value;
        inputs[currentLine] = currentInput;
        renderText();
        hideHints();
    } 
    if (e.key === " " && e.ctrlKey) {
        e.preventDefault();
        getHints(true);
        return;
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
            if (programming_language === "js") {
                inputField.value = inputField.value.slice(0, -1);
            } else {
                inputField.value = inputField.value.slice(0, -3);
            }
        } else if (inputField.value.endsWith(" " && programming_language === "js")) {
            inputField.value = inputField.value.slice(0, -1);
        }
    } else if (e.key === "Enter") {
        if (e.ctrlKey) {
            endTest();
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
        if (currentInput.trim().endsWith(":") && programming_language === "python") {
            tabs += 4;
        } else if (currentInput.trim().endsWith("{") && programming_language === "js") {
            tabs += 2;
        }
        currentLine++;
        currentInput = " ".repeat(tabs);
        inputField.value = currentInput;
        inputs[currentLine] = currentInput;

        if (currentLine >= text.length) {
            endTest();
            return;
        }

        hideHints();
        renderText();
        e.preventDefault();
    }
});

function restartTest(sameText=false) {
    startTime = null;
    totalTypedChars = 0;
    clearInterval(wpmInterval);
    document.getElementById("wpmDisplay").textContent = "Скорость: 0 WPM";
    let lang = document.getElementById("selected").textContent.toLowerCase();

    newText(sameText ? test_id : null, lang);
    renderText();
    inputField.focus();
}

restartBtn.addEventListener("click", () => restartTest(true));

newTextBtn.addEventListener("click", () => restartTest(false));

document.addEventListener("DOMContentLoaded", () => {
    let test = document.querySelector("meta[name=test-id]");
    newText(test.content, "python");
    inputField.focus();
});

// Auto-focus input field
document.addEventListener('click', (e) => {
    if (!['INPUT', 'BUTTON'].includes(e.target.tagName) && 
        !e.target.closest('#programmingLanguage') && 
        !e.target.closest('#hintsBox')) {
    document.getElementById('inputField').focus();
    }
});