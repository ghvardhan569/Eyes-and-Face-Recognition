import socket

mySock = socket.socket()
host = socket.gethostname()
port = 65534
mySock.connect((host, port))
data = mySock.recv(1024)
print(data.decode())
mySock.close()
