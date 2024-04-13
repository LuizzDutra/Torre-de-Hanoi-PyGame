import pygame as pg

class Piece:
    HEIGHT = 15
    WIDTH = 30
    def __init__(self, size: int):
        self.size = size
        self.sprite = pg.Surface((self.WIDTH*self.size, self.HEIGHT))
        self.sprite.fill((255, 255, 255))


class Tower:
    def __init__(self, size: int, pos: tuple):
        self.pos = pos
        self.size = size
        self.spacing = Piece.WIDTH*(self.size + 1)
        self.poles = [[Piece(i) for i in range(size, 0, -1)], [], []]
        self.pole_sprite = pg.Surface((Piece.HEIGHT, Piece.HEIGHT*(self.size+1)))
        self.pole_sprite.fill((127, 127, 127))
    
    def change(self, n, m):
        if len(self.poles[n-1]) > 0 and ((len(self.poles[m-1]) == 0) or (self.poles[n-1][-1].size < self.poles[m-1][-1].size)):
            self.poles[m-1].append(self.poles[n-1].pop())

    def blit(self, screen: pg.Surface):

        for i in range(3):
            screen.blit(self.pole_sprite, (self.pos[0]+self.spacing*i-self.pole_sprite.get_width()/2, self.pos[1]-self.pole_sprite.get_height()+Piece.HEIGHT))

        for i, pole in enumerate(self.poles):
            for j, piece in enumerate(pole):
                 screen.blit(piece.sprite, (self.pos[0]+self.spacing*i-piece.sprite.get_width()/2, self.pos[1]-Piece.HEIGHT*j))
        
