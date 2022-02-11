class Game:
    def __init__(self, players, score = 0, speed = 10, direction = 'up'):
        self.speed = speed
        self.score = score
        self.direction = direction
        self.snake_list = [[players.x,players.y]]

    def grow_snake(self,food,players):
     if self.snake_list[0][0] == food.x and self.snake_list[0][1] == food.y:
         if self.direction == 'up':
             x_len = self.snake_list[-1][0]
             y_len = self.snake_list[-1][1] + players.size
         elif self.direction == 'down':
             x_len = self.snake_list[-1][0]
             y_len = self.snake_list[-1][1] - players.size
         elif self.direction == 'right':
             x_len = self.snake_list[-1][0] - players.size
             y_len = self.snake_list[-1][1]
         elif self.direction == 'left':
             x_len = self.snake_list[-1][0] + players.size
             y_len = self.snake_list[-1][1]
         self.snake_list.append([x_len,y_len])

    def move_snake(self,players):
     if self.direction == 'up':
         pos_x = self.snake_list[0][0]
         pos_y = self.snake_list[0][1] - players.size
     elif self.direction == 'down':
         pos_x = self.snake_list[0][0]
         pos_y = self.snake_list[0][1] + players.size
     elif self.direction == 'right':
         pos_x = self.snake_list[0][0] + players.size
         pos_y = self.snake_list[0][1]
     elif self.direction == 'left':
         pos_x = self.snake_list[0][0] - players.size
         pos_y = self.snake_list[0][1]
     self.snake_list.insert(0,[pos_x,pos_y])
     self.snake_list.pop()
     if [pos_x,pos_y] in self.snake_list[1:]:
         return True
     return False
