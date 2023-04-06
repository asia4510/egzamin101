import random

shapes = ['paper', 'rock', 'scissors']


def player_shape():
    player_choice = input("Choose paper, rock or scissors: ")
    return str(player_choice).lower()

def computer_shape():
    computer_choice = random.choice(shapes)
    return str(computer_choice)

def paper_rock_scissors(player_shape, computer_shape):
    
    if player_choice == computer_choice:
        print("It's a draw, nobody gets a point")
    elif player_choice == 'paper':
        if computer_choice == 'rock':
            print("You scored a point!")
            points['player'] += 1
        else:
            points['computer'] += 1
            print("Computer scored a point")
    elif player_choice == 'rock':
        if computer_choice == 'scissors':
            print("You scored a point!")
            points['player'] += 1
        else:
            print("Computer scored a point")
            points['computer'] += 1
    elif player_choice == 'scissors':
        if computer_choice == 'paper':
            print("You scored a point!")
            points['player'] += 1
        else:
            print("Computer scored a point")
            points['computer'] += 1
            

points = {'player': 0, 'computer': 0}

# Whoever wins at least 3 times wins the overall game

while (points['player'] < 3) and (points['computer'] < 3):

    player_choice = player_shape()

    while player_choice not in shapes:
        print("That's not a valid shape")
        player_choice = player_shape()

    computer_choice = computer_shape()
    print(f"Computer chose: {computer_choice}")
    game = paper_rock_scissors(player_shape, computer_shape)

    print(points)
    print()

print("Game over")
if points['player'] > points['computer']:
    print("You won a game :-)")
else:
    print("You lost :-(")




       

#Winner: first to win two throws    
    
##print("Winner is the one who wins two throws first")      


