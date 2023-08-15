# Tetris-in-Python
This is the desktop iteration of the popular 1980's game Tetris. 
Built on python using pygame package

It has 7 classes each of them having specific methods 

1. Main : has all the main game loop and functioning of the game. All the game screen window, refresh rate etc. are in this class. 
2. Grid : has the main 20x30 grid for playing the game. It is a 20x30 multi dimensional array having specific no. of id in each cell for performing tasks.
3. Colors : has all the colors define in Colors class used in all over the game.
4. Block : having all the common properties of a tetrimino like rotation,colors etc.
5. Blocks : having all the seven tetromino defined in this along with there positions in the corressponding cells.
6. Position : is a class which returns row and column of a particular cell.
7. Game : for better optimization of the code game class has been created. It has all the basic functionality of the game from movements of the tetromino the clear line and game over logic.

Source:- https://www.youtube.com/watch?v=nF_crEtmpBo&list=WL&index=23
