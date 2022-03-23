import pygame as p
from Chess import ChessEngine

w = h = 400
xByY = 8
sqrSize = h/xByY
max_fps = 15
images = {}


def loadpieceimages():
    pieces = ['wP', 'wR', 'wN', 'wQ', 'wK', 'wB', 'bP', 'bR', 'bN', 'bQ', 'bK', 'bB'] #list of all pieces
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("chess images/images/" + piece + ".png"), (sqrSize, sqrSize))  #loops through for each piece in the list and searches for the file path with the name of index


def main():
    p.init()  #initialises pygame
    screen = p.display.set_mode((w, h))  #opens a screen with the dimensions described in the variables above
    screen.fill(p.Color("White"))  #makes the background white
    gs = ChessEngine.GameState()  #calls gamestate, where board is kept
    print(gs.board)   #prints the board
    loadpieceimages()  #loads the images of the pieces
    running = True  #while the program is running
    sqrSelected = ()  #sets variable sqrSelected to empty
    clicks = []  #holds in tuple format - [(6, 0) (7, 0)]
    while running:
        for i in p.event.get():  #gets the event
            if i.type == p.QUIT:  #if user quits, stop running
                running = False
            elif i.type == p.MOUSEBUTTONDOWN:  #if the mouse button is clicked
                location = p.mouse.get_pos()  #gets position of mouse and stores it in variable
                col = (location[0])//sqrSize  #finds the column of the square by dividing first item in location by the size of square
                row = (location[1])//sqrSize  #same as above for row
                if sqrSelected == (row, col):  #if the same square is selected, empty the contents of both variables - allow a user to choose a new move
                    sqrSelected = ()
                    clicks = ()
                else:
                    sqrSelected = (row, col)
                    clicks.append(sqrSelected)  #adds the row, col coords to clicks
                if len(clicks) == 2:  #if 2 clicks have been made
                    move = ChessEngine.Move(clicks[0], clicks[1], gs.board)  #passes the
                    gs.doMove(move)  #executes move, then empties variables again
                    sqrSelected = ()
                    clicks = []
        drawgs(screen, gs)
        p.display.flip()


def drawgs(screen, gs):
    drawboard(screen)
    displaypieces(screen, gs.board)


def drawboard(screen):  #draws the board with the colours white and light blue
    colours = [p.Color("white"), p.Color("light blue")]
    for x in range(xByY):
        for y in range(xByY):
            colour = colours[((x+y) % 2)]  #performs modulus of x+y so alternating equal size squares are made (checkerboard pattern)
            p.draw.rect(screen, colour, p.Rect(y*sqrSize, x*sqrSize, sqrSize, sqrSize))


def displaypieces(screen, board):
    for a in range(xByY):
        for b in range(xByY):
            piece = board[a][b]
            if piece != "--":
                screen.blit(images[piece], p.Rect(b*sqrSize, a*sqrSize, sqrSize, sqrSize))  #draws the pieces according to the parameters, making sure it fits in square


if __name__ == "__main__":
    main() #
