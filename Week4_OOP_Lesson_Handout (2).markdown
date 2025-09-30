# Applied Technology – Week 4 Lesson Handout: Introduction to Object-Oriented Programming (OOP)

**Module**: Python Programming Foundations  
**Duration**: 1 hour (plus a 1–2 hour take-home assignment)  
**Objective**: Transition your Week 3 conditional logic text-based adventure game into an Object-Oriented Programming (OOP) framework in Python. Learn to organize code using classes and objects to manage locations, weapons, and player attributes like health and inventory.

## 🎯 Learning Targets
By the end of this lesson, you will be able to:  
- Understand the basics of Object-Oriented Programming (classes, objects, methods).  
- Refactor your Week 3 text-based adventure game (e.g., moving through locations or making choices) into an OOP structure.  
- Create and use Python classes with attributes (e.g., player health, inventory) and methods (e.g., move to a location, pick up a weapon).  
- Debug basic OOP-related errors in Python.

## 🧠 Key Concepts
- **Classes**: Blueprints for creating objects (e.g., a template for a player or location).  
- **Objects**: Instances of a class (e.g., a specific player or location).  
- **Attributes**: Data stored in an object (e.g., a player’s health or inventory).  
- **Methods**: Functions that belong to a class and define what objects can do (e.g., move or pick up a weapon).  
- **OOP Benefits**: Makes code reusable, organized, and easier to expand for larger games.

## 🗓️ Agenda
1. **Quick Review of Week 3 (10 min)**  
   - Revisit your Week 3 text-based adventure game (e.g., a game where players make choices to move through locations or interact with items).  
   - Discuss: Why is procedural code (using only conditionals and variables) hard to manage as the game grows?  
   - Example issue: Repeating code for each location or item interaction.  

2. **Introduction to OOP (15 min)**  
   - What is OOP? Think of it like organizing your game into "objects" (like players, locations, or weapons) that have properties (data) and actions (functions).  
   - Live demo: Convert a simple procedural adventure game snippet into a class-based structure.  
     ```python
     # Procedural (Week 3 style)
     player_name = "Hero"
     health = 100
     location = "Forest"
     if location == "Forest":
         print(f"{player_name} is in a dark forest with {health} health.")

     # OOP Version
     class Player:
         def __init__(self, name, health):
             self.name = name
             self.health = health
             self.location = "Forest"
         
         def display_status(self):
             print(f"{self.name} is in a {self.location} with {self.health} health.")
     
     hero = Player("Hero", 100)
     hero.display_status()
     ```

3. **Class Coding Walkthrough (15 min)**  
   - Together, we’ll start refactoring your Week 3 adventure game into an OOP framework.  
   - Example: Create a `Player` class to track health and inventory, and a `Location` class to manage game locations and choices.  
   - Key steps:  
     - Define a `Player` class with attributes (e.g., `name`, `health`, `inventory`).  
     - Define a `Location` class with attributes (e.g., `name`, `description`) and methods (e.g., `enter_location()`).  
     - Use methods to handle game logic (e.g., moving or picking up a weapon).  

4. **Student Challenge: Refactor Your Game (15 min)**  
   - **Task**: Take your Week 3 adventure game and start turning it into an OOP structure.  
   - **Requirements**:  
     - Create at least one class (e.g., `Player` or `Location`).  
     - Include at least two attributes (e.g., `health`, `inventory`, or `location_name`).  
     - Write at least one method that uses conditional logic from your Week 3 game (e.g., moving to a new location or picking up a weapon).  
     - Example output: A game where a `Player` moves between locations and collects items.  
   - Example code:  
     ```python
     class Player:
         def __init__(self, name):
             self.name = name
             self.health = 100
             self.inventory = []
             self.current_location = "Forest"
         
         def move_to(self, new_location):
             self.current_location = new_location
             print(f"{self.name} moves to the {self.current_location}.")
         
         def pickup_weapon(self, weapon):
             self.inventory.append(weapon)
             print(f"{self.name} picks up a {weapon}! Inventory: {self.inventory}")
     
     class Location:
         def __init__(self, name, description):
             self.name = name
             self.description = description
         
         def enter_location(self):
             print(f"You enter the {self.name}: {self.description}")
     
     # Create and play the game
     hero = Player("Alex")
     forest = Location("Forest", "A dark, misty forest with hidden treasures.")
     forest.enter_location()
     hero.move_to("Forest")
     hero.pickup_weapon("Sword")
     ```

5. **Share & Reflect (5 min)**  
   - Share your refactored game with a partner or the class.  
   - Discuss: How does the OOP version feel different? Was it easier to add new features like inventory?  

6. **Wrap-Up & Homework Explanation (5 min)**  
   - Review what makes OOP powerful: organization, reusability, and scalability for complex games.  
   - Preview Week 5: Functions and modularity to enhance your OOP skills.  
   - Assign the take-home project (see below).

## 🎒 Take-Home Assignment
**Task**: Fully refactor your Week 3 text-based adventure game into an OOP framework.  
- **Requirements**:  
  - Create at least one class (e.g., `Player`, `Location`, or `Weapon`).  
  - Include at least three attributes (e.g., `health`, `inventory`, `current_location`, or `location_description`).  
  - Write at least two methods that handle game logic (e.g., `move_to()`, `pickup_weapon()`, or `display_status()`).  
  - Use conditional logic from Week 3 in at least one method (e.g., check if the player can move or if health is sufficient).  
  - Test your game to ensure it works as expected.  
- **Example Idea**: If your Week 3 game had players choosing paths, create a `Location` class for each area (e.g., Forest, Cave) and a `Player` class to track `health` and `inventory`. Add a method to handle moving between locations or picking up items like a "Sword" or "Shield."  
- **Bonus**: Add a second class (e.g., a `Weapon` class with attributes like `name` and `damage`) and make the classes interact (e.g., picking up a weapon updates the player’s inventory).  

**Submission**: Share your Python script via your coding platform (e.g., Replit link or file upload) by the next class.

## 💡 Tips for Success
- **Start Small**: Focus on one part of your Week 3 game to refactor first (e.g., moving between locations or managing inventory).  
- **Test Often**: Run your code after adding each method to catch errors early (e.g., forgetting `self`).  
- **Ask for Help**: If you’re stuck on OOP syntax (like `self` or class setup), check with a classmate or the teacher.  
- **Think Like an Adventurer**: OOP is like designing a game world—each class (Player, Location, Weapon) is a piece of the story that works together!