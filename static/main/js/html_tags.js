const alwaysOpened = ["br", "hr", "img", "input", "link", "meta", "source",
    "track", "wbr", "area", "base", "basefont", "col", "colgroup", "command",
    "datalist", "embed", "keygen", "param"];
const mustClosed = ["html", "head", "body", "title", "div", "span", "p", "a",
    "ul", "ol", "li", "table", "tr", "td", "th", "form", "label", "script",
    "style", "select", "option", "section", "header", "footer", "article",
    "nav", "main", "aside", "h1", "h2", "h3", "h4", "h5", "h6", "address"];
const sqlWords = new Set([
  "ADD", "ALTER", "AND", "ANY", "AS", "ASC", "BACKUP", "BETWEEN", "CASE", "CHECK", "REPLACE", 
  "CREATE", "UNIQUE", "DELETE", "DESC", "DROP", "COLUMN", "CONSTRAINT", "DATABASE", "DEFAULT", 
  "VIEW", "EXEC", "EXISTS", "FOREIGN", "FROM", "FULL", "GROUP", "HAVING", "IN", "INDEX", 
  "INNER", "INSERT", "INTO", "IS", "LEFT", "LIKE", "LIMIT", "NOT", "NULL", "OR", "ORDER", 
  "BY", "OUTER", "PRIMARY", "KEY", "PROCEDURE", "RIGHT", "JOIN", "ROWNUM", "SELECT", 
  "DISTINCT", "TOP", "SET", "TRUNCATE", "TABLE", "UNION", "ALL", "UPDATE", "VALUES", 
  "CHAR", "VARCHAR", "BINARY", "VARBINARY", "TINYBLOB", "TINYTEXT", "BLOB", "TEXT", 
  "MEDIUMBLOB", "MEDIUMTEXT", "LONGBLOB", "LONGTEXT", "ENUM", "BIT", "TINYINT", "SMALLINT", 
  "MEDIUMINT", "INT", "BIGINT", "FLOAT", "DOUBLE", "DECIMAL", "DEC", "BOOLEAN", "BOOL", 
  "DATE", "TIME", "DATETIME", "TIMESTAMP", "YEAR", "INCREMENT", "AUTO_INCREMENT", "USE", 
  "CURRENT_TIMESTAMP", "CURRENT_TIME", "CURRENT_DATE", "CURRENT_USER", "CURRENT_ROLE", 
  "CURRENT_YEAR", "CURRENT_MONTH", "CURRENT_DAY", "CURRENT_HOUR", "CURRENT_MINUTE", 
  "CURRENT_SECOND", "REFERENCES"
]);

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
  if (!tokenInfo || !sqlWords.has(tokenInfo.value.toUpperCase())) return "incorrect";
  return line[index].toLowerCase() === inputChar.toLowerCase() ? "correct" : "incorrect";
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
