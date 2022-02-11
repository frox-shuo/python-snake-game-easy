from color import Color
import pygame

class Player:
    def __init__(self, x, y, size = 10, color=Color.red):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.size,self.size))

class Food(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size = 10, color=Color.blue)
