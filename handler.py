#!/usr/bin/python3.5
from http.server import BaseHTTPRequestHandler, HTTPServer
import cv2, time, imutils, requests

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as f:
                self.wfile.write(f.read().encode())

        elif self.path.strip('/') == 'stream':
            self.send_response(301)
            self.send_header('Location', 'http://localhost:8888')
            self.end_headers()
        else:
            self.send_response(404)

    def do_OPTIONS(self):
        methods = ['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']
        sup_methods = []
        self.send_response(200)
        for m in methods:
            if hasattr(self, 'do_' + m):
                sup_methods.append(m)
            else:
                pass
        print(sup_methods)
        meth = ', '.join(sup_methods)
        self.send_header('Allow', meth)

