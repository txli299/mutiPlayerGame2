class Game:
    def __init__(self, id):       
        self.p1Went = [False,False,False,False,False]
        self.p2Went = [False,False,False,False,False]
        self.board = [" " for _ in range(9)]
        self.ready = False
        self.id = id
        self.exit = False
        self.move1 = set()
        self.move2 = set()
        self.p1Moves = set()
        self.p2Moves = set()
        self.round = 0
        self.current_player = "X"
        self.choices = ["agree", "agree"]


    def is_full(self):
        return all(cell != " " for cell in self.board)

    def get_first_player(self):
        return 0

    def get_board(self):
        return self.board

    def game_over(self):
        return self.winner() != -1


    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        if p == 0:
            return self.move1
        else:
            return self.move2

    def exit_game(self):
        self.exit = True

    def reset_game(self):
        return
    

    # def play(self, player, move):
    #         if player ==0:
    #             self.p1Went[self.round] = True
    #             self.move1.add(move)
    #         else:
    #             self.p2Went[self.round] = True        
    #             self.move2.add(move)
    #             self.round+=1

    def play(self, player, move):
        if player ==0:
            self.p1Went[self.round] = True
            self.move1.add(move)
        else:
            self.p2Went[self.round] = True        
            self.move2.add(move)
            self.round+=1

        position = int(move)-1
        if player == self.get_first_player():
            self.board[position] = "X"
            self.p1Moves.add(position)
            self.current_player = "O"
        else:
            self.board[position] = "O"
            self.p2Moves.add(position)
            self.current_player = "X"

    def check_valid_move(self, position):
        return self.board[position] == " "


    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went[self.round] and self.p2Went[self.round]

    def winner(self):
        winner = -1
        if "1"  in self.move1 and "2" in self.move1 and "3" in self.move1:
            winner = 1
        elif "4"  in self.move1 and "5" in self.move1 and "6" in self.move1:
            winner = 1
        elif "7"  in self.move1 and "8" in self.move1 and "9" in self.move1:
            winner = 1
        elif "1"  in self.move1 and "4" in self.move1 and "7" in self.move1:
            winner = 1
        elif "2"  in self.move1 and "5" in self.move1 and "8" in self.move1:
            winner = 1  
        elif "3"  in self.move1 and "6" in self.move1 and "9" in self.move1:
            winner = 1
        elif "1"  in self.move1 and "5" in self.move1 and "9" in self.move1:
            winner = 1
        elif "3"  in self.move1 and "5" in self.move1 and "7" in self.move1:
            winner = 1
        elif "1"  in self.move2 and "2" in self.move2 and "3" in self.move2:
            winner = 2
        elif "4"  in self.move2 and "5" in self.move2 and "6" in self.move2:
            winner = 2
        elif "7"  in self.move2 and "8" in self.move2 and "9" in self.move2:
            winner = 2
        elif "1"  in self.move2 and "4" in self.move2 and "7" in self.move2:
            winner = 2
        elif "2"  in self.move2 and "5" in self.move2 and "8" in self.move2:
            winner = 2 
        elif "3"  in self.move2 and "6" in self.move2 and "9" in self.move2:
            winner = 2
        elif "1"  in self.move2 and "5" in self.move2 and "9" in self.move2:
            winner = 2
        elif "3"  in self.move2 and "5" in self.move2 and "7" in self.move2:
            winner = 2
        elif self.round == 4 and self.p1Went[4]:
            winner = 0

        return winner

    def resetWent(self):
        for a in len(self.p1Went):
            self.p1Went[a] = False
        for b in len(self.p1Went):
            self.p1Went[b] = False
        self.round = 0









