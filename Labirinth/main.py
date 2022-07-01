from pygame import *

win_w = 1022
win_h = 498
mw = display.set_mode((win_w, win_h))
surf = Surface((win_w, win_h-110))


class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.clamp_ip(surf.get_rect())


class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed=0, y_speed=0):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        wall_touch = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for wall in wall_touch:
                self.rect.right = min(self.rect.right, wall.rect.left)
        if self.x_speed < 0:
            for wall in wall_touch:
                self.rect.left = max(self.rect.left, wall.rect.right)
        if self.y_speed > 0:
            for wall in wall_touch:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)
        if self.y_speed < 0:
            for wall in wall_touch:
                self.rect.top = max(self.rect.top, wall.rect.bottom)

    def fire(self):
        bullets.add(Bullet('sprites/shot.png', 15, 4, self.rect.right, self.rect.centery, 10))


class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed=0, y_speed=0):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        wall_touch = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for wall in wall_touch:
                self.rect.right = min(self.rect.right, wall.rect.left)
                self.x_speed *= -1
        elif self.x_speed < 0:
            for wall in wall_touch:
                self.rect.right = max(self.rect.right, wall.rect.left)
                self.x_speed *= -1


class Bullet(GameSprite):
    def __init__(self, picture, w, h, x, y, speed=0):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed


picture = transform.scale(image.load('sprites/green.jpg'), (win_w, win_h))
win = transform.scale(image.load('sprites/level_complete.png'), (560, 170))
lose = transform.scale(image.load('sprites/lose.png'), (450, 200))
display.set_caption('My window')

walls = sprite.Group()
walls.add(GameSprite('sprites/wall_inv.png', 40, 117, -40, 250))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 200, 250))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 200, 250))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 297, 173))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 337, 173))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 347, 57))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 250, 95))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 5, 250))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 100, 173))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 100, 56))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 100, 95))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 100, -61))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 430, -61))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 430, 0))  # смерть или секрет
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 470, 78))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 490, 117))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 490, 280))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 530, 194))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 530, 284))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 627, 194))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 627, 284))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 567, 78))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 664, 78))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 724, 284))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 764, 244))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 814, 204))
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 864, 164))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 982, 0))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 982, 247))
walls.add(GameSprite('sprites/wall_inv.png', 40, 117, 1022, 117))


traps = sprite.Group()
traps.add(Enemy('sprites/enemy.png', 20, 20, 170, 300, 10))
traps.add(Enemy('sprites/enemy.png', 30, 30, 260, 220, 8))
traps.add(Enemy('sprites/enemy.png', 25, 25, 310, 140, 10))
traps.add(Enemy('sprites/enemy.png', 30, 30, 310, 60, 8))
traps.add(Enemy('sprites/enemy.png', 20, 20, 340, 215, 8))
traps.add(Enemy('sprites/enemy.png', 30, 30, 240, 295, 8))
traps.add(Enemy('sprites/enemy.png', 30, 30, 710, 160, 6))
traps.add(Enemy('sprites/enemy.png', 30, 30, 710, 115, 8))
traps.add(Enemy('sprites/enemy.png', 30, 30, 825, 290, 8))

enemies = sprite.Group()
enemies.add(Enemy('sprites/fly_enemy.png', 44, 49, 445, 120, 5))
enemies.add(Enemy('sprites/fly_enemy.png', 44, 49, 720, 235, 5))

hero = Player('sprites/shadow.png', 30, 39, 30, 340)
finish = GameSprite('sprites/finish.png', 30, 25, 530, 330)

bullets = sprite.Group()

run = True
end = False

while run:
    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                hero.y_speed = -8
            elif e.key == K_DOWN:
                hero.y_speed = 8
            elif e.key == K_LEFT:
                hero.x_speed = -8
            elif e.key == K_RIGHT:
                hero.x_speed = 8
            elif e.key == K_SPACE:
                hero.fire()
        elif e.type == KEYUP:
            if e.key == K_UP:
                hero.y_speed = 0
            elif e.key == K_DOWN:
                hero.y_speed = 0
            elif e.key == K_LEFT:
                hero.x_speed = 0
            elif e.key == K_RIGHT:
                hero.x_speed = 0
    if not end:
        mw.blit(picture, (0, 0))

        walls.draw(mw)

        enemies.update()
        enemies.draw(mw)

        traps.update()
        traps.draw(mw)

        finish.reset()

        hero.reset()
        hero.update()

        bullets.update()
        bullets.draw(mw)

        sprite.groupcollide(bullets, walls, True, False)
        sprite.groupcollide(bullets, enemies, True, True)

        if sprite.collide_rect(hero, finish):
            end = True
            mw.blit(win, (255, 160))

        elif sprite.spritecollide(hero, enemies, False) or sprite.spritecollide(hero, traps, False):
            end = True
            mw.blit(lose, (286, 149))

    display.update()
