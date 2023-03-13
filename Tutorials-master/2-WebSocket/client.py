import socket,time

server = socket.socket()
IP = 'localhost'
PORT = 65432

server.connect((IP,PORT))
print("Connection Successful")
time.sleep(2)
message = server.recv(1024)
array=[]

i=0
while True:
    array.append(message.decode())
    print(message.decode(),":is getting")
    i+=1
    if i==4:
        print("this array getting: ",array)
        time.sleep(3)
        break
        
server.close()       