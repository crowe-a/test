import socket
import json

# sunucu soketine bağlanın
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 12345
client_socket.connect((host, port))

# verileri alın ve onları ondalık sayı listesi olarak ayrıştırın
json_data = client_socket.recv(2048).decode()
data = json.loads(json_data)

# alınan verileri yazdırın
print(data)

# soketi kapatın
client_socket.close()