# this class will contain different positions for each different state
from block import block
from position import Position

class LBlock(block): # L tetromino 
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {              #rotational states
            0:[Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(2,1),Position(2,2)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }
        self.move(0,3)

class JBlock(block): # J tetromino 
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {              #rotational states
            0:[Position(0,0),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(0,2),Position(1,1),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,2)],
            3:[Position(0,1),Position(1,1),Position(2,0),Position(2,1)]
        }
        self.move(0,3)

class IBlock(block): # I tetromino 
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {              #rotational states
            0:[Position(1,0),Position(1,1),Position(1,2),Position(1,3)],
            1:[Position(0,2),Position(1,2),Position(2,2),Position(3,2)],
            2:[Position(2,0),Position(2,1),Position(2,2),Position(2,3)],
            3:[Position(0,1),Position(1,1),Position(2,1),Position(3,1)]
        }
        self.move(-1,3)

class OBlock(block): # O tetromino 
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {              #rotational states
            0:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            # 1:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            # 2:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            # 3:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)]
        }
        self.move(0,4)

class SBlock(block): # S tetromino 
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {              #rotational states
            0:[Position(0,1),Position(0,2),Position(1,0),Position(1,1)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,2)],
            2:[Position(1,1),Position(1,2),Position(2,0),Position(2,1)],
            3:[Position(0,0),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3)

class TBlock(block): # T tetromino 
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {              #rotational states
            0:[Position(0,1),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,1)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3)

class ZBlock(block): # Z tetromino 
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {              #rotational states
            0:[Position(0,0),Position(0,1),Position(1,1),Position(1,2)],
            1:[Position(0,2),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(2,1),Position(2,2)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,0)]
        }
        self.move(0,3)

