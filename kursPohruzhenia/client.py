import time
import socket


class ClientError(Exception):
    pass


class SocketError(ClientError):
    pass


class ProtocolError(ClientError):
    pass


class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = int(port)
        self.timeout = timeout
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise SocketError("failed to establish a connection", err)

    def __del__(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise SocketError("failed to close the socket", err)

    def put(self, key, value, timestamp=None):
        if timestamp == None:
            timestamp = str(int(time.time()))

        # form a request
        message = "put {} {} {}\n".format(key, value, timestamp)

        # send the request
        try:
            self.connection.sendall(message.encode())
        except socket.error as err:
            raise SocketError("failed to send a request", err)

        # obtain a feedback
        try:
            data = self.connection.recv(1024).decode()
        except socket.error as err:
            raise SocketError("failed to receive a feedback", err)

        # throw an exception if failed
        if data == "error\nwrong command\n\n":
            raise ProtocolError(data)

    def get(self, key):

       try:
           self.connection.sendall(
               f"get {key}\n".encode()
           )
       except socket.error as err:
           raise ClientError()

       data = b""

       while not data.endswith(b"\n\n"):
           try:
               data += self.connection.recv(1024)
           except socket.error as err:
               raise ClientError()

       decoded_data = data.decode()

       status, payload = decoded_data.split("\n", 1)
       payload = payload.strip()

       if status == "error":
           raise ClientError

       data = {}

       if payload == "" or payload == "''":
           return data

       for row in payload.split("\n"):
           try:
                key, value, timestamp = row.split()
                if key not in data:
                    data[key] = []
                data[key].append((int(timestamp), float(value)))
           except ValueError as err:
               raise ClientError
       return data
