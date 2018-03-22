import socket, re

def maximo(data):
    t = str(bytes(data).decode()).replace('[', '').replace(']', '').replace(' ', '')
    list = t.split(',')
    max = list[0]
    for a in list:
        a = int(a)
        max = int(max)
        if a > max:
            max = a
    return max

def start():
    start = "start"
    host = "158.69.192.239"
    port = 1337
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect((host, port))

    data = sk.recv(1024)
    print(str(bytes(data).decode()))
    sk.send(start.encode())
    data = sk.recv(1024)
    print(str(bytes(data).decode()))
    data = sk.recv(1024)

    t = 1
    while  t != "":
        max = maximo(data)
        print(max)
        sk.send(str(max).encode())
        data = sk.recv(1024)
        t = str(bytes(data).decode())
        result = re.search('EY', t)
        if result != None:
            print(t)
            exit()
start()
"""
FLAG
EY{G0774_G0_F457_M47H}
"""



