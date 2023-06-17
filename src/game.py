import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()


    #show methods

    def show_bg(self, surface):
        for col in range(COL):
            if col == COL//2:
                color = (0,0,0) #Black
                
            elif col == (COL//2 -1):
                color = (0,0,0) #Black
                
            elif col%2 == 0:
                color = (234,235,200) #light green 
            else:
                color = (119, 154, 88) #dark green
            
            rect = (col * PILLER_SIZE, 0, PILLER_SIZE, HEIGHT)
            
            pygame.draw.rect(surface, color, rect)
        
        
        for row in range(ROW):
            if row == (ROW//2):
                color = (0,0,0)
            elif row == ((ROW//2)-1):
                color = (0,0,0)
            else:
                continue
            rect = ( 0, row * ROW_SIZE, WIDTH, ROW_SIZE)
            
            pygame.draw.rect(surface, color, rect)
            
    def show_pieces(self, surface):
        for row in range(ROW):
            for col in range (COL):
                #Piece?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                        img = pygame.image.load(piece.texture)
                        img_center = col * PILLER_SIZE + PILLER_SIZE//2 , row * ROW_SIZE + ROW_SIZE//2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)
            