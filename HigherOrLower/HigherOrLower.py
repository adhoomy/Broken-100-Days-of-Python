import Art, GameData, random
from replit import clear

score = 0
compareA = random.randint(0, len(GameData.data)-1)

streak = True
while streak == True:
    print(f"{Art.logo}\n")
    
    accountA = GameData.data[compareA]
    print(f"Compare A: {accountA['name']}, a {accountA['description']}, from {accountA['country']}.")
    followersA = accountA['follower_count']
    print(f"{Art.vs}\n")
    
    compareB = random.randint(0, len(GameData.data)-1)
    while compareB==compareA:
        compareB = random.randint(0, len(GameData.data)-1)
    accountB = GameData.data[compareB]
    print(f"Compare B: {accountB['name']}, a {accountB['description']}, from {accountB['country']}.\n")
    followersB = accountB['follower_count']

    if followersA > followersB:
        answer = 'a'
    if followersB > followersA:
        answer = 'b'

    guess = input("Who has more followers? type 'A' or 'B': ").lower()
    while guess!='a' and guess!='b':
        guess = input("Please enter a valid input: ").lower()
    if guess!=answer:
        clear()
        print(Art.logo)
        print(f"Wrong, your final score is: {score}.")
        streak = False
    if guess==answer:
        score += 1
        compareA = compareB
        clear()