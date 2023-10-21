import pygame
pygame.init()

setting_w = (700, 550)
window = pygame.display.set_mode(setting_w)
bg_png = pygame.image.load("1653866388_1-celes-club-p-kiberpank-oboi-krasivie-1.jpg")
clock = pygame.time.Clock()

pygame.display.set_caption('MAZE')

game = True

class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height=None, speed=None, hp=None, image=None):
        super().__init__(x, y, width, height)
        self.HP = hp
        self.SPEED = speed
        self.IMAGE = image

    def move(self, x, y):
        self.x += x
        self.y += y

class Hero(Sprite):
    def __init__(self, x, y, width, height, image=None, hp=5, speed=5):
        super().__init__(x, y, width, height, speed, hp, image)
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}

player_png = Hero(10, 10, 50, 50)
player_png.IMAGE = pygame.image.load("pixil-frame-0.png")  

while game:
    window.blit(bg_png, (-200, -450))
    window.blit(player_png.IMAGE, (player_png.x, player_png.y))

    x_movement = 0
    y_movement = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_png.MOVE["UP"] = True
            if event.key == pygame.K_s:
                player_png.MOVE["DOWN"] = True
            if event.key == pygame.K_a:
                player_png.MOVE["LEFT"] = True
            if event.key == pygame.K_d:
                player_png.MOVE["RIGHT"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_png.MOVE["UP"] = False
            if event.key == pygame.K_s:
                player_png.MOVE["DOWN"] = False
            if event.key == pygame.K_a:
                player_png.MOVE["LEFT"] = False
            if event.key == pygame.K_d:
                player_png.MOVE["RIGHT"] = False

    if player_png.MOVE["UP"]:
        y_movement = -player_png.SPEED
    if player_png.MOVE["DOWN"]:
        y_movement = player_png.SPEED
    if player_png.MOVE["LEFT"]:
        x_movement = -player_png.SPEED
    if player_png.MOVE["RIGHT"]:
        x_movement = player_png.SPEED

    player_png.move(x_movement, y_movement)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()