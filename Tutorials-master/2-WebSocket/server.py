import socket,time

server = socket.socket()
IP = 'localhost'
PORT = 65432

server.bind((IP,PORT))
server.listen(1)

client, client_address = server.accept()
print(client_address)
time.sleep(3)
print("waiting for sending...")
data=[1,2,3,4]
for i in data:
    i=str(i)
    print(i)
    sendForData=i.encode()
    client.send(sendForData)
    print(sendForData,"is sending")
server.close()