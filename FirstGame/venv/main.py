import pygame
pygame.init()

import random
import time

WIDTH = 800
HEIGHT = 600

GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explorer Game")

FPS = 60
COUNT_FONT = pygame.font.SysFont("comicsans", 50)

#color variables
GRASS = (0, 75, 25)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ENEMY_COLOR = (255, 0, 50)

class Player:
    def __init__(self, x, y, size=30, color=WHITE, velocity=5):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity = velocity
        #self.body = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        #pygame.draw.rect(win, self.PLAYER_COLOR, self.body)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def move(self, up=False, down=False, right=False, left=False):
        if up:
            self.y -= self.velocity
        if down:
            self.y += self.velocity
        if right:
            self.x += self.velocity
        if left:
            self.x -= self.velocity



class Coin:
    COIN_COLOR = YELLOW

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5

    def draw(self, win):
        pygame.draw.circle(win, self.COIN_COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)


class Enemy(Player):
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.color = ENEMY_COLOR
        self.size = 25

    def move(self):
        pass

def draw(win, player, coin, coin_count):
    win.fill(GRASS)

    score_text = COUNT_FONT.render(f"{coin_count}", 1, WHITE)
    win.blit(score_text, (WIDTH//2 - score_text.get_width()/2, 20))

    player.draw(win)
    coin.draw(win)

    pygame.display.update()

def player_movement(keys, player):
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player.velocity >=0:
        player.move(up=True)
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player.size + player.velocity <=HEIGHT:
        player.move(down=True)
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player.size + player.velocity <=WIDTH:
        player.move(right=True)
    if (keys[pygame.K_a] or keys[pygame.K_LEFT] ) and player.x - player.velocity >=0:
        player.move(left=True)

def collision_handler(player, coin):
    if player.x <= coin.x <= player.x + player.size:
        if player.y <= coin.y <= player.y + player.size:
            coin.move()
            return True
        

def main():
    #this is the main function for running the game loop.
    run = True
    clock = pygame.time.Clock()
    coinx = 400
    coiny = 300

    #Game Objects init
    player = Player(WIDTH//2 + 10, HEIGHT - 30)
    enemies = []
    coin = Coin(coinx, coiny)
    coin_count = 0
    enemy_count = coin_count + 1

    while run:
        clock.tick(FPS)
        draw(GAME_WINDOW, player, coin, coin_count)

        keys = pygame.key.get_pressed()
        player_movement(keys, player)

        if collision_handler(player, coin):
            coin_count += 1
            enemies.append(Enemy())
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if keys[pygame.K_ESCAPE]:
            run = False
            break
        
        


    pygame.quit()


if __name__ == "__main__":
    main()