
import jedi
from .lsp_client import LSPClient

ts_lsp = LSPClient("ts", "typescript", "typescript-language-server")
ts_lsp.initialize()

html_lsp = LSPClient("html", "html", "vscode-html-language-server")
html_lsp.initialize()

cpp_lsp = LSPClient("cpp", "cpp", "clangd", "--enable-config")
cpp_lsp.initialize()


async def get_hints(data: dict):
    try:
        inputs = data.get("inputs", [])
        lang = data.get("lang")
        lines = [line for line in inputs if line]

        if not lines or not lang:
            return []

        current_line = lines[-1]
        full_code = '\n'.join(lines)

        if lang == "python":
            line_number = len(lines)
            column = len(current_line)
            script = jedi.Script(code=full_code)

            completions = script.complete(line=line_number, column=column)
            suggestions = [c.name for c in completions]
        else:
            line_number = len(lines) - 1
            column = len(lines[-1])
            if lang == "js":
                result = ts_lsp.completion(full_code, line_number, column)
            elif lang == "html":
                result = html_lsp.completion(full_code, line_number, column)
            elif lang == "cpp":
                result = cpp_lsp.completion(full_code, line_number, column)

            suggestions = []
            if result and 'items' in result:
                suggestions = [item['label'] for item in result['items']]

        return suggestions
    except Exception as e:
        print(e)
        return []
