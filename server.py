#!/usr/bin/env python3
"""Static server with SPA fallback for the Penguin WebGL site."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import mimetypes
import sys

ROOT = Path(__file__).resolve().parent

mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("image/ktx2", ".ktx2")
mimetypes.add_type("application/octet-stream", ".drc")
mimetypes.add_type("audio/ogg", ".ogg")
mimetypes.add_type("image/aces", ".exr")
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("font/woff", ".woff")
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("application/json", ".json")


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".js": "application/javascript",
        ".mjs": "application/javascript",
        ".wasm": "application/wasm",
        ".ktx2": "image/ktx2",
        ".drc": "application/octet-stream",
        ".ogg": "audio/ogg",
        ".exr": "image/aces",
        ".woff2": "font/woff2",
        ".woff": "font/woff",
        ".json": "application/json",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        rel = path.lstrip("/")
        file_path = (ROOT / rel).resolve()
        try:
            file_path.relative_to(ROOT)
        except ValueError:
            self.send_error(403)
            return
        if file_path.is_file():
            return super().do_GET()
        if not rel.startswith("assets/"):
            self.path = "/index.html"
            return super().do_GET()
        return super().do_GET()

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5173
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Penguin site → http://127.0.0.1:{port}/")
    print("Hard-refresh (Cmd+Shift+R) if you were stuck on the loader.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
