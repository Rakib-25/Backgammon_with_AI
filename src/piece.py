
import os

class Piece:
    
    def __init__(self, name, color, value, texture = None, texture_rect = None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' or color == 'black'  else -1
        self.value = value * value_sign
        self.moves = []
        self.moded = False
        self.texture = texture
       
        self.set_texture()
     
        self.texture_rect = texture_rect
        
    def set_texture(self, size = 80):
        self.texture = os.path.join(
            f'assets/images/{self.color}_{self.name}.png'
        )
        
    def add_moves(self, move):
        self.moves.append(move)
    
    
        


class Guti(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('guti', color, 1.0)


class Dice(Piece):
    def __init__(self,color):
        super().__init__('dice',color, -1.0)
        