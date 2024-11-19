from collections import defaultdict

class ConnectK:

    def __init__(self, k: int):
        """
        Initalizes the board
        """
        self.column_tracker = set()
        self.board = defaultdict(list)
        self.k = k

    def add_piece(self, player: str, column: int):
        """
        Adds a piece to the board
        """
        self.board[column].append(player)
        self.column_tracker.add(column)

        # checks vertical win
        if self.check_vertical_win(column, player):
            print("Player {} wins!".format(player))
            return player
        
        # checks horizontal win
        did_win, player = self.check_horizontal_win(column)
        if did_win:
            print("Player {} wins!".format(player))
            return player

    def check_vertical_win(self, column: int, player: str):
        """
        Checks if the player has won vertically
        """
        # Board not long enough
        if len(self.board[column]) < self.k:
            return False
        
        # Check if the last k pieces are the same
        for i in range(len(1, self.k+1)):
            if self.board[column][-i] != player:
                return False
            
        return True
    

    def check_horizontal_win(self, column: int, player: str):
        """
        Checks if the player has won horizontally
        """
        did_win_hold = False
        player_hold = False
        
        # iterate through the column
        for row_num in range(1,len(self.board[column])+1):
            
            # iterate through the length of the columns (number of horiz rows)
            x_tracker = 0
            o_tracker = 0
            last_piece = None
            for col in range(-self.k+1 + column, self.k + column):

                # check if the column is in the board
                if col in self.column_tracker:
                    
                    # checks to see if row number is greater than the length of the column
                    if row_num > len(self.board[col]):
                        x_tracker = 0
                        o_tracker = 0
                        last_piece = None
                        continue

                    # check if the piece is an X or O to adjust our tracker for "k" in a row
                    if self.board[col][-row_num] == "X":
                        if last_piece == "X":
                            x_tracker += 1
                        else:
                            x_tracker = 1
                            last_piece = "X"
                            o_tracker = 0
                    else:
                        if last_piece == "O":
                            o_tracker += 1
                        else:
                            o_tracker = 1
                            last_piece = "O"
                            x_tracker = 0

                    # check if the player has won
                    if x_tracker == self.k:
                        if player == "X":
                            return True, "X"
                        else:
                            did_win_hold = True
                            player_hold = "X"
                    elif o_tracker == self.k:
                        if player == "O":
                            return True, "O"
                        else:
                            did_win_hold = True
                            player_hold = "O"

                # if the column doesn't exist
                else:
                    x_tracker = 0
                    o_tracker = 0
                    last_piece = None
                
        
        return did_win_hold, player_hold

            
                
                
