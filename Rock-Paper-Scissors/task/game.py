# Write your code here
import random
from pathlib import Path

def is_lose(spullen, player, computer) -> bool:
    """Does the player loose?"""
    looses_from, _ = vijanden(spullen, player)

    if computer in looses_from:
        return True
    else:
        return False

def is_win(spullen, player, computer):
    _, wins_from = vijanden(spullen, player)

    if computer in wins_from:
        return True
    else:
        return False

def is_draw(spullen, player, computer):

    if player == computer:
        return True
    else:
        return False

def vijanden(spullen, player):
    new_lijst = []
    
    index = spullen.index(player)
    new_lijst += spullen[index+1:]
    new_lijst += spullen[:index]

    midden = len(new_lijst) / 2
    vijanden = new_lijst[:int(midden)]
    vrienden = new_lijst[int(midden):] # They are friends because we can murder them.

    return vijanden, vrienden

aantal = 0
score = 0

name_player = input("Enter your name: ")
print(f"Hello, {name_player}")

ratings = Path("rating.txt").read_text().splitlines()

for line in ratings:
    name, rating = line.split()
    if name == name_player:
        score = int(rating)

spullen = input()

if len(spullen.split(",")) <= 3:
    spullen = "scissors,rock,paper"
spullen = spullen.split(',')

print("Okay, let's start")

while True:
    player = input()
    computer = random.choice(spullen)


    if player not in spullen + ["!exit", "!rating"]:
        print("Invalid input")

    elif player == "!rating":
        print(f"Your rating: {score}")

    elif player == "!exit":
        print("Bye!")
        break

    elif is_lose(spullen, player, computer):
        print(f"Sorry, but the computer chose {computer}")

    elif is_win(spullen, player, computer):
        print(f"Well done. The computer chose {computer} and failed")
        score += 100

    elif is_draw(spullen, player, computer):
        print(f"There is a draw ({computer})")
        score += 50

    else:
        print("igigf")

assert is_lose(['S', 'R', 'P'], player='R', computer='S') is False
#assert is_lose(['S', 'R', 'P'], player='R', computer='R') is True
assert is_lose(['S', 'R', 'P'], player='R', computer='P') is True


assert is_lose(['R', 'P', 'S'], player='R', computer='S') is False
#assert is_lose(['S', 'R', 'P'], player='R', computer='R') is True
assert is_lose(['R', 'P', 'S'], player='R', computer='P') is True

