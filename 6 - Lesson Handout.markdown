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