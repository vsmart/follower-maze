import threading
import socket

host = '127.0.0.1'
port = 9090
data = "Hi server"

eventer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try: 
   
   eventer_socket.connect((host,port))
   eventer_socket.sendall(data + "\n")  

finally: 
   eventer_socket.close()

print "Sent: ", data
