import socket

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

host = socket.gethostbyname()
port = 444

serversocket.bind((host,port))

serversocket.listen(3)

while True :
    clientsocket , adress = serversocket.accept()

    print("recieved connection from" % str(adress))

    message = "Hello thank you for connecting to the server" + "\r\n"
    clientsocket.send(message)

    clientsocket.close()
