import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "a" * 4096
sock.sendto(data.encode("ascii"), ("127.0.0.1", 5005))
