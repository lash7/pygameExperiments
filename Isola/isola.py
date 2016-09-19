# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:19:53 2016

@author: abhilash.j2
"""
import numpy as np
import pygame 
from GameClasses import GameBoard, Player

# Params
N = 7
SIZE = (800,800)
MARGIN = SIZE[0]/10
POS = [SIZE[0]/4 , SIZE[0]/4]
TILE_SIZE = (np.min(SIZE)- 2*MARGIN)/N
TILE_SPACE = 0
red   = (170,0,0)
green = (0, 170, 0)
black = (0, 0 , 0)
yellow = (245,245, 20)
orange = (240,110, 20)
white  = (255,255,255)
COLOR = {
    -1: white,
    0: orange,
    1:green,
    2:green
}


pygame.init()
gameDisplay = pygame.display.set_mode(SIZE)
pygame.display.set_caption('ISOLA Game - by Abhilash')
clock = pygame.time.Clock()
fps = 20


"""
Function to generate tiles
"""
def drawGrid(board, player,firstMove):
    global boardTiles
    x,y = player.x, player.y
    for i in range(board.n):
        for j in range(board.n):
            xpos = MARGIN + j*(TILE_SIZE + TILE_SPACE)
            ypos = MARGIN + i*(TILE_SIZE + TILE_SPACE)
            gridValue = board.grid[i][j]
            if firstMove and gridValue == 0 and \
                abs(i-x) <= 1 and abs(j-y) <= 1 :
                    tileColor = yellow
            else:
                tileColor = COLOR[gridValue]
            boardTiles[(i,j)] = pygame.draw.rect(gameDisplay,tileColor,\
                                        [xpos,ypos, TILE_SIZE, TILE_SIZE])
            pygame.draw.rect(gameDisplay,white, \
                                [xpos,ypos, TILE_SIZE, TILE_SIZE],2)
            
            if gridValue > 0:
                showText("P" + str(gridValue), white, \
                            (xpos + TILE_SIZE/2, ypos + TILE_SIZE/2 ))
            
            
            
font = pygame.font.SysFont(None,24)
def showText(text , color , xycenter):
    msg = font.render(text, True, color)
    msgRect = msg.get_rect()
    msgRect.center = xycenter  
    gameDisplay.blit(msg,msgRect)
    
def createGame():
    global board, player1, player2, player  , boardTiles, \
            hasGameExited, inPlay, player1Turn, firstMove
    board = GameBoard(N)
    player1 = Player(1,0,N//2)
    player2 = Player(2,N-1,N//2)    
    board.markPlayer(player1)
    board.markPlayer(player2)
    player = player1
    boardTiles = {}
    hasGameExited = False
    inPlay = True
    player1Turn = True
    firstMove = True




createGame()

def getXYFromRectClicked(board,pos):
    for i in range(board.n):
        for j in range(board.n):
            if boardTiles[(i,j)].collidepoint(pos):
                return (i,j)


""" 
Function to perform the game logic:
- If its the first turn of player
  --  move to a valid tile 
- If its the second turn
  -- remove a valid tile
"""
def performGameLogic():
    global board, player1Turn, firstMove, player
    
    if firstMove and player.isMoveValid(x,y):
        board.movePlayer(player,x,y)
        # Toggle the move after every possible move
        firstMove = not firstMove
    elif not firstMove:
        board.removeTile(x,y)
        # Toggle player if the move is the second one for current player
        player1Turn = not player1Turn
        firstMove = not firstMove
        player = player1 if player1Turn else player2
        

"""
Function to check if the game has ended
"""
def checkGameEnd(board, player):
    x, y = player.x, player.y
    n = board.n
    #  Checking for the normal cases            
    startX = 0 if x == 0   else x - 1
    endX   = n if x == n-1 else x + 2
    startY = 0 if y == 0   else y - 1
    endY   = n if y == n-1 else y + 2
    
    return not np.any(board.grid[startX : endX, startY:endY ] == 0)


def makeDisplayChanges():
    gameDisplay.fill(white)
    drawGrid(board, player, firstMove)
    if inPlay:
        showText("Player " + str(1 if player1Turn else 2) + "'s turn" ,\
                    red, (2*MARGIN, MARGIN/2))
        showText("Move to a Yellow Tile" if firstMove else "Remove any Orange Tile",\
                    red, (2*SIZE[0]/3, MARGIN/2))
    pygame.display.update()


while not hasGameExited:
    
    while inPlay:
        """ Event handling """    
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                inPlay = False
                hasGameExited = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ## if mouse is pressed get position of cursor ##
                pos = event.pos
                print(pos)
                ## check if cursor is on button ##
                coord = getXYFromRectClicked(board, pos)
                if coord != None:
                    x,y = coord           
                    print((x,y))
                    if board.checkIfMoveIsPossible(x,y):
                        performGameLogic()
                    
                if checkGameEnd(board, player):
                    inPlay = False
                
                
        """ Drawing to screen """
        makeDisplayChanges()
        #clock.tick(fps)
        
    while not inPlay and not hasGameExited:
        showText("Player " + str(player.id) + " Lost !!" ,\
                  black, (SIZE[0]/2, MARGIN/3))
        showText("Press Q to Quit or R to Restart",\
                  black,(SIZE[0]/2, 2*MARGIN/3))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = True
                hasGameExited = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    inPlay = True
                    hasGameExited = True
                elif event.key == pygame.K_r:
                    createGame()
                    makeDisplayChanges()
                    
pygame.quit()

quit()
