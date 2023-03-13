import socket

# sunucu soketine bağlanın
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 12345
client_socket.connect((host, port))

# verileri alın ve onları ondalık sayı listesi olarak ayrıştırın
data1 = client_socket.recv(1024)
data = eval(data1.decode())

# alınan verileri yazdırın
print(data)

# soketi kapatın
client_socket.close()