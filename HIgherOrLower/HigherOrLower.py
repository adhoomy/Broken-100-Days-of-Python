import Art
import GameData
import random

streak = True
while streak == True:
    print(f"{Art.logo}\n")
    compareA = random.randint(0, len(GameData.data)-1)
    print(f"Compare A: {GameData.data[compareA]['name']}, a {GameData.data[compareA]['description']}, from {GameData.data[compareA]['country']}.")
    streak = False
