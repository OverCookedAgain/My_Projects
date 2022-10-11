import pygame
from pygame.locals import *

class Snake:

    def __init__(self):

        self.block_x = 100
        self.block_y = 100
        self.display()
        self.game_running()


    def display(self):

        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((110, 110, 5))
        self.block_img = pygame.image.load('./primary_block.jpg').convert()
        self.surface.blit(self.block_img, (self.block_x, self.block_y))
        pygame.display.flip()

    def movement(self):
        self.surface.blit(self.block_img, (self.block_x, self.block_y))
        pygame.display.flip()


    def game_running(self):

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                    if event.key == K_UP:
                        self.block_y -= 10
                        self.movement()
                    if event.key == K_DOWN:
                        self.block_y += 10
                        self.movement()

                    if event.key == K_LEFT:
                        self.block_x -= 10
                        self.movement()

                    if event.key == K_RIGHT:
                        self.block_x += 10
                        self.movement()



                elif event.type == QUIT:
                    self.running = False


if __name__ == '__main__':

    game1 = Snake()






