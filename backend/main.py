from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api":

            dados = {
                "mensagem": "Olá! A API Python respondeu.",
                "linguagem": "Python"
            }
            resposta = json.dumps(dados).encode("utf-8")
            self.send_response(200)

            # Header responsável pelo CORS
            self.send_header("Access-Control-Allow-Origin", "http://localhost:5500")
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(resposta)))
            self.end_headers()
            self.wfile.write(resposta)


servidor = HTTPServer(
    ("localhost", 8000),
    APIHandler
)

print("API rodando em http://localhost:8000")
servidor.serve_forever()