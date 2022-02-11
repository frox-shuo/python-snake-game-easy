from color import Color
import pygame
import random

class Screen:

    def __init__(self,screen_width=600,screen_height=600,background_color=Color.background_color,font_type="monospace",font_size=20,clock_tick=20):
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.background_color=background_color
        self.screen = pygame.display.set_mode([screen_width,screen_height])
        self.font=pygame.font.SysFont(font_type,font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick=clock_tick
        pygame.display.set_caption('Snake')

    def refresh_background(self):
        self.screen.fill(self.background_color)

    def draw_score(self, snake_list, color=Color.yellow):
        score = len(snake_list)-1
        text = "Score:" + str(score)
        label = self.font.render(text,1,color)
        self.screen.blit(label,(450,550))

    def draw_food(self,snake_list,food):
     if snake_list[0][0] == food.x and snake_list[0][1] == food.y:
         food.x = random.randint(1,(self.screen_width/10)-1)*10
         food.y = random.randint(1,(self.screen_height/10)-1)*10
     food.draw(self.screen)
     return food.x, food.y

    def draw_snake(self, snake_list, players):
        for snake in snake_list:
            pygame.draw.rect(self.screen, Color.red, (snake[0],snake[1],players.size,players.size))

    def update_screen(self,snake_list,food, players):
        self.refresh_background()
        self.draw_score(snake_list)
        self.draw_food(snake_list,food)
        self.draw_snake(snake_list,players)
        self.clock.tick(self.clock_tick)
        pygame.display.update()
