import socket

mySock = socket.socket()
host = socket.gethostname()
port = 65534
mySock.bind((host, port))
mySock.listen(1)

conn, addr = mySock.accept()
message = 'Thank you for connecting client '+ str(addr)
conn.send(message.encode())
conn.close()
mySock.close()
