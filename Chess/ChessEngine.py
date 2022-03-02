class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []

    def doMove(self, move):
        if self.board[move.startRow][move.startCol] != '--': #checks if the piece selected is actually a piece
            self.board[move.startRow][move.startCol] = '--'   #makes the initial square clicked empty ie. the piece has moved off this square
            self.board[move.endRow][move.endCol] = move.pieceMoved   #puts the piece moved on the final/destination square
            self.moveLog.append(move)   #adds the move to the movelog
            self.whiteToMove = not self.whiteToMove   #switches the turn to black


# board = [
#         ["0,0", "1,0", "2,0", "3,0", "4,0", "5,0", "6,0", "7,0"],
#         ["0,1", "1,1", "2,1",

#class Pieces():
    #def __init__(self, colour, piece, position):
       # pieces = ['wP', 'wR', 'wN', 'wQ', 'wK', 'wB', 'bP', 'bR', 'bN', 'bQ', 'bK', 'bB']
        #for piece in pieces:
           # if piece[0] == "w":
              #  self.colour = "white"
           # elif piece[0] == "b":
               # self.colour = "black"

        #for piece in pieces:
           # if piece[1] == "P":
               # self.piece = "pawn"
            #elif piece[1] == "R":
               # self.piece = "rook"
           # elif piece[1] == "N":
            #    self.piece = "knight"
           # elif piece[1] == "B":
            #    self.piece = "bishop"
           # elif piece[1] == "Q":
           #     self.piece = "queen"
           # elif piece[1] == "K":
          #      self.piece = "King"
board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
class Pawn:
    def __init__(self, x, y, colour): #constructor
        self.row = y
        self.col = x
        self.colour = colour #attributes

    def validMove(self, x, y): #validating pawn moves
        if self.colour == "white": #if it is a white pawn
            if x == self.x and y-self.y == 1: #check if remains in same column and moves up 1 (y-self.y as indexes from 0, so moving up board is a decrease)
                return True
            elif self.y == 6 and x == self.x and y-self.y == 2: #check if it is in starting pos, so it can move 2
                return True
            elif board[self.y+1][self.x+1] != "--" and abs(self.x-x) == 1 and y-self.y == 1: #check if the
                return True
            else:
                return False
        elif self.colour == "black": #validation for black pawn
            pass










#class Rook(x,y):

#class Bishop(x,y):

#class Knight(x,y):

#class Queen(x,y):

#class King(x,y):

class Move():

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = int(startSq[0]) #finds the x coordinate of the piece selected (int needed as used to calculate as a float rather than integer
        self.startCol = int(startSq[1])
        self.endRow = int(endSq[0])
        self.endCol = int(endSq[1])
        self.pieceMoved = board[self.startRow][self.startCol] #finds the piece moved by applying the x,y coords to the board
        self.pieceCaptured = board[self.endRow][self.endCol] #finds the destination or piece captured by applying x,y coords to board

    def getNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, a, b):
        return self.colsToFiles[b] + self.rowsToRanks[a]

