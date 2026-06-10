class Game:
    #Class is like a collection of variables and methods(function/def)
    def __init__(self, score, turn, position):
        self.score = score
        self.turn = turn
        self.position = position

    def getTurn(self):
        return self.turn
        
        
        (self.turn+"'s turn, enter the position:")
    
    def makeMove(self, turn, position):
        #Check if position is occupied 1. Check if variable position is present in self.position
        self.position.append(f"{turn}:{position}")
        if turn == "X": # = means value, == means comparison value
            self.turn = "O"
        else:
            self.turn = "X"

        print(turn)

G1 = Game(0, "X", [])

while True:
    CurrentPlayer = G1.getTurn()
    Position = input(f"{CurrentPlayer}'s turn: where do you want to play (select from 1 to 9)? ")
    #Need to check the input (from 1 to 9) and can't play an existence playing
    G1.makeMove(CurrentPlayer, Position)

    print(G1.position)