import pygame
import random
from time import sleep

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("deki.jpg")
ball = pygame.image.load("boof.png")
x = 0
y = 480-robot.get_height()

robot_width = robot.get_width()
robot_height = robot.get_height()
ball_width = ball.get_width()
ball_height = ball.get_height()

to_right = False
to_left = False

score = 0

asteriod_position = []
pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)

for i in range(100):
    x1 = random.randint(0, 640 - ball_width)
    y1 = random.randint(0, 480) * random.randint(-100, -1)
    asteriod_position.append((x1, y1))

clock = pygame.time.Clock()

game_font = pygame.font.SysFont("Arial", 24)

ended = False

while not ended:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()
    for i, (x1, y1) in enumerate(asteriod_position):
        if y1 < 480:
            y1 += 2
            asteriod_position[i] = (x1, y1)
        else:
            asteriod_position.pop(i)
            print(f"Your score was: {score}")
            ended = True
            
    if to_right:
        x += 5
        if x + robot_width > 640:
            x = 640 - robot_width
    if to_left:
        x -= 5
        if x < 0:
            x = 0
    
    for i, (x1, y1) in enumerate(asteriod_position):
        if 480 - robot_height - ball_height < y1 < 480 and ((x < x1 < x + robot_width) or (x < x1 + ball_width < x + robot_width)):
            asteriod_position.pop(i)
            score += 1
            
    text = game_font.render(f"Score: {score}", True, (100, 0, 100))
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    for (x1, y1) in asteriod_position:
        window.blit(ball, (x1, y1))
    window.blit(text, (500, 0))
    pygame.display.flip()

    clock.tick(75)
    
game_font = pygame.font.SysFont("Times New Roman", 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    text1 = game_font.render(f"JA {'NI' if score == 0 else ''}SAM{' TESKA ' if score > 10 else ' '}NARKOMANCINA:", True, (0, 0, 0))
    text2 = game_font.render(f"{score} BUKSNI SAM ISPUSIO", True, (0, 0, 0))
    window.fill((255, 255, 255))
    window.blit(robot, (x, y))
    window.blit(text1, (10, 150))
    window.blit(text2, (80, 200))
    pygame.display.flip()
