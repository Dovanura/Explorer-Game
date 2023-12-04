import pygame
pygame.init()

import random
import time

WIDTH = 800
HEIGHT = 600

GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explorer Game")

FPS = 60

#color variables
GRASS = (0, 75, 25)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Player:
    PLAYER_HEIGHT, PLAYER_WIDTH = 20, 20
    PLAYER_COLOR = WHITE
    VEL = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def draw(self, win):
        pygame.draw.rect(win, self.PLAYER_COLOR, (self.x, self.y, self.PLAYER_WIDTH, self.PLAYER_HEIGHT))

    def move(self, up=False, down=False, right=False, left=False):
        if up:
            self.y -= self.VEL
        if down:
            self.y += self.VEL
        if right:
            self.x += self.VEL
        if left:
            self.x -= self.VEL


class Coin:
    COIN_COLOR = YELLOW
    COIN_HEIGHT, COIN_WIDTH = 10, 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, self.COIN_COLOR, (self.x, self.y, self.COIN_WIDTH, self.COIN_HEIGHT))

    def coin_location(self):
        pass


def draw(win, player, coin):
    win.fill(GRASS)
    player.draw(win)
    coin.draw(win)

    pygame.display.update()

def player_movement(keys, player):
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player.VEL >=0:
        player.move(up=True)
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player.height + player.VEL <=HEIGHT:
        player.move(down=True)
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player.width + player.VEL <=WIDTH:
        player.move(right=True)
    if (keys[pygame.K_a] or keys[pygame.K_LEFT] ) and player.x - player.VEL >=0:
        player.move(left=True)

def collision_handler():
    pass

def quit_game(run, keys):

    if keys[pygame.K_ESCAPE]:
        run = False

    return run

def main():
    #this is the main function for running the game loop.
    run = True
    clock = pygame.time.Clock()
    player = Player(WIDTH//2 + 10, HEIGHT - 30)
    

    while run:
        coin = Coin()
        clock.tick(FPS)
        draw(GAME_WINDOW, player, coin)

        keys = pygame.key.get_pressed()
        player_movement(keys, player)

        #collision_handler()
        coin.location()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if keys[pygame.K_ESCAPE]:
            run = False
            break
        
        #quit_game(run, keys)
        


    pygame.quit()


if __name__ == "__main__":
    main()