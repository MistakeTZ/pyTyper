import json
import subprocess
import threading
import uuid
import shutil

class TypeScriptLSP:
    def __init__(self):
        TSSERVER_PATH = shutil.which("typescript-language-server")
        if not TSSERVER_PATH:
            raise RuntimeError("typescript-language-server not found")

        self.proc = subprocess.Popen(
            [TSSERVER_PATH, '--stdio'],
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
            length = int([line for line in headers.decode().split('\r\n') if line.startswith("Content-Length")][0].split(":")[1])
            body = self.proc.stdout.read(length)
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
        return self._request("initialize", {
            "processId": None,
            "rootUri": None,
            "capabilities": {},
            "workspaceFolders": None
        })

    def shutdown(self):
        self._request("shutdown", None)
        self.proc.terminate()

    def get_completions(self, code, line, character):
        uri = f"file:///{uuid.uuid4().hex}.ts"
        self._send({
            "jsonrpc": "2.0",
            "method": "textDocument/didOpen",
            "params": {
                "textDocument": {
                    "uri": uri,
                    "languageId": "javascript",
                    "version": 1,
                    "text": code
                }
            }
        })
        return self._request("textDocument/completion", {
            "textDocument": {"uri": uri},
            "position": {"line": line, "character": character}
        })
