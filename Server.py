from socket import *
import threading
import random

def handle_client(connectionSocket, addr):
    print(addr[0])
    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode()
        splitedSentence = sentence.split(";")
        if len(splitedSentence) == 3 and splitedSentence[0].strip() == "Random":
            if(int(splitedSentence[1]) > int(splitedSentence[2])):
                 errorMessage = "Fejl: Det første tal kan ikke være større end det andet tal"
                 connectionSocket.send(str(errorMessage + "\r\n").encode())
            else:
                randomNumber = random.randint(int(splitedSentence[1]),int(splitedSentence[2]))
                responseClient = randomNumber
                connectionSocket.send((str(responseClient) + "\r\n").encode())
        elif len(splitedSentence) == 3 and splitedSentence[0].strip() == "Add":
                addNumber = int(splitedSentence[1]) + int(splitedSentence[2])
                responseClient = addNumber
                connectionSocket.send((str(responseClient) + "\r\n").encode())
        elif len(splitedSentence) == 3 and splitedSentence[0].strip() == "Subtract":
                subtractNumber = int(splitedSentence[1]) - int(splitedSentence[2])
                responseClient = subtractNumber
                connectionSocket.send((str(responseClient) + "\r\n").encode())
        else:
            connectionSocket.send(sentence.encode())
    connectionSocket.close()

serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()