import json
import subprocess
import threading
import uuid
import shutil


class LSPClient:
    def __init__(self, ext, lang, command, parametres="--stdio"):
        self.ext = ext
        self.lang = lang

        self.server_path = shutil.which(command)
        # self.server_path = r"C:\Users\Admin\scoop\apps\llvm\20.1.8\bin\clangd.exe"
        if not self.server_path:
            raise RuntimeError(f"{command} not found")

        self.proc = subprocess.Popen(
            [self.server_path, parametres],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0
        )

        self.lock = threading.Lock()
        self.id_counter = 1

    def _send(self, payload):
        message = json.dumps(payload)
        content = f"Content-Length: {len(message)}\r\n\r\n{message}"
        with self.lock:
            self.proc.stdin.write(content.encode('utf-8'))
            self.proc.stdin.flush()

    def _read(self):
        with self.lock:
            headers = b''
            while b'\r\n\r\n' not in headers:
                headers += self.proc.stdout.read(1)

            header_text = headers.decode()
            length_line = next(line for line in header_text.split('\r\n') if line.startswith("Content-Length"))
            length = int(length_line.split(":")[1].strip())

            body = b''
            while len(body) < length:
                chunk = self.proc.stdout.read(length - len(body))
                if not chunk:
                    break
                body += chunk

            return json.loads(body)

    def _request(self, method, params):
        req_id = self.id_counter
        self.id_counter += 1
        payload = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params
        }
        self._send(payload)
        while True:
            response = self._read()
            if "id" in response and response["id"] == req_id:
                return response["result"]

    def initialize(self):
        result = self._request("initialize", {
            "processId": None,
            "rootUri": None,
            "capabilities": {},
            "workspaceFolders": None
        })
        self._send({
            "jsonrpc": "2.0",
            "method": "initialized",
            "params": {}
        })
        return result

    def completion(self, code: str, line: int, character: int):
        tmpfile = f"/tmp/{uuid.uuid4().hex}.{self.ext}"
        uri = f"file://{tmpfile}"

        self._send({
            "jsonrpc": "2.0",
            "method": "textDocument/didOpen",
            "params": {
                "textDocument": {
                    "uri": uri,
                    "languageId": self.lang,
                    "version": 1,
                    "text": code
                }
            }
        })

        return self._request("textDocument/completion", {
            "textDocument": {"uri": uri},
            "position": {"line": line, "character": character}
        })

    def shutdown(self):
        try:
            self._request("shutdown", None)
        finally:
            self.proc.terminate()

if __name__ == "__main__":
    code = "const x = Math."
    code = "<h"
    code = "#include <vector>\nint main() { std::vec"
    # lsp = LSPClient("ts", "typescript", "typescript-language-server")
    # lsp = LSPClient("html", "html", "vscode-html-language-server")
    lsp = LSPClient("cpp", "cpp", "clangd", "--enable-config")
    print("Initializing...")
    lsp.initialize()
    print("Requesting completions...")
    print(code, 0, len(code))
    result = lsp.completion(code, 0, len(code))
    print(result["items"])

    lsp.shutdown()
