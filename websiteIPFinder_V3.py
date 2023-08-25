import socket

while 1:
    website = input("Please enter the URL:\n")
    if website.__contains__("https://"): website = website[8:]
    elif website.__contains__("http://"): website = website[7:]
    if website.__contains__("/"): website = website[:website.index("/")]
    if not website.__contains__(".") or website[len(website) - 1] == ".": continue
    try:
        print(socket.getaddrinfo(website, 0)[0][4][0])
    except:
        continue
