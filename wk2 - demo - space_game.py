import random

print("Welcome to Space Explorer: Monster Battle!")
name = input("Enter your astronaut name: ")
#health = int(input("Enter your starting health (1-100): "))

health_string = input("Enter your starting health (1-100): ")
health = int(health_string)
    
    
location = input("Go up a mountain, into a cave, or a field? ").lower()

if location == "mountain":
    first_monster = "Star Beast"
    new_weapon = "plasma rifle"
elif location == "asteroid field":
    first_monster = "Cosmic Drone"
    new_weapon = "ion cannon"
else:
    first_monster = "Cave Wraith"
    new_weapon = "sonic bomb"

#Make an list of weapons
weapons = ["laser", "sword", "blaster", "shield", "grenade"]

monsters = [first_monster, "Space Slime", "Cosmic Drone"]
game_over = False
for monster in monsters:
    if game_over:
        break
    print(f"\nHealth: {health}")
    print(f"You face a {monster}!")
    print(f"Weapons: {weapons}")
    weapon = input("Pick a weapon: ").lower()
    if weapon in weapons:
        if weapon == "laser" or weapon == new_weapon:
            print(f"{weapon} defeats {monster}! Gain 20 health.")
            health += 20
        elif weapon in ["sword", "blaster"]:
            damage = 10
            print(f"{weapon} wounds {monster}, but you lose {damage} health.")
            health -= damage
        else:
            damage = random.randint(20, 40)
            print(f"{weapon} fails! Lose {damage} health.")
            health -= damage
    else:
        damage = random.randint(15, 25)
        print(f"Invalid weapon! Lose {damage} health.")
        health -= damage
    if monster == first_monster:
        weapons.append(new_weapon)
        print(f"You found a {new_weapon}!")
    if health <= 0:
        print("Game Over! You died.")
        game_over = True
if not game_over:
    print(f"\nVictory! {name} defeated all monsters with {health} health!")