import pygame
pygame.init()

setting_w = (700, 550)
window = pygame.display.set_mode(setting_w)
bg_png = pygame.image.load("1653866388_1-celes-club-p-kiberpank-oboi-krasivie-1.jpg")
player_png = pygame.image.load("pixil-frame-0.png")
enemy_png = pygame.image.load("pixil-frame-1.png")

clock = pygame.time.Clock()

pygame.display.set_caption('MAZE')

game = True

class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height=None, speed=None, hp=None, image=None):
        super().__init__(x, y, width, height)
        self.HP = hp
        self.SPEED = speed
        self.IMAGE = image

class Hero(Sprite):
    def __init__(self, x, y, width, height, image=None, hp=5, speed=5):
        super().__init__(x, y, width, height, speed, hp, image)
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}

    def move(self, window):
        if self.MOVE["UP"] == True:
            self.y -= self.SPEED
        if self.MOVE["DOWN"] == True:
            self.y += self.SPEED
        if self.MOVE["LEFT"] == True:
            self.x -= self.SPEED
        if self.MOVE["RIGHT"] == True:
            self.x += self.SPEED

hero = Hero(10, 10, 50, 50)
while game:
    window.blit(bg_png, (-200, -450))
    window.blit(player_png, (-100, 175))

    hero.move(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.MOVE["UP"] = True
            if event.key == pygame.K_s:
                hero.MOVE["DOWN"] = True
            if event.key == pygame.K_a:
                hero.MOVE["LEFT"] = True
            if event.key == pygame.K_d:
                hero.MOVE["RIGHT"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.MOVE["UP"] = False
            if event.key == pygame.K_s:
                hero.MOVE["DOWN"] = False
            if event.key == pygame.K_a:
                hero.MOVE["LEFT"] = False
            if event.key == pygame.K_d:
                hero.MOVE["RIGHT"] = False

    clock.tick(60)
    pygame.display.flip()