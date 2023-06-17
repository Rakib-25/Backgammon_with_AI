
from const import *
from square import Square
from piece import *

class Board:
    
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0] for col in range(COL)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')


    def _create(self):
        
        
        for row in range(ROW):
            for col in range (COL):
                self.squares[row][col] = Square(row, col)
    
    
    
    def _add_pieces(self,color):
        
        if True :
            c = [0,0,0,0,0,0,0,0]
            
         #this are all Guti's
            for row in range(ROW):
                for col in range(COL):
                    if color == 'white':
                        if col ==8:
                            if c[0]>4 :
                                continue
                            self.squares[row][col] = Square(row, col, Guti(color))
                            c[0]+=1
                        elif col == 4:
                            if c[1]>2:
                                continue
                            self.squares[row][col] = Square(row, col, Guti(color))
                            c[1]+=1
                        
                        elif col == 0 and row >=9:
                            self.squares[row][col] = Square(row, col, Guti(color))
                            
                        
                        elif col == 13 and row >=12:
                            self.squares[row][col] = Square(row, col, Guti(color))
                            
                            
                            
                    else:
                        if col ==0:
                            if c[2]>4 :
                                continue
                            self.squares[row][col] = Square(row, col, Guti(color))
                            c[2]+=1
                        elif col == 13:
                            if c[3]>1:
                                continue
                            self.squares[row][col] = Square(row, col, Guti(color))
                            c[3]+=1
                        
                        elif col == 8 and row >=9:
                            self.squares[row][col] = Square(row, col, Guti(color))
                            
                        
                        elif col == 4 and row >=11:
                            self.squares[row][col] = Square(row, col, Guti(color))
                        
                    
                    

