from socket import *

sock = socket()
sock.bind(("0.0.0.0", 8000))
sock.listen(3)

c, addr = sock.accept()
print("Connect from..", addr)
data = c.recv(4096)
print(data.decode())

response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:text/html\r\n"
response += "\r\n"
response += "FK ALL !!!"

print(response)
c.send(response.encode())

c.close()
sock.close()
