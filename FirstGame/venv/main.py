import pygame
pygame.init()

import random

WIDTH = 800
HEIGHT = 600

GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explorer Game")

FPS = 60
COUNT_FONT = pygame.font.SysFont("comicsans", 50)
TEXT_FONT = pygame.font.SysFont("comicsans", 30)

#color variables
GRASS = (0, 75, 25)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ENEMY_COLOR = (255, 0, 50)
PLAYER_COLOR = (51, 187, 255)

class Player:
    def __init__(self, x, y, size=30, color=PLAYER_COLOR, velocity=5):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity = velocity
        self.body = pygame.Rect(self.x, self.y, self.size, self.size)


    def draw(self, win):
        pygame.draw.rect(win, self.color, self.body)

    def move(self, up=False, down=False, right=False, left=False):
        if up:
            self.y -= self.velocity
        if down:
            self.y += self.velocity
        if right:
            self.x += self.velocity
        if left:
            self.x -= self.velocity

        self.body.update(self.x, self. y, self.size, self.size)



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
        self.vel_choice = [1, 2, 3]
        self.direction_choice = [-1, 1]
        self.velocity_x = random.choice(self.vel_choice)
        self.velocity_y = random.choice(self.vel_choice)
        self.direction_x = random.choice(self.direction_choice)
        self.direction_y = random.choice(self.direction_choice)
        self.body = pygame.Rect(self.x, self. y, self.size, self.size)

    def move(self):
        self.x += self.direction_x * self.velocity_x
        self.y += self.direction_y * self.velocity_y



        if self.y + self.size >= HEIGHT:
            self.velocity_y *= -1
        elif self.y <= 0:
            self.velocity_y *= -1

        if self.x + self.size >= WIDTH:
            self.velocity_x *= -1
        elif self.x <= 0:
            self.velocity_x *= -1

        self.body.update(self.x, self. y, self.size, self.size)


def draw(win, player, coin, coin_count, enemies, tutorial):
    win.fill(GRASS)

    score_text = COUNT_FONT.render(f"{coin_count}", 1, WHITE)
    win.blit(score_text, (WIDTH//2 - score_text.get_width()/2, 20))

    if tutorial:
        tutorial1 = TEXT_FONT.render("WASD/ARROW KEYS to move around.", 1, WHITE)
        tutorial2 = TEXT_FONT.render("Collect the Coins and avoid the Enemies!", 1, WHITE)

        win.blit(tutorial1, (WIDTH//2 - tutorial1.get_width()/2, 100))
        win.blit(tutorial2, (WIDTH//2 - tutorial2.get_width()/2, 140))

    player.draw(win)
    coin.draw(win)

    for i in range(len(enemies)):
            enemies[i+1].draw(win)
            enemies[i+1].move()
    

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

def coin_collector(player, coin):
    if player.x <= coin.x <= player.x + player.size:
        if player.y <= coin.y <= player.y + player.size:
            coin.move()
            return True
        
def enemy_collision(player, enemy):
    if player.body.colliderect(enemy.body):
        return True



def main():
    replay = True
    while replay:
        #this is the main function for running the game loop.
        run = True
        tutorial = True
        clock = pygame.time.Clock()
        coinx = 400
        coiny = 300
        coin_count = 0

        #Game Objects init
        player = Player(WIDTH//2 + 10, HEIGHT - 30)
        coin = Coin(coinx, coiny)
        enemies = dict()
        enemy_count = coin_count
        
        
        while run:
            clock.tick(FPS)

            if enemy_count != coin_count:
                enemy_count += 1
                enemies[enemy_count] = Enemy()
            
            
            draw(GAME_WINDOW, player, coin, coin_count, enemies, tutorial)
            

            keys = pygame.key.get_pressed()
            player_movement(keys, player)

            for i in range(len(enemies)):
                if enemy_collision(player, enemies[i+1]):
                    lose_text = COUNT_FONT.render(f"Game Over! Score: {coin_count}", 1, WHITE)
                    GAME_WINDOW.blit(lose_text, (WIDTH//2 - lose_text.get_width()/2, HEIGHT//2 - lose_text.get_height()/2))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False
                    break
            

            if coin_collector(player, coin):
                coin_count += 1
                tutorial = False
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    replay = False
                    break

            if keys[pygame.K_ESCAPE]:
                run = False
                replay = False
                break
        
        


    pygame.quit()


if __name__ == "__main__":
    main()