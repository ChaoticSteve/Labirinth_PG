from pygame import *
win_w = 1022
win_h = 498
mw = display.set_mode((win_w,win_h))

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        mw.blit(self.image,(self.rect.x, self.rect.y))

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
        elif self.x_speed < 0:
            for wall in wall_touch:
                self.rect.left = max(self.rect.left, wall.rect.right)
        elif self.y_speed > 0:
            for wall in wall_touch:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)
        elif self.y_speed < 0:
            for wall in wall_touch:
                self.rect.top = max(self.rect.top, wall.rect.bottom)

picture = transform.scale(image.load('sprites/green.jpg'),(win_w,win_h))
win = transform.scale(image.load('sprites/level_complete.png'), (560, 170))
display.set_caption('My window')
run = True
walls = sprite.Group()
walls.add(GameSprite('sprites/wall_1.png',40,117,200,250))
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
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 430, 0)) #смерть или секрет
walls.add(GameSprite('sprites/wall_2.png', 97, 40, 470, 78))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 490, 117))
walls.add(GameSprite('sprites/wall_1.png', 40, 117, 490, 274))
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



enemy1 = Player('sprites/enemy.png', 30, 30, 170, 290)
enemy2 = Player('sprites/enemy.png', 30, 30, 260, 220)
enemy3 = Player('sprites/enemy.png', 30, 30, 310, 140)
enemy4 = Player('sprites/enemy.png', 30, 30, 310, 65)
enemy5 = Player('sprites/enemy.png', 40, 40, 350, 15)
enemy6 = Player('sprites/fly_enemy.png', 44, 49, 445, 120)

hero = Player('sprites/shadow.png', 30, 39, 30, 340)
finish = GameSprite('sprites/finish.png', 30, 25, 530, 330)

end = False
while run:
    time.delay(50)
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                hero.y_speed = -5
            elif e.key == K_DOWN:
                hero.y_speed = 5
            elif e.key == K_LEFT:
                hero.x_speed = -5
            elif e.key == K_RIGHT:
                hero.x_speed = 5
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
        mw.blit(picture, (0,0))
   
        walls.draw(mw)
    
        enemy1.reset()
        enemy2.reset()
        enemy3.reset()
        enemy4.reset()
        enemy5.reset()
        enemy6.reset()
    
        finish.reset()

        hero.reset()
        hero.update()
        if sprite.collide_rect(hero, finish):
            end = True
            mw.blit(win,(255, 160))
    display.update()