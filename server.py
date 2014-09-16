# import threading
import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler): 

   def handle(self):
      self.msg = self.request.recv(1024).strip()
      print "client <{}>: ".format(self.client_address[0])
      print self.msg


if __name__ == "__main__": 
   host, port = '127.0.0.1', 9090
   
   # Create server, bind to local host and port 
   server = SocketServer.TCPServer((host,port),TCPHandler)

   print "server is starting on ", host, port
 
   # start server
   server.serve_forever()
   
  
