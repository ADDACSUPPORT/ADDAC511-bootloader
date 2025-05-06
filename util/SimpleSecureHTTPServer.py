#!/usr/bin/python

import http.server
from http.server import HTTPServer 
#from http.server import SimpleHTTPServer
import ssl
    
def run(args):
    httpd = HTTPServer((args.hostname, args.port), http.server.SimpleHTTPRequestHandler)
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(args.cert)
    httpd.socket = ssl_context.wrap_socket(
        httpd.socket,
        server_side=True,
    )
    print("Serving on https://{}:{}".format(args.hostname, args.port))
    httpd.serve_forever()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostname", default="localhost")
    parser.add_argument("--port", type=int, default=443)
    parser.add_argument("--cert", default="server.pem")

    args = parser.parse_args()
    
    run(args)


# # To generate a certificate use:
# # openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes