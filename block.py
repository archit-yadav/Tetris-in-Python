
# there are 7 types of blocks in tetris 
#1. define a class block having common properties of the blocks
#2. draw method will draw tetrominos in rotational states 
#3. moving the tetromino changing the rows and column with move function
#4. 

from colors import Colors
import pygame 
from position import *

class block:
    def __init__(self,id) :
        self.id = id #id is the is of the block 
        self.cells = {} # cells occupied in the block 
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
    
    def move(self,rows,columns): # to calculate the offset 
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):  # to return the modified position according to the offset 
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1
        

    def draw(self,screen,offset_x,offset_y):    
        tiles = self.get_cell_positions() # this line retrives current rotational state of the tetromino
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size , offset_y + tile.row* self.cell_size, self.cell_size - 1,self.cell_size - 1)
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)