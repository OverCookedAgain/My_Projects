import pygame
from pygame.locals import *
import time

class Snake:

    def __init__(self, parent_screen):

        self.parent_screen = parent_screen
        self.x = 100
        self.y = 100
        self.block_img = pygame.image.load('./snake_icon.jpg').convert() #ikonka snake



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

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()


                elif event.type == QUIT:
                    self.running = False



if __name__ == '__main__':

    game1 = Game()
    game1.game_run()






