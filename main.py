import pygame
from persistence.profile_repository import ProfileRepository

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

repo = ProfileRepository()

player_x = 100
score = 0
running = True

font = pygame.font.SysFont(None, 32)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # guardar con S
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                repo.save_profile(1, {
                    "score": score
                })
                print("perfil guardado")

            if event.key == pygame.K_l:
                data = repo.get_profile(1)
                print("perfil cargado:", data)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x += 5
        score += 1

    screen.fill((135, 206, 235))

    pygame.draw.rect(screen, (255, 0, 0), (player_x, 450, 50, 50))

    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()