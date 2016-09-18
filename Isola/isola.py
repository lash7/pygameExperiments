# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:19:53 2016

@author: abhilash.j2
"""
import numpy as np
import pygame 

# Params
N = 7
SIZE = (800,800)
MARGIN = SIZE[0]/10
POS = [SIZE[0]/4 , SIZE[0]/4]
TILE_SIZE = (np.min(SIZE)- 2*MARGIN)/N
TILE_SPACE = 0
red   = (255,0,0)
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
pygame.display.set_caption('ISOLA Game')
clock = pygame.time.Clock()
fps = 20


class GameBoard:
    """ 
    Initialize the game board with values
    """
    def __init__(self, n):
        self.n = n
        self.grid = np.zeros((n,n), dtype = int)
        
    """ 
    Function to move the current player to specified
    point on the grid
    """
    def movePlayer(self, player, x,y):
        self.grid[player.x][player.y] = 0
        player.setPosition(x,y)
        self.markPlayer(player)
    
    
    def removeTile(self, x, y):
        self.grid[x][y] = -1
    
    """
    Function returns if the player move is possible
    """
    def checkIfMoveIsPossible(x,y):
        return self.grid[x][y] == 0 and x < n and \
               y < n and x >= 0 and y >=0      
    
        
    """
    Set the position in the grid with the player id
    """
    
    def markPlayer(self, player):
        self.grid[player.x][player.y] = player.id
       
    

class Player:
    def __init__(self, id, x, y):
        self.x = x
        self.y = y
        self.id = id
    
    """
    Move the player's item to the specified x, y
    """
    def setPosition(self,x,y):
        self.x = x
        self.y = y



boardTiles = {}

"""
Function to generate tiles
"""
def drawGrid(board):
    global boardTiles
    for i in range(board.n):
        for j in range(board.n):
            xpos = MARGIN + j*(TILE_SIZE + TILE_SPACE)
            ypos = MARGIN + i*(TILE_SIZE + TILE_SPACE)
            gridValue = board.grid[i][j]             
            tileColor = COLOR[gridValue]
            boardTiles[(i,j)] = pygame.draw.rect(gameDisplay,tileColor, [xpos,ypos, TILE_SIZE, TILE_SIZE])
            pygame.draw.rect(gameDisplay,white, [xpos,ypos, TILE_SIZE, TILE_SIZE],2)
            
            if gridValue > 0:
                showText("P" + str(gridValue), white, (xpos + TILE_SIZE/2, ypos + TILE_SIZE/2 ))
            
            
            
font = pygame.font.SysFont(None,32)
def showText(text , color , xycenter):
    msg = font.render(text, True, color)
    msgRect = msg.get_rect()
    msgRect.center = xycenter  
    gameDisplay.blit(msg,msgRect)
    
def createGame():
    global board, player1, player2    
    board = GameBoard(7)
    player1 = Player(1,0,3)
    player2 = Player(2,6,3)    
    board.markPlayer(player1)
    board.markPlayer(player2)
    

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


while not hasGameExited:
    
    while inPlay:
        """ Event handling """    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False
                hasGameExited = True
            if event.type == pygame.mouse.get_pressed():
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                print(pos)
                ## check if cursor is on button ##
                x,y = getXYFromRectClicked(board, pos)
                print((x,y))
                board.removeTile(x,y)
                
                
                
        """ Game mechanics """
        
        
        
        """ Drawing to screen """
        gameDisplay.fill(white)
        drawGrid(board)
        showText("Player " + str(1 if player1Turn else 2) + "'s turn" ,black, (2*MARGIN, MARGIN/2))
        pygame.display.update()
        #clock.tick(fps)
        
#    while not inPlay and not GameExit:
#        showText("You Lose !", \
#                  white, (size[0]//2, size[1]//2))
#        showText("Press Q to Quit or C to continue",\
#                  black,(size[0]//3, size[1]//3))
#        pygame.display.update()
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                inPlay = True
#                GameExit = True
#            elif event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_q:
#                    inPlay = True
#                    GameExit = True
#                elif event.key == pygame.K_c:
#                    inPlay = True
#                    score = 0
#                    screen.fill(orange)
#                    pygame.display.update()
                    
pygame.quit()

quit()
