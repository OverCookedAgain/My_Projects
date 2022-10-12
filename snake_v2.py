import random

import pygame
from pygame.locals import *
import random
import time

class Snake:

    def __init__(self, parent_screen):

        self.parent_screen = parent_screen
        self.x = 100
        self.y = 100
        self.block_img = pygame.image.load('./snake_icon.jpg').convert() #ikonka snake
        self.directory = random.choice(['up', 'down', 'left', 'right'])



    def draw(self):
        self.parent_screen.fill((110, 110, 5))  # wypelnienie tla, ustawiam kolory
        self.parent_screen.blit(self.block_img, (self.x, self.y))  # ustawiam gdzie ma być ikonka snake
        pygame.display.flip()  # jakby loop taki

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def walk(self):
        if self.directory == 'up':
            self.move_up()
        if self.directory == 'down':
            self.move_down()
        if self.directory == 'right':
            self.move_right()
        if self.directory == 'left':
            self.move_left()


class Game:

    def __init__(self):
        pygame.init()  # inicjalizuje pygame
        self.surface = pygame.display.set_mode((500, 500))  # definiuje pokazywany ekran
        self.surface.fill((110, 110, 5))  # wypelnienie tla, ustawiam kolory
        self.snake= Snake(self.surface)
        self.snake.draw()




    def game_run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                        self.snake.directory = 'up'

                    if event.key == K_DOWN:
                        self.snake.move_down()
                        self.snake.directory = 'down'

                    if event.key == K_LEFT:
                        self.snake.move_left()
                        self.snake.directory = 'left'

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        self.snake.directory = 'right'


                elif event.type == QUIT:
                    self.running = False

            self.snake.walk()
            time.sleep(0.2)



if __name__ == '__main__':

    game1 = Game()
    game1.game_run()






