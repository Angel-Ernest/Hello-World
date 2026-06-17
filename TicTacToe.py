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

        #print(turn)

G1 = Game(0, "X", [])

while True:
    CurrentPlayer = G1.getTurn()
    Position = int(input(f"{CurrentPlayer}'s turn: where do you want to play (select from 1 to 9)? "))

    if Position < 0 or Position > 9:
        print("You can't play there.")
        break

    AlreadyPlay = False
    
    for x in G1.position:
        L = x[-1]#Cut from the position; number indicates from where (-1 = last digit)
        #print(L)
        if L == Position:
            AlreadyPlay = True
            
    if AlreadyPlay == False:
        G1.makeMove(CurrentPlayer, Position)
        print(f"{G1.turn} : {Position}")
    else:
        print("Number already occupied, please try again.")