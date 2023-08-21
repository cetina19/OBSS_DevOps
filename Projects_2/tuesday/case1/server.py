from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import time

hostName = "localhost"
serverPort = 3000
method = "GET"
page_path = "/"

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.requestline.split(' ')[0] == 'GET':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            content = open('index.html', 'rb').read()
            if self.path == "/":
                content = open('index.html', 'rb').read()
            elif self.path == "/next/":
                content = open('next.html', 'rb').read()
            self.wfile.write(content)
        
        else:
            self.send_response(404)
        return
    def do_POST(self):
        if self.requestline.split(' ')[0] == 'POST':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            content = open('next.html', 'rb').read()
            if self.path == "/":
                content = open('index.html', 'rb').read()
                page_path = "/next/"
            elif self.path == "/next/":
                content = open('next.html', 'rb').read()
                page_path = "/"
            #print(self.path)
            self.wfile.write(content)
    

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Welcome\nServer started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")