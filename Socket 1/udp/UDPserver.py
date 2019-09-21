#Manuel Herrera
#Lab 1 UDPserver 

from socket import *
serverport = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while Ture:
    message, clientAddress = serverSocket .recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)