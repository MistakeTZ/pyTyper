
import jedi
from .ts_lsp_client import TypeScriptLSP

lsp = TypeScriptLSP()
lsp.initialize()


async def get_hints(data: dict):
    try:
        inputs = data.get("inputs", [])
        lang = data.get("lang", "python")
        lines = [line for line in inputs if line]

        if not lines:
            return []

        current_line = lines[-1]
        full_code = '\n'.join(lines)

        if lang == "python":
            line_number = len(lines)
            column = len(current_line)
            script = jedi.Script(code=full_code)

            completions = script.complete(line=line_number, column=column)
            suggestions = [c.name for c in completions]
        elif lang == "js":
            line_number = len(lines) - 1
            column = len(lines[-1])
            result = lsp.completion(full_code, line_number, column)

            suggestions = []
            if result and 'items' in result:
                suggestions = [item['label'] for item in result['items']]

        return suggestions
    except Exception as e:
        print(e)
        return []
