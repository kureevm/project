import pygame
import os
from random import randrange

x, y = randrange(0, 500, 50), randrange(0, 500, 50)
point = randrange(0, 500, 50), randrange(0, 500, 50)
length = 1
snake = [(x, y)]
qx, qy = 0, 0
control = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True, }
score = 0
speed_count, snake_speed = 0, 10

pygame.init()
pygame.display.set_caption("Змейка")
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load(os.path.join("fon.jpg")).convert(), (500, 500))
font_score = pygame.font.Font('font.ttf', 25)
font_end = pygame.font.Font('font.ttf', 50)


def terminate():
    pygame.quit()
    exit()


def drawIntro():
    fontintro = pygame.font.Font('font.ttf', 62)
    fontintrokg = pygame.font.Font('font.ttf', 13)
    fontintrostart = pygame.font.Font('font.ttf', 18)
    textintro = fontintro.render("ИГРА ЗМЕЙКА", True, [80, 80, 80])
    textintrostart = fontintrostart.render("нажмите клавишу для начала", True, [255, 255, 55])
    textintrokg = fontintrokg.render("", True, [0, 255, 255])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return

        screen.blit(bg, (0, 0))
        screen.blit(textintro, (68, 150))
        screen.blit(textintrostart, (3, 220))
        screen.blit(textintrokg, (362, 488))
        pygame.display.update()
        clock.tick(60)


drawIntro()


def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()


while True:
    screen.fill(pygame.Color(70, 70, 70))
    [pygame.draw.rect(screen, pygame.Color(0, 200, 255), (i, w, 50, 50)) for i, w in snake]
    pygame.draw.rect(screen, pygame.Color(255, 0, 0), (*point, 50, 50))
    render_score = font_score.render(f'очки: {score}', 1, pygame.Color(0, 255, 0))
    render_length = font_score.render(f'длина змейки: {length}', 1, pygame.Color(0, 255, 0))
    screen.blit(render_score, (5, 455))
    screen.blit(render_length, (5, 475))
    speed_count += 1
    if not speed_count % snake_speed:
	    x += qx * 50
	    y += qy * 50
	    snake.append((x, y))
	    snake = snake[-length:]
    if snake[-1] == point:
        point = randrange(0, 500, 50), randrange(0, 500, 50)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 7)
    if x < 0 or x > 450 or y < 0 or y > 450 or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('ВЫ ПРОИГРАЛИ', 1, pygame.Color(255, 55, 0))
            render_score = font_score.render(f'ваwи очки: {score}', 1, pygame.Color(255, 255, 0))
            render_length = font_score.render(f'длина змейки: {length}', 1, pygame.Color(0, 255, 255))
            screen.blit(render_end, (85, 175))
            screen.blit(render_score, (85, 225))
            screen.blit(render_length, (85, 255))
            pygame.display.flip()
            quit()


    pygame.display.flip()
    clock.tick(60)
    quit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        if control['UP']:
            qx, qy = 0, -1
            control = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
    elif key[pygame.K_DOWN]:
        if control['DOWN']:
            qx, qy = 0, 1
            control = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
    elif key[pygame.K_LEFT]:
        if control['LEFT']:
            qx, qy = -1, 0
            control = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
    elif key[pygame.K_RIGHT]:
        if control['RIGHT']:
            qx, qy = 1, 0
            control = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}