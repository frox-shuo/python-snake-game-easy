import pygame
import random
import sys
from color import Color
from screen import Screen
from players import Player,Food
from gamelogic import Game

def play_game(screen,players,game,food):
    game_over = False
    while not game_over:

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()

         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN and game.direction != 'up':
                 game.direction = 'down'
             elif event.key == pygame.K_UP and game.direction !='down':
                 game.direction = 'up'
             elif event.key == pygame.K_LEFT and game.direction != 'right':
                 game.direction = 'left'
             elif event.key == pygame.K_RIGHT and game.direction != 'right':
                 game.direction = 'right'

     if game.move_snake(players) or game.snake_list[0][0] > screen.screen_width or game.snake_list[0][0] < 0 or game.snake_list[0][1] > screen.screen_height or game.snake_list[0][1] < 0:
         game_over = True
         break

     game.grow_snake(food,players)
     screen.update_screen(game.snake_list,food,players)

if __name__ == "__main__":
    pygame.init()

    screen = Screen()
    players = Player(screen.screen_width/2, screen.screen_height/2)
    game = Game(players)
    food = Food(random.randint(1,screen.screen_width/10)*10,random.randint(1,screen.screen_height/10)*10)

    play_game(screen,players,game,food)
