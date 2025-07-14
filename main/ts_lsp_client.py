import json
import subprocess
import threading
import uuid
import shutil

class TypeScriptLSP:
    def __init__(self):
        self.tsserver_path = shutil.which("typescript-language-server")
        if not self.tsserver_path:
            raise RuntimeError("typescript-language-server not found")

        self.proc = subprocess.Popen(
            [self.tsserver_path, '--stdio'],
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

            try:
                return json.loads(body)
            except json.JSONDecodeError:
                print("=== INVALID JSON ===")
                print(body.decode(errors="replace"))
                raise

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
        tmpfile = f"/tmp/{uuid.uuid4().hex}.ts"
        uri = f"file://{tmpfile}"

        self._send({
            "jsonrpc": "2.0",
            "method": "textDocument/didOpen",
            "params": {
                "textDocument": {
                    "uri": uri,
                    "languageId": "typescript",
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
    lsp = TypeScriptLSP()
    print("Initializing...")
    lsp.initialize()
    print("Requesting completions...")
    result = lsp.completion(code, 0, len(code))
    print(json.dumps(result, indent=2))
    lsp.shutdown()
