import self as self


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

class Pieces():
    def __init__(self, colour, piece, position):
        pieces = ['wP', 'wR', 'wN', 'wQ', 'wK', 'wB', 'bP', 'bR', 'bN', 'bQ', 'bK', 'bB']
        for piece in pieces:
            if piece[0] == "w":
                self.colour = "white"
            elif piece[0] == "b":
                self.colour = "black"

        for piece in pieces:
            if piece[1] == "P":
                self.piece = "pawn"
            elif piece[1] == "R":
                self.piece = "rook"
            elif piece[1] == "N":
                self.piece = "knight"
            elif piece[1] == "B":
                self.piece = "bishop"
            elif piece[1] == "Q":
                self.piece = "queen"
            elif piece[1] == "K":
                self.piece = "King"

class Pawn(self, x, y, color)
    def __init__(self, x, y, color):
    pawns = ['wP', 'bP']
    for pawn in pawns:
        if pawn[0] == "w":
            self.color = "white"
        elif pawn[1] == "b":
            self.color = "black"

    if self.color == "white":
        





#class Rook(x,y):
#class Bishop(x,y):
#class Knight(x,y):
#class Queen(x,y):
#class King(x,y):


#wP = Pawn(x, y)

class Move():

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = int(startSq[0])
        self.startCol = int(startSq[1])
        self.endRow = int(endSq[0])
        self.endCol = int(endSq[1])
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, a, b):
        return self.colsToFiles[b] + self.rowsToRanks[a]

p8 = Pawn()
