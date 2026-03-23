import pygame


class GameScene:

    def __init__(self, repo):
        
        self.repo = repo

        
        self.player_x = 100
        self.player_y = 450
        self.speed = 5

        self.score = 0
        self.running = True

        self.font = pygame.font.SysFont(None, 32)

    
    def handle_input(self, keys):
        if keys[pygame.K_RIGHT]:
            self.player_x += self.speed
            self.score += 1

        if keys[pygame.K_LEFT]:
            self.player_x -= self.speed

    
    def update(self):
        
        if self.score >= 500:
            self.save_game()
            self.running = False

    
    def draw(self, screen):
        screen.fill((135, 206, 235))

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (self.player_x, self.player_y, 50, 50)
        )

        text = self.font.render(
            f"Score: {self.score}", True, (0, 0, 0)
        )
        screen.blit(text, (20, 20))

    
    def save_game(self):
        profile = {
            "score": self.score
        }

        self.repo.save_profile(1, profile)
        print("Juego guardado automáticamente")
