import pygame
import sys
from const import *
from game import Game








class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('BACKGAMMON')
        self.game = Game()
        
        

    def mainloop(self):
        
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board
        
        while True:
            
            self.game.show_bg(screen)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.Update_blit(screen)
            
            for event in pygame.event.get():
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // ROW_SIZE
                    clicked_col = dragger.mouseX // PILLER_SIZE 
                    
                    
                    #if clicked square has a piece?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece #instead of typing large we can call with piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                                   
                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        dragger.Update_blit(screen)
                    
                    
                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                
                #for quitting the application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            


            pygame.display.update()




main = Main()
main.mainloop()
