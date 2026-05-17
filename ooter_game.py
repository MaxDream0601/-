#Создай собственный Шутер!
from pygame import *
from random import randint
import os
import sys



def resource_path(relative_path):
    try:
        # PyInstaller создает временную папку _MEIPASS при сборке в один файл
        base_path = sys._MEIPASS
    except Exception:
        # Обычный запуск скрипта
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

run = True
time1 = 0
#mixer.init_()

win = display.set_mode((700, 500))
display.set_caption("Космические кораблики")
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, name, x, y, speed, w, h):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(name), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 696:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 4:
            self.rect.x -= self.speed
        if keys_pressed[K_w] and self.rect.y > 4:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 496:
            self.rect.y += self.speed
    def fire(self):
        # 1. Create bullet
        gun = Bullet('bullet.png', self.rect.centerx, self.rect.top, 10, 5, 10)
        # 2. Add bullet to group
        Bullets.add(gun)

monsters = sprite.Group()
Bullets = sprite.Group()
class Emely(GameSprite):
    def update(self):
        # move from up to bottom
        global time1
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            time1 += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

Mad = GameSprite(resource_path('assets/galaxy.jpg'), 0, 0, 0, 700, 500)
PlayerI = Player(resource_path('assets/rocket.png'), 320, 400, 7, 60, 100)
for i in range(5):
    Monster = Emely(resource_path('assets/asteroid.png'), randint(20, 680), 0, randint(1, 2), 50, 50)
    monsters.add(Monster)

while run:
  
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                PlayerI.fire()
                
    print(time1)
    Mad.reset()
    PlayerI.reset()
    PlayerI.move()
    # Monster.move_Emely()
    # gun.move_gun()

    collision = sprite.groupcollide(
        monsters,
        Bullets,
        True,
        True
    )



    monsters.draw(win)
    monsters.update()
    
    Bullets.draw(win)
    Bullets.update()

    clock.tick(FPS)
    display.update()