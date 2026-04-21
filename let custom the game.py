import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Simple Sprite")
bg_colors = [(0, 0, 255), (173, 216, 230), (0, 0, 139)]
sprite_colors = [(255, 255, 0), (255, 0, 255), (255, 165, 0), (255, 255, 255)]
bg_color = random.choice(bg_colors)
rect = pygame.Rect(100, 100, 30, 20)
dx = random.choice([-3, 3])
dy = random.choice([-3, 3])
color = random.choice(sprite_colors)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect.x += dx
    rect.y += dy
    if rect.left <= 0 or rect.right >= 500:
        dx = -dx
        color = random.choice(sprite_colors)
        bg_color = random.choice(bg_colors)
    if rect.top <= 0 or rect.bottom >= 400:
        dy = -dy
        color = random.choice(sprite_colors)
        bg_color = random.choice(bg_colors)
    screen.fill(bg_color)
    pygame.draw.rect(screen, color, rect)
    pygame.display.update()
    pygame.time.delay(10)
pygame.quit()