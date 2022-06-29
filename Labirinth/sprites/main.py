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

picture = transform.scale(image.load('sprites/green.jpg'),(win_w,win_h))
display.set_caption('My window')
run = True
walls = sprite.Group()
wall1 = walls.add(GameSprite('sprites/wall_1.png',40,117,200,250))
wall2 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 200, 250))
wall3 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 297, 173))
wall4 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 337, 173))
wall5 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 347, 57))
wall6 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 250, 95))
wall7 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 5, 250))
wall8 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 100, 173))
wall9 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 100, 56))
wall10 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 100, 95))
wall11 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 100, -61))
wall12 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 430, -61))
wall13 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 430, 0)) #смерть или секрет
wall14 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 470, 78))
wall15 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 490, 117))
wall16 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 490, 274))
wall17 =walls.add(GameSprite('sprites/wall_2.png', 97, 40, 530, 194))
wall18 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 530, 284))
wall19 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 627, 194))
wall20 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 627, 284))
wall21 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 567, 78))
wall22 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 664, 78))
wall23 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 724, 284))
wall24 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 764, 244))
wall25 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 814, 204))
wall26 = walls.add(GameSprite('sprites/wall_2.png', 97, 40, 864, 164))
wall27 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 982, 0))
wall28 = walls.add(GameSprite('sprites/wall_1.png', 40, 117, 982, 247))



enemy1 = Player('sprites/enemy.png', 30, 30, 170, 290)
enemy2 = Player('sprites/enemy.png', 30, 30, 260, 220)
enemy3 = Player('sprites/enemy.png', 30, 30, 310, 140)
enemy4 = Player('sprites/enemy.png', 30, 30, 310, 65)
enemy5 = Player('sprites/enemy.png', 40, 40, 350, 15)
enemy6 = Player('sprites/fly_enemy.png', 44, 49, 445, 120)

hero = Player('sprites/shadow.png', 30, 39, 30, 340)
finish = GameSprite('sprites/finish.png', 30, 25, 530, 330)

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
    
    mw.blit(picture, (0,0))

    hero.reset()
    hero.update()
    
    wall1.reset()
    wall2.reset()
    wall3.reset()
    wall4.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    wall8.reset()
    wall9.reset()
    wall10.reset()
    wall11.reset()
    wall12.reset()
    wall13.reset()
    wall14.reset()
    wall15.reset()
    wall16.reset()
    wall17.reset()
    wall18.reset()
    wall19.reset()
    wall20.reset()
    wall21.reset()
    wall22.reset()
    wall23.reset()
    wall24.reset()
    wall25.reset()
    wall26.reset()
    wall27.reset()
    wall28.reset()
    
    enemy1.reset()
    enemy2.reset()
    enemy3.reset()
    enemy4.reset()
    enemy5.reset()
    enemy6.reset()
    
    finish.reset()
    display.update()