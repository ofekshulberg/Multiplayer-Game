class Game:
    def __init__(self, id):
        self.p1Went = False  # Indicates if player 1 has made a move
        self.p2Went = False  # Indicates if player 2 has made a move
        self.ready = False  # Indicates if both players are ready to play
        self.id = id  # Game ID
        self.moves = [None, None]  # Moves made by each player
        self.wins = [0,0]  # Number of wins for each player
        self.ties = 0  # Number of tie games

    def get_player_move(self, p):
        """
        Get the move made by a player.

        :param p: Player index (0 or 1)
        :return: Move made by the player
        """
        return self.moves[p]

    def play(self, player, move):
        """
        Record the move made by a player.

        :param player: Player index (0 or 1)
        :param move: Move made by the player
        """
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        """
        Check if both players are connected and ready to play.

        :return: True if both players are connected and ready, False otherwise
        """
        return self.ready

    def bothWent(self):
        """
        Check if both players have made a move.

        :return: True if both players have made a move, False otherwise
        """
        return self.p1Went and self.p2Went

    def winner(self):
        """
        Determine the winner of the game based on the moves made by the players.

        :return: Index of the winning player (0 or 1), or -1 for a tie game
        """
        p1 = self.moves[0].upper()[0]  # Get the first character of player 1's move
        p2 = self.moves[1].upper()[0]  # Get the first character of player 2's move

        winner = -1  # Default value for a tie game
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        """
        Reset the flags indicating if players have made a move.
        """
        self.p1Went = False
        self.p2Went = False
