import pygame
from pygame.draw import *
from random import randint
pygame.init()

class Ball(object):
    def __init__(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.radius = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        
    def pos(self):
        return self.x, self.y

    def reborn(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.radius = randint(10, 100)
        self.color = COLORS[randint(0, 5)]
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        
    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.radius)

class Cube(object):
    def __init__(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.size = randint(15, 30)
        self.color = COLORS[randint(0, 5)]
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        
    def pos(self):
        return self.x, self.y

    def reborn(self):
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.size = randint(21, 25)
        self.color = COLORS[randint(0, 5)]
        self.vx = randint(-20, 20)
        self.vy = randint(-20, 20)
        
    def draw(self):
        rect(screen, self.color, ((self.x - self.size, self.y - self.size),
                                  (2 * self.size, 2 * self.size)))


FPS = 10
screen = pygame.display.set_mode((1200, 900))
rect(screen, (255, 255, 255), (0, 0, 150, 50))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
print('What is your name?')
name = input()

balls = []
for i in range(10):
    ball = Ball()
    balls.append(ball)
    ball.draw()
cubes = []
for i in range(5):
    cube = Cube()
    cubes.append(cube)
    cube.draw()
cnt = 0

pygame.display.update()
clock = pygame.time.Clock()
time = 0
font = pygame.font.Font(None, 30)


while time < 80 * FPS:
    rect(screen, (255, 255, 255), (0, 0, 150, 50))
    time += FPS
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for ball in balls:
                xb, yb = ball.pos()
                if (xb - x) ** 2 + (yb - y) ** 2 <= ball.radius ** 2:
                    print('ball')
                    cnt += 1
                    ball.reborn()
            f = 0
            for cube in cubes:
                xc, yc = cube.pos()
                if abs(xc - x) <= cube.size and abs(yc - y) <= cube.size:
                    print('cube')
                    cnt += 10
                    f = 1
                    break
            if f:
                for cube in cubes:
                    cube.reborn()
    cnt = str(cnt)
    s = 'Score: ' + cnt
    score_surf = font.render(s, False, (0, 0, 0))
    screen.blit(score_surf,(0,0))
    cnt = int(cnt)
                    
    for ball in balls:
        ball.draw()
        ball.x += ball.vx
        ball.y += ball.vy
        if ball.y < ball.radius or ball.y > 900 - ball.radius:
            ball.vy *= -1
        if ball.x < ball.radius or ball.x > 1200 - ball.radius:
            ball.vx *= -1
    for cube in cubes:
        cube.draw()
        cube.x += cube.vx
        cube.y += cube.vy
        if cube.y < cube.size or cube.y > 900 - cube.size:
            cube.vy *= -1
        if cube.x < cube.size or cube.x > 1200 - cube.size:
            cube.vx *= -1
    pygame.display.update()
    screen.fill(BLACK)
    
f = open('results.txt', 'r')
lines = [[str(cnt), '-', name]]
for line in f:
    if line != '\n':
        lines.append(line.split())
lines.sort(key = lambda x: int(x[0]))
lines.reverse()
f = open('results.txt', 'w')
for line in lines:
    f.write(' '.join(line))
    f.write('\n')
f.close()
print('Your score:', cnt)
pygame.quit()
