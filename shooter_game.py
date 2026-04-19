#Создай собственный Шутер!
from pygame import *
from random import randint
run = True

#mixer.init_()

win = display.set_mode((700, 500))
display.set_caption("Космические кораблики")
clock = time.Clock()
FPS = (60)

class GameSprite(sprite.Sprite):
    def __init__(self, name, x, y, speed, w, h):
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

class Emely(GameSprite):
    def update(self):
        if self.go == 'down':
            self.rect.y += self.speed
        if self.go == 'up':
            self.rect.y -= self.speed

Mad = GameSprite('galaxy.jpg', 0, 0, 0, 700, 500)
PlayerI = Player('rocket.png', 320, 300, 7, 60, 100)
monsters = sprite.Group()
monsters.add(Emely('asteroid.png', randint(50, 651), 0, 2, 50, 50))
while run:
    Mad.reset()
    PlayerI.reset()
    PlayerI.move()
    

    for e in event.get():
        if e.type == QUIT:
            run = False

    clock.tick(FPS)

    monsters.draw(win)

    monsters.update()
    display.update()