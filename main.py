import pygame
from persistence.profile_repository import ProfileRepository
from game_scene import GameScene

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

repo = ProfileRepository()
game = GameScene(repo)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    game.handle_input(keys)
    game.update()
    game.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()