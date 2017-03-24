#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SimpleHTTPServer
import SocketServer
import sys
import re
import urllib

PORT = 8081

class MyHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    log_file = open('logfile.txt', 'w')
    def log_message(self, format, *args):
	for arg in args:
	  regex = re.compile(r"id=(.*)&end")
	  if regex.search(str(arg)):
	    match = regex.search(str(arg))
	    #print urllib.unquote(match.group(1)).decode('utf8') 
            self.log_file.write("%s\n" % (urllib.unquote(match.group(1)).decode('utf8')))
	    self.log_file.flush()
try:
  Handler = MyHTTPHandler

  httpd = SocketServer.TCPServer(("", PORT), Handler)

  print "Start scanning the id parameter at: http://127.0.0.1:" + str(PORT) + "/?id=§§&end"

  httpd.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    httpd.socket.close()
