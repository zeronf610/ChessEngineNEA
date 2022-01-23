import pygame as p
from Chess import ChessEngine

w = h = 512
dimension = 8
sqrSize = h/dimension
max_fps = 15
images = {}


def loadpieceimages():
    pieces = ['wP', 'wR', 'wN', 'wQ', 'wK', 'wB', 'bP', 'bR', 'bN', 'bQ', 'bK', 'bB']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("chess images/images/" + piece + ".png"), (sqrSize, sqrSize))


def main():
    p.init()
    screen = p.display.set_mode((w, h))
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    print(gs.board)
    loadpieceimages()
    running = True
    sqrSelected = ()
    clicks = []
    while running:
        for i in p.event.get():
            if i.type == p.QUIT:
                running = False
            elif i.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//sqrSize
                row = location[1]//sqrSize
                if sqrSelected == (row, col):
                    sqrSelected = ()
                    clicks = []
                else:
                    sqrSelected = (row, col)
                    clicks.append(sqrSelected)
                if len(clicks) == 2:
                    move = ChessEngine.Move(clicks[0], clicks[1], gs.board)
                    print(move.getNotation())
                    gs.doMove(move)
                    sqrSelected = ()
                    clicks = []
        drawgs(screen, gs)
        p.display.flip()


def drawgs(screen, gs):
    drawboard(screen)
    displaypieces(screen, gs.board)


def drawboard(screen):
    colours = [p.Color("white"), p.Color("light blue")]
    for x in range(dimension):
        for y in range(dimension):
            colour = colours[((x+y) % 2)]
            p.draw.rect(screen, colour, p.Rect(y*sqrSize, x*sqrSize, sqrSize, sqrSize))


def displaypieces(screen, board):
    for a in range(dimension):
        for b in range(dimension):
            piece = board[a][b]
            if piece != "--":
                screen.blit(images[piece], p.Rect(b*sqrSize, a*sqrSize, sqrSize, sqrSize))


if __name__ == "__main__":
    main()
