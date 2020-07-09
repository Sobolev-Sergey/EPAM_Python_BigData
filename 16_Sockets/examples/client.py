import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("188.120.248.147", 9999))

data = input(">")
sock.send(data.encode("utf-8"))
resp = sock.recv(1024)
print(resp.decode("utf-8"))

sock.close()
