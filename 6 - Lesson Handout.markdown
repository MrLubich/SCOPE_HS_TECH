# 🧠 Week 6 Python Lesson Plan: Catch the Falling Stars — Building Games with Custom Methods

## 🎮 Theme: Catch the Falling Stars
This week, students will build a Pygame-based game where a player moves left/right to catch falling stars, earning points. The focus is on implementing **custom methods** in classes to define object behaviors, enhancing code organization and reusability.

---

## ✅ Review: Core Python Concepts
Before diving into new material, let’s review what we’ve covered in previous weeks:

- **Classes & Objects**: Built `Game`, `Player`, and `Location` classes to structure a game world.
- **Attributes**: Objects store their own data (e.g., health, weapons, monsters, location).
- **Object Relationships**: Objects reference each other (e.g., `game.player`, `game.locations`).
- **Lists & Loops**: Used to manage collections like monsters, weapons, and game flow.
- **Conditionals**: Handled combat, health changes, and input validation.
- **User Input**: Players choose locations and weapons using `input()`.

---

## 🆕 New Concept: Custom Methods in Classes

### 🎯 What Are Custom Methods?
Custom methods are **functions defined inside a class** that specify what an object can do. They allow objects to perform actions using their own data (attributes).

### 🧪 Example
```python
class Player:
    def move_to(self, location):
        self.location = location
        print(f"You moved to {location.name}")
```
In this example, the `move_to` method updates the player’s location and prints a message.

### 🧠 Why Use Custom Methods?
- **Organization**: Keeps related code inside the class.
- **Reusability**: Methods can be called multiple times on different objects.
- **Encapsulation**: Methods work with an object’s own data, making behavior intuitive.

---

## 🎮 This Week’s Game: Catch the Falling Stars

### Game Overview
Students will create a Pygame where:
- A **Player** moves left/right using keyboard input.
- **Star** objects fall from the top of the screen.
- The player catches stars to earn points.

### 🧱 Key Classes
1. **Player**:
   - Attributes: `position`, `speed`
   - Methods: `.move()` to change position based on input
2. **Star**:
   - Attributes: `position`, `speed`
   - Methods: `.fall()` to move downward, `.check_collision()` to detect if caught by the player

---

## 🧪 Challenge: Expand the Game

### 🧩 Your Mission
Enhance the game by adding:
- **At least two new custom methods** to the `Player` or `Star` classes.
- **One new feature or mechanic** to make the game more engaging.

### 🧠 Ideas to Try
- Add a `.reset()` method to restart the game.
- Add a `.missed()` counter to track stars that fall past the player.
- Add a `.power_up()` method to temporarily increase player speed.
- Add a `Star.type` attribute with different effects (e.g., bonus stars worth more points, slow stars).
- Add sound effects or visual feedback when catching a star.

---

## 📝 Submission Checklist
To ensure your project meets the requirements, check off the following:

- [ ] Game runs without errors.
- [ ] At least **2 new custom methods** added to the `Player` or `Star` classes.
- [ ] At least **1 new feature or mechanic** implemented.
- [ ] Code is **commented and organized** for readability.
- [ ] You can explain what each custom method does.

---

## 💻 Demo Code
Below is the starter code for *Catch the Falling Stars*. Use this as a foundation and add your custom methods and new feature as part of the challenge.

```python
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
    if random.randint(1, 20) == 1:
        stars.append(Star())

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

---

## 📚 Learning Objectives
By the end of this lesson, students will:
1. Understand how to define and use **custom methods** in classes.
2. Apply custom methods to create interactive game behaviors.
3. Enhance a game with new features using object-oriented programming.
4. Write organized, commented code that’s easy to understand and maintain.

---

## 🛠️ Setup Instructions
1. Install Pygame: `pip install pygame`
2. Create a new Python file (e.g., `catch_the_stars.py`) and copy the demo code above.
3. Test the base game to ensure it runs.
4. Implement your new methods and feature as part of the challenge.
5. Submit your code to GitHub with clear comments and a README explaining your new methods and feature.

---

Happy coding, and let’s catch those stars! 🌟