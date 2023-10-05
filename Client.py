from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = ""

while True:
    userInput = int(input("Du kan vælge følgende kommandoer: "  + "\r\n"
                          "Tast 1 og angiv 2 numre som du vil have et tilfædigt tal ud af" + "\r\n"
                          "Tast 2 hvis du vil plusse 2 tal" + "\r\n"
                            "Tast 3 hvis du vil minusse 2 tal" + "\r\n"))
    num1 = input("Vælg tal 1: " )
    num2 = input("Vælg tal 2; " )
    
    if (userInput == 1):
        sentence = "Random" + ";" + num1 + ";" + num2
    elif (userInput == 2):
        sentence = "Add" + ";" + num1 + ";" + num2
    elif (userInput == 3):
        sentence = "Subtract" + ";" + num1 + ";" + num2

    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From server: ', modifiedSentence.decode())