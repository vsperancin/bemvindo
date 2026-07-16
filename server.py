"""Bem-vindo Vinicius! — VinIA Cinema

Servidor HTTP minimo usando stdlib (sem Flask/FastAPI) pra ficar
bem pequeno no Docker (imagem final ~25MB com python:3.13-alpine).
"""
from __future__ import annotations
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"

CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
    ".json": "application/json; charset=utf-8",
}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, content_type: str, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "public, max-age=300")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = self.path.split("?")[0]
        # Servir index.html na raiz
        if path == "/" or path == "":
            body = (TEMPLATES / "index.html").read_bytes()
            return self._send(200, CONTENT_TYPES[".html"], body)
        # Servir /static/<arquivo>
        if path.startswith("/static/"):
            rel = path.lstrip("/")
            target = ROOT / rel
            if not target.is_file():
                return self._send(404, "text/plain", b"Not found")
            ext = target.suffix.lower()
            ct = CONTENT_TYPES.get(ext, "application/octet-stream")
            return self._send(200, ct, target.read_bytes())
        # Health
        if path == "/health":
            return self._send(200, "application/json", b'{"status":"ok"}')
        return self._send(404, "text/plain", b"Not found")

    def log_message(self, fmt: str, *args: object) -> None:
        # log compacto pra stdout do container
        print(f"[{self.log_date_time_string()}] {self.address_string()} - {fmt % args}", flush=True)


def main() -> None:
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    print(f"VinIA Cinema listening on http://{host}:{port}", flush=True)
    HTTPServer((host, port), Handler).serve_forever()


if __name__ == "__main__":
    main()