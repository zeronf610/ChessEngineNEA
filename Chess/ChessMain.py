import pygame as p
from Chess import ChessEngine

w = 400
h = 400  #makes both the width and height equal to 400 pixels
xByY = 8  #dimensions
sqrSize = h/xByY  #allocates the square size by dividing the pixels equally between 8 squares (chessboard is 8x8)
images = {}  #holds all the images


def loadpieceimages(): #function to load piece images
    pieces = ['wP', 'wR', 'wN', 'wQ', 'wK', 'wB', 'bP', 'bR', 'bN', 'bQ', 'bK', 'bB'] #list of all pieces
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("chess images/images/" + piece + ".png"), (sqrSize, sqrSize))
        # loops through for each piece in the list and searches for the file path with the name of index

def main():
    p.init()  #initialises pygame
    screen = p.display.set_mode((w, h))  #opens a screen with the dimensions described in the variables above
    screen.fill(p.Color("White"))  #makes the background white
    gs = ChessEngine.GameState()  #calls gamestate, where board is kept
    print(gs.board)   #prints the board
    loadpieceimages()  #loads the images of the pieces
    running = True  #while the program is running
    sqSelected = ()  #sets variable sqrSelected to empty
    clicks = []  #list which holds tuple values
    while running:
        for e in p.event.get():  #gets the event
            if e.type == p.QUIT:  #if user quits, stop running
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:  #if the mouse button is clicked
                location = p.mouse.get_pos()  #gets position of mouse and stores it in variable
                col = (location[0])//sqrSize  #finds the column of the square by dividing first item in location by the size of square
                row = (location[1])//sqrSize  #same as above for row
                if sqSelected == (row, col):  #if the same square is selected, empty the contents of both variables - allow a user to choose a new move
                    sqSelected = ()  #empties sqrSelected
                    clicks = ()  #empties clicks
                else:
                    sqSelected = (row, col)
                    clicks.append(sqSelected)  #adds the row, col coords to clicks
                if len(clicks) == 2:  #if 2 clicks have been made
                    move = ChessEngine.Move(clicks[0], clicks[1], gs.board)  #passes the
                    gs.doMove(move)  #executes move, then empties variables again
                    sqSelected = ()
                    clicks = []
        drawgs(screen, gs)
        p.display.flip()


def drawgs(screen, gs):  #draws the board and displays the piece
    createboard(screen)  #passes screen through drawboard function
    displaypieces(screen, gs.board)  #passes screen and gs.board through displayPieces function


def createboard(screen):  #draws the board with the colours white and light blue
    colours = [p.Color("white"), p.Color("light blue")]
    for x in range(xByY):  #iterates from 1 to 8 horizontally
        for y in range(xByY):  #iterates from 1 to 8 vertically
            colour = colours[((x+y) % 2)]  #performs modulus of x+y so alternating equal size squares are made (checkerboard pattern)
            p.draw.rect(screen, colour, p.Rect(y*sqrSize, x*sqrSize, sqrSize, sqrSize))  #uses pygame function to draw a rectangle, and enters dimensions


def displaypieces(screen, board):  #function for displaying pieces
    for a in range(xByY):  #iterates to 8
        for b in range(xByY):  #iterates to 8
            piece = board[a][b]  #piece is equal to the x, y on the board
            if piece != "--":  #if this x,y on the the board is not empty
                screen.blit(images[piece], p.Rect(b*sqrSize, a*sqrSize, sqrSize, sqrSize))  #draws the pieces according to the parameters, making sure it fits in square


if __name__ == "__main__":
    main() #
