import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Stars")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self):
        self.width = 60
        self.height = 20
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 7
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# Star class
class Star:
    def __init__(self):
        self.radius = 10
        self.x = random.randint(0, WIDTH - self.radius * 2)
        self.y = 0
        self.speed = random.randint(3, 6)
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def fall(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.ellipse(screen, YELLOW, self.rect)

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)

# Game setup
player = Player()
stars = []
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move and draw player
    player.move(keys)
    player.draw()

    # Update and draw stars
    for star in stars[:]:
        star.fall()
        star.draw()
        if star.check_collision(player.rect):
            stars.remove(star)
            score += 1
        elif star.rect.top > HEIGHT:
            stars.remove(star)

    # Add new stars randomly
    if random.randint(1, 1) == 1:
        stars.append(Star())

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()