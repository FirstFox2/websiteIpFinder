import socket

while 1:
    website = input("Please enter the URL:\n")
    if not website.__contains__(".") or website[len(website) - 1] == ".": continue
    try:
        print(socket.getaddrinfo(website, 0)[0][4][0])
    except:
        continue