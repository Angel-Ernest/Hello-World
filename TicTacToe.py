class Game:
    #Class is like a collection of variables and methods(function/def)
    def __init__(self, score, turn, position):
        self.score = score
        self.turn = turn
        self.position = position

    def getTurn(self):
        print(self.turn+"'s turn, enter the position:")
    
    def makeMove(self, turn, position):
        #Check if position is occupied 1. Check if variable position is present in self.position
        self.position.append(f"{turn}:{position}")

G1 = Game(0, "X", [])

G1.getTurn()



G1.makeMove("X", 1)
G1.makeMove("0", 4)
print(G1.position)

