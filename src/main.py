import pygame
import sys
from const import *
from game import Game
import random
import time



def show_dices( surface, row, col, random1 = 1 , random2 = 6):
        # Load the dice images
        dice_images = [
            pygame.image.load('assets/images/cpu_dice_1.png'),
            pygame.image.load('assets/images/cpu_dice_2.png'),
            pygame.image.load('assets/images/cpu_dice_3.png'),
            pygame.image.load('assets/images/cpu_dice_4.png'),
            pygame.image.load('assets/images/cpu_dice_5.png'),
            pygame.image.load('assets/images/cpu_dice_6.png')
        ]
        
        dice_value1 = random1
        dice_value2 = random2
        position_x = 6*PILLER_SIZE + PILLER_SIZE//2.5
        position_y = 6*ROW_SIZE + ROW_SIZE//2
        position_x1 = 7*PILLER_SIZE
        position_y1 = 6*ROW_SIZE + ROW_SIZE//2
        surface.blit(dice_images[dice_value1 - 1], (position_x, position_y))  
            
        surface.blit(dice_images[dice_value2 - 1], (position_x1, position_y1))
        '''is_dice_visible = False 
        
        running = True
        while running:
           
            
            img_rect = dice_images[dice_value1 - 1].get_rect()
            
            for event in pygame.event.get():
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('here2')
                    if event.button == 1:
                        print('here3')
                        mouse_pos = pygame.mouse.get_pos()
                        if row ==  7 or 8 and col == 6 or 7:
                            print('here4')
                            is_dice_visible = not is_dice_visible
                            
            
                        
            
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if is_dice_visible:'''
                


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
        
        
        running = True
        
        while running:
            
            self.game.show_bg(screen)
            game.show_pieces(screen)
            
            
            
            if dragger.dragging:
                dragger.Update_blit(screen)
                
                

            img = pygame.image.load("assets/images/dice_roll.png")
            img_rect = img.get_rect()
            position_x = 6*PILLER_SIZE
            position_y = 7*ROW_SIZE + ROW_SIZE//2
            screen.blit(img, (position_x, position_y))
            img_rect.center = (img_rect.width, img_rect.height)
            
            
            
            
            for event in pygame.event.get():
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // ROW_SIZE
                    clicked_col = dragger.mouseX // PILLER_SIZE 
                    print(clicked_col,clicked_row)
                    
                    
                    #if clicked square has a piece?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece #instead of typing large we can call with piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        
                    elif clicked_row ==  7 or 8 and clicked_col == 6 or 7:
                        
                        rand1 = random.randint(1, 6)
                        rand2 = random.randint(1, 6)
                        dice_images = [
                            pygame.image.load('assets/images/cpu_dice_1.png'),
                            pygame.image.load('assets/images/cpu_dice_2.png'),
                            pygame.image.load('assets/images/cpu_dice_3.png'),
                            pygame.image.load('assets/images/cpu_dice_4.png'),
                            pygame.image.load('assets/images/cpu_dice_5.png'),
                            pygame.image.load('assets/images/cpu_dice_6.png')
                        ]
                        
                        dice_value1 = rand1
                        dice_value2 = rand2
                        position_x = 6*PILLER_SIZE + PILLER_SIZE//2.5
                        position_y = 6*ROW_SIZE + ROW_SIZE//2
                        position_x1 = 7*PILLER_SIZE
                        position_y1 = 6*ROW_SIZE + ROW_SIZE//2
                        screen.blit(dice_images[dice_value1 - 1], (position_x, position_y)) 
                        screen.blit(dice_images[dice_value2 - 1], (position_x1, position_y1))
                                

                    
                                   
                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        game.show_button(screen)
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
