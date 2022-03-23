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
        self.objectBoard = [
            [bR1, bN1, bB1, "bQ", "bK", bB2, bN2, bR2],
            [bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            [wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8],
            [wR1, wN1, wB1, "wQ", "wK", wB2, wN2, wR2]]
        self.whiteToMove = True
        self.moveLog = []


    def doMove(self, move):
        r1 = move.startRow
        c1 = move.startCol
        r2 = move.endRow
        c2 = move.endCol
        selectedPiece = self.objectBoard[r1][c1]

        if self.board[r1][c1] != '--':  #checks if the piece selected is actually a piece
            if selectedPiece.validMove(r2, c2):
                self.board[r1][c1] = '--'    #makes the initial square clicked empty ie. the piece has moved off this square
                self.board[r2][c2] = move.pieceMoved  #puts the piece moved on the final/destination square
                self.objectBoard[r1][c1] = '--'
                self.objectBoard[r2][c2] = self.objectBoard[r1][c1]
                self.moveLog.append(move)   #adds the move to the moveLogS
                self.whiteToMove = not self.whiteToMove   #switches the turn to black


class Pawn:  #class which holds attributes of pawn and validation for pawn moves
    def __init__(self, x, y, colour):  #constructor
        self.row = y
        self.col = x
        self.colour = colour  #attributes

    def getX(self):  #getters/setters
        return self.col  #returns new x value

    def getY(self):
        return self.row  #returns the new y value

    def updateXY(self, x, y):
        self.x = x
        self.y = y

    def getColour(self):
        return self.colour

    def validMove(self, y, x): #validating pawn moves
        if self.colour == "white":  #if it is a white pawn
            if x == self.col and y-self.row == -1:  #check if remains in same column and moves up 1 (y-self.y as indexes from 0, so moving up board is a decrease)
                return True
            elif self.row == 6 and x == self.col and y-self.row == -2:  #check if it is in starting pos, so it can move 2
                return True
            elif objectBoard[y][x] != "--" and abs(self.col-x) == 1 and y-self.row == -1:  #check if there is a piece one up and one to the right of the pawn
                return True
            else:
                return False
        elif self.colour == "black":  #validation for black pawn, same process as white pawn but moving in diff direction on 2d array
            if x == self.col and y-self.row == 1:
                return True
            elif self.row == 1 and x == self.col and y-self.row == 2:
                return True
            elif objectBoard[y][x] != "--" and abs(self.col-x) == 1 and y-self.row == 1:
                return True
            else:
                return False


class Knight(Pawn):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)  #inherits these attributes/methods from the pawn class
        self.row = y
        self.col = x
        self.colour = colour #attributes

    def validMove(self, x, y):  #move validation method
            if abs(y-self.row) == 2 and abs(x-self.row) == 1 or abs(x-self.row) == 2 and abs(y-self.row) == 1:
                return True
            else:
                return False


class Bishop(Pawn):  #class for bishop inheriting from pawn
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)  #takes these attributes from parent class
        self.row = y
        self.col = x
        self.colour = colour


    def validMove(self, x, y):  #validation for bishop
        destination = self.objectBoard[self.endRow][self.endCol] #square to be moved to (final in the diagonal)
        if destination == "--":  #if it is empty square
            if abs(y-self.row) == abs(x-self.col):
                return True  #if change in y = change in x return true (means its moving diagonally)
            else:
                return False
        elif destination[0] != self.objectBoard[self.endRow][self.endCol][0]:
            return True
        else:
            return False



class Rook(Pawn):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.row = y
        self.col = x
        self.colour = colour

    def validMove(self, x, y):
        if self.col != x and self.row == y:
            return True
        elif self.row != y and self.col == x:
            return True
        else:
            return False




class Queen(Pawn):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.row = y
        self.col = x
        self.colour = colour

        if self.col != x and self.row == y or self.row != y and self.col == x or abs(y-self.row) == abs(x-self.col):
            return True
        else:
            return False


class King(Pawn):
    pass

# instantiating pieces
wP1 = Pawn(0, 6, "white")
wP2 = Pawn(1, 6, "white")
wP3 = Pawn(2, 6, "white")
wP4 = Pawn(3, 6, "white")
wP5 = Pawn(4, 6, "white")
wP6 = Pawn(5, 6, "white")
wP7 = Pawn(6, 6, "white")
wP8 = Pawn(7, 6, "white")
wP9 = Pawn(2, 2, "white")

bP1 = Pawn(0, 1, "black")
bP2 = Pawn(1, 1, "black")
bP3 = Pawn(2, 1, "black")
bP4 = Pawn(3, 1, "black")
bP5 = Pawn(4, 1, "black")
bP6 = Pawn(5, 1, "black")
bP7 = Pawn(6, 1, "black")
bP8 = Pawn(7, 1, "black")
bP9 = Pawn(3, 5, "black") #test pawn

wN1 = Knight(1, 7, "white")
wN2 = Knight(6, 7, "white")
bN1 = Knight(1, 0, "black")
bN2 = Knight(6, 0, "black")

wB1 = Bishop(2, 7, "white")
wB2 = Bishop(5, 7, "white")
bB1 = Bishop(2, 0, "black")
bB2 = Bishop(5, 0, "black")

wR1 = Rook(0, 7, "white")
wR2 = Rook(7, 7, "white")
bR1 = Rook(0, 0, "black")
bR2 = Rook(7, 0, "black")

objectBoard = [
            [bR1, bN1, bB1, "bQ", "bK", bB2, bN2, bR2],
            [bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            [wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8],
            [wR1, wN1, wB1, "wQ", "wK", wB2, wN2, wR2]]

class Move():

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, #dictionary
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}#maps out the index of the array to a chess notation style


    def __init__(self, startSq, endSq, board):
        self.startRow = int(startSq[0]) #finds the x coordinate of the piece selected (int needed as used to calculate as a float rather than integer
        self.startCol = int(startSq[1]) #finds the y coordinate of the piece selected
        self.endRow = int(endSq[0]) #finds x of destination square
        self.endCol = int(endSq[1]) #finds y of destination square
        self.pieceMoved = board[self.startRow][self.startCol] #finds the piece moved by applying the x,y coords to the board
        self.pieceCaptured = board[self.endRow][self.endCol] #finds the destination or piece captured by applying x,y coords to board



    def getRankFile(self, a, b):
        return self.colsToFiles[b] + self.rowsToRanks[a]



