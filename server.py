from http.server import BaseHTTPRequestHandler, HTTPServer
import os
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = f"{os.environ['NAME']}"
        self.wfile.write(bytes(message, "utf8"))
with HTTPServer(('', int(os.environ['PORT'])), handler) as server:
    server.serve_forever()