from http.server import BaseHTTPRequestHandler, HTTPServer
from config import FILE_PATH

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Обработчик GET-запросов — возвращает содержимое HTML-файла
    """
    def do_GET(self):
     with open(FILE_PATH, "r", encoding="utf-8") as f:
         content = f.read()
     encoded = content.encode("utf-8")

     self.send_response(200)
     self.send_header("Content-type", "text/html")
     self.end_headers()
     self.wfile.write(encoded)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")