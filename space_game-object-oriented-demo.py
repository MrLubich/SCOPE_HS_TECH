import random

# Game Class -
# Game class will hold all current game information like the list of all rooms and player state
# Ex Player Health, Player Location
class Game:
    def __init__(self):
        self.gameOver = False
        self.player = None
        self.monsters = ["Space Slime", "Cosmic Drone"]
        self.locations = []

# The location class will hold all the data of where the player wants to move
# EX: The mountain - Name: Mountain - First Monster they Encounter: Star Beast - The new weapon they will get at that location: plasma rifle
class Location:
    def __init__(self, game, name, firstMonster, newWeapon):
        self.name = name
        self.firstMonster = firstMonster
        self.newWeapon = newWeapon
        game.locations.append(self)

# Will hold all player data - will be way more useful with the more features added to game
# But for now it will hold all the player data like health and weapons
class Player:
    def __init__(self, game, name, health):
        self.name = name
        self.health = health
        self.location = None
        self.weapons = ["laser", "sword", "blaster", "shield", "grenade"]
        game.player = self

# Setup
myGame = Game()
myPlayer = Player(myGame, input("Enter your astronaut name: "), int(input("Enter your starting health (1-100): ")))
mountain = Location(myGame, "Mountain", "Star Beast", "plasma rifle")
cave = Location(myGame, "Cave", "Cave Wraith", "sonic bomb")
astroidField = Location(myGame, "Astroid Field", "Cosmic Drone", "ion cannon")

## --- Game Logic ---

# Figure out where player should move to
print(f"Where would you like to go {myPlayer.name}?")
for location in myGame.locations:
    # What on earth is the \u2022
    # Whenever using a backslash symbol (\) it denotes a special character
    # You will most commonly see it with an "n" like this \n denoting a new line
    # In this case it just makes a bullet point
    print(f"\u2022 {location.name}")
moveLocation = input()

# Finds the correct location object based of the object name and user input
for location in myGame.locations:
    if moveLocation.lower() == location.name.lower():
        myPlayer.location = location
        print(f"You entered {location.name}")
        # Put the first monster at the front of the list
        myGame.monsters.insert(0, location.firstMonster)

# Will say if the player didn't enter structure - will happen if the user didn't input the correct text!
if not myPlayer.location:
    print(f"{myPlayer.name} didn't enter structure")
    randomLocation = myGame.locations[random.randint(0, 2)]
    myPlayer.location = randomLocation
    myGame.monsters.insert(0, myPlayer.location.firstMonster)
    print(f"You have stumbled apon the {myPlayer.location.name}")

# Loop through all monsters
for monster in myGame.monsters:
    # Conditional used to break the monster loop if you die
    if myGame.gameOver:
        break
    print(f"\nHealth: {myPlayer.health}")
    print(f"You face a {monster}!")
    print(f"Weapons: ")
    for weapon in myPlayer.weapons:
        print(f"\u2022 {weapon}")
    weapon = input("Pick a weapon: ").lower()

    if weapon in myPlayer.weapons:
        if weapon == "laser" or weapon == myPlayer.weapons[0]:
            print(f"{weapon} defeats {monster}! Gain 20 health.")
            myPlayer.health += 20
        elif weapon in ["sword", "blaster"]:
            damage = 10
            print(f"{weapon} wounds {monster}, but you lose {damage} health.")
            myPlayer.health -= damage
        else:
            damage = random.randint(20, 40)
            print(f"{weapon} fails! Lose {damage} health.")
            myPlayer.health -= damage
    else:
        damage = random.randint(15, 25)
        print(f"Invalid weapon! Lose {damage} health.")
        myPlayer.health -= damage

    # Check if it is the "first monster"
    if monster == myPlayer.location.firstMonster:
        myPlayer.weapons.insert(0, myPlayer.location.newWeapon)
        print(f"You found {myPlayer.location.newWeapon}")

    if myPlayer.health <= 0:
        print("Game Over! You died.")
        myGame.gameOver = True

if not myGame.gameOver:
    print(f"\nCongratulations {myPlayer.name}! You defeated all the monsters with {myPlayer.health} health!")
