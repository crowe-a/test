import socket

server = socket.socket()
IP = 'localhost'
PORT = 65432

server.connect((IP,PORT))
print("Connection Successful")



array=[]
# print(message.decode())


i=0
while True:
    message = server.recv(1024)
    appd=message.decode()
    appd=int(appd)
    array.append(appd)
    if i==191:
        break
    i+=1
print(array)
# for i in message:


#     i=str(i)
#     array.append(i.decode())
# print(array)


server.close()