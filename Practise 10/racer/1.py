# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0 
COIN_SCORE = 0 # НОВОЕ: Переменная для подсчета собранных монет

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Loading background
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# НОВОЕ: Класс для Монетки (Coin), похожий на Enemy, но со своей картинкой
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # ВАЖНО: Вам понадобится картинка "Coin.png" в папке с игрой
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        # Появляется в случайной точке по X, за пределами экрана сверху
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        # Монетка падает вниз с той же скоростью, что и враги
        self.rect.move_ip(0, SPEED)
        # Если монетка пролетела мимо экрана, возвращаем ее наверх
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin() # НОВОЕ: Создаем объект монетки

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group() # НОВОЕ: Группа специально для монеток
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1) # НОВОЕ: Добавляем монетку ко всем спрайтам для отрисовки

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
       
    # Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    
    # Отрисовка счета уклонений (слева)
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    # НОВОЕ: Отрисовка количества собранных монет (справа)
    # Формируем текст и размещаем его ближе к правому краю (x=280, y=10)
    coin_scores_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_scores_text, (280,10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # НОВОЕ: Проверка столкновения игрока с монетками
    # Используем spritecollide, чтобы получить список монеток, с которыми столкнулись
    collided_coins = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collided_coins:
        COIN_SCORE += 1 # Увеличиваем счетчик монет
        # Перемещаем собранную монетку обратно наверх, чтобы она упала снова
        coin.rect.top = 0
        coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          # pygame.mixer.Sound('crash.wav').play() # Раскомментируйте, если есть файл
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)