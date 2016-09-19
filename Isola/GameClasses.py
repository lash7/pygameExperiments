# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:48:47 2016

@author: Abhilash
"""

import numpy as np
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
    
    
    """
    Function to remove the tile in the second move of player
    """
    def removeTile(self, x, y):
        self.grid[x][y] = -1
    
    """
    Function returns if the player move is possible
    """
    def checkIfMoveIsPossible(self,x,y):
        return self.grid[x][y] == 0 and x < self.n and \
               y < self.n and x >= 0 and y >=0      
    
        
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
    
        """
    Return if the player can move to the spefied tile locations
    """
    def isMoveValid(self, x,y):
        return abs(self.x - x) <= 1 and \
            abs(self.y - y) <= 1 and \
            not (self.x == x and self.y == y)
