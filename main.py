#!/usr/bin/python3.5
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading, argparse
from handler import MyHandler
from socketserver import ThreadingMixIn
import cv2
import streamer
ag = argparse.ArgumentParser()
ag.add_argument('-t', '--test', action='store_true')
args = ag.parse_args()
print(args)
if args.test:
    address = ('localhost', 9999)
else:
    address = ('10.0.0.117', 6789)

class MyServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    print('starting camera ...')
    print('starting server ...')

    httpd = MyServer(address, MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
bg_server= threading.Thread(target = run)
bg_server.start()
streamer.app.run(host='localhost', port=8888, threaded=True)
