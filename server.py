import os
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes(socket.gethostname(), 'utf-8'))


def main():
    port = int(os.environ.get('PORT', 8000))

    print('Listening on {}.'.format(port))
    httpd = HTTPServer(('', port), Handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Exiting...')
        exit(0)


if __name__ == '__main__':
    main()
