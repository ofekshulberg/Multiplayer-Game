import socket
from _thread import *
import pickle
from game import Game

server = "192.168.0.93"  # Server IP address
port = 5555  # Server port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket

try:
    s.bind((server, port))  # Bind the socket to the server address and port
except socket.error as e:
    str(e)

s.listen(2)  # Listen for incoming connections (maximum 2 connections)
print("Waiting for a connection, Server Started")

connected = set()  # Set to store connected clients
games = {}  # Dictionary to store game instances
idCount = 0  # Counter for assigning game IDs


def threaded_client(conn, p, gameId):
    """
    Threaded function to handle communication with a client.

    :param conn: Connection socket
    :param p: Player number (0 or 1)
    :param gameId: Game ID
    """
    global idCount
    conn.send(str.encode(str(p)))  # Send the assigned player number to the client

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()  # Receive data from the client

            if gameId in games:  # Check if the game exists
                game = games[gameId]  # Get the game instance

                if not data:
                    break
                else:
                    if data == "reset":  # Handle reset request
                        game.resetWent()
                    elif data != "get":  # Handle player moves
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))  # Send the updated game state back to the client
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]  # Remove the game instance
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()  # Accept a new connection
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2  # Calculate the game ID based on the connection count
    if idCount % 2 == 1:  # Create a new game if it's the first player in the game
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:  # Assign the second player to the existing game
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))  # Start a new thread to handle the client's communication
