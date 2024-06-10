from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards are not removed from deck when drawn, each card in list will have equal probability

choice = (input("Do you want to play a game of Blackjack? type 'y' or 'n': ")).lower()
while choice!="y" and choice!="n":
    choice = (input("Please type a valid input: ")).lower()
if choice=="y":
    clear()