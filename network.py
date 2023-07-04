import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket for the client
        self.server = "10.11.250.207"  # Server IP address
        self.port = 5555  # Server port
        self.addr = (self.server, self.port)  # Server address
        self.p = self.connect()  # Connect to the server and get the assigned player number

    def getP(self):
        """
        Get the assigned player number.

        :return: Assigned player number
        """
        return self.p

    def connect(self):
        """
        Connect to the server and receive the assigned player number.

        :return: Assigned player number
        """
        try:
            self.client.connect(self.addr)  # Connect to the server
            return self.client.recv(2048).decode()  # Receive the assigned player number from the server
        except:
            pass

    def send(self, data):
        """
        Send data to the server and receive a response.

        :param data: Data to send
        :return: Received data
        """
        try:
            self.client.send(str.encode(data))  # Send data to the server
            return pickle.loads(self.client.recv(2048*2))  # Receive and deserialize the response from the server
        except socket.error as e:
            print(e)
