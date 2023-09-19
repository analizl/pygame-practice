import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Single collition")

rect_1 = pygame.Rect(0,0,25,25)
obstacle_rect = pygame.Rect(random.randint(0,500), random.randint(0,300), 25, 25)

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.mouse.set_visible(False)

run = True
while run:
  screen.fill(BG)

  col = GREEN
  if rect_1.colliderect(obstacle_rect):
    col = RED

  pos = pygame.mouse.get_pos()
  rect_1.center = pos

  pygame.draw.rect(screen, col, rect_1)
  pygame.draw.rect(screen, BLUE, obstacle_rect)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()

