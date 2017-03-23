import socket
import threading
from Queue import Queue
import sys

class Server:
    def __init__(self, IP, PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((IP, PORT))
        self.queue = Queue(maxsize=0)

    def closeSocket(self):
        self.sock.close()

    def listenForPackets(self):
        def listen():
            while True:
                data, addr = self.sock.recvfrom(1024)
                self.queue.put(data)

        self.listen_UDP = threading.Thread(target=listen)
        self.listen_UDP.daemon = True
        self.listen_UDP.start()


