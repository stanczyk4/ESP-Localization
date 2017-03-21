import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5007

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

#while True:
message = "12:34:56:78:9A,05:34:23:12:32,-61"
sock.sendto(message, (UDP_IP,UDP_PORT))

message = "12:34:56:78:9A,34:23:34:45:43,-61"
sock.sendto(message, (UDP_IP,UDP_PORT))

message = "12:34:56:78:9A,43:23:45:23:56,-61"
sock.sendto(message, (UDP_IP,UDP_PORT))

message = "12:34:56:78:9A,34:23:45:34:32,-61"
sock.sendto(message, (UDP_IP,UDP_PORT))


sock.close()


