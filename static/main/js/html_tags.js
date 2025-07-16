const alwaysOpened = ["br", "hr", "img", "input", "link", "meta", "source",
    "track", "wbr", "area", "base", "basefont", "col", "colgroup", "command",
    "datalist", "embed", "keygen", "param"];
const mustClosed = ["html", "head", "body", "title", "div", "span", "p", "a",
    "ul", "ol", "li", "table", "tr", "td", "th", "form", "label", "script",
    "style", "select", "option", "section", "header", "footer", "article",
    "nav", "main", "aside", "h1", "h2", "h3", "h4", "h5", "h6", "address"];

let opened = 0;

function isOpened(line) {
    const matches = [...line.matchAll(/<([\/]?\w+)/g)].map(m => m[1]);
    
    let addOpened = 0;
    for (const tag of matches) {
        if (mustClosed.includes(tag)) {
            addOpened++;
        } else if (mustClosed.includes(tag.slice(1))) {
            addOpened--;
        }
    }
    
    return addOpened;
}

function sqlClassName(line, index, inputChar) {
  const tokenInfo = getTokenAt(line, index);

  if (tokenInfo !== null && tokenInfo.value.toUpperCase() === tokenInfo.value) {
    return line[index].toLowerCase() === inputChar.toLowerCase() ? "correct" : "incorrect";
  }
  return "incorrect";
}

function getTokenAt(str, index) {
  const re = /\w+|[.,()]/g;
  let match;

  while ((match = re.exec(str)) !== null) {
    const start = match.index;
    const end = start + match[0].length;
    if (index >= start && index < end) {
      return { value: match[0], start, end };
    }
  }

  return null;
}
