import socket
import os.path
import datetime

server =('127.0.0.1',50007)
soc =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(server)

msg  ='AMNTSP amnts://127.0.0.1/test NADENADE\r\n'
msg +='Host: localhost:50007\r\n'
msg +='Count: 4\r\n'
msg +='\r\n'
msg +='なーでなで\r\n' # Body
soc.send(msg.encode('utf-8'))
data =soc.recv(4096).decode('utf-8')
print("Request")
print(msg)
print("Response")
print(str(data))
soc.close()
print("Client Stopped...")