import re
sql_words = {
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
}


def replace_html_tags(text: str):
    return text.replace("<", "&lt;").replace(">", "&gt;")


def get_token_at(s: str, index: int):
    for match in re.finditer(r'\w+|[.,()]', s):
        start, end = match.start(), match.end()
        if start <= index < end:
            return match.group()
    return None


def sql_checker(line: str, index: int, input_char: str) -> bool:
    token = get_token_at(line, index)
    if not token or token.upper() not in sql_words:
        return False
    return line[index].lower() == input_char.lower()
