from http.server import BaseHTTPRequestHandler, HTTPServer

BLOCKED_PATHS = ["/tomcatwar.jsp"]
BLOCKED_HEADERS = {
    "suffix": "%>//",
    "c1": "Runtime",
    "c2": "<%",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded"
}
BLOCKED_QUERY = "?pwd=j&cmd="

class FirewallHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.is_malicious():
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked by firewall rule")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Request allowed")

    def do_POST(self):
        if self.is_malicious():
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked by firewall rule")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Request allowed")

    def is_malicious(self):
        # Check path
        if self.path in BLOCKED_PATHS:
            return True
        # Check query string
        if BLOCKED_QUERY in self.path:
            return True
        # Check headers
        for key, value in BLOCKED_HEADERS.items():
            if self.headers.get(key) == value:
                return True
        return False

def run(server_class=HTTPServer, handler_class=FirewallHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Firewall server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
