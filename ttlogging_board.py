from board import Board

class LoggingBoard(Board):
    # Initializes the board, then initializes an empty list for logging 
    def __init__(self):
        super().__init__()
        self.log = []  

    def claim_square(self, player, index):
        # Error will be raised if a inalid request is made 
        # Initializes the log to record player's index choice  
        super().claim_square(player, index)
        self.log.append(f"{player.name} selects square {index}")

    def get_winner(self):
        # Initializes log to record and announce when there is a winner 
        winner = super().get_winner()
        if winner:
            self.log.append(f"{winner.name} wins")
        return winner

    def game_over(self):
        # Prints playback of choices made by players, and winners score
        result = super().game_over()
        if result:
            for log_results in self.log:
                print(log_results)
        return result

