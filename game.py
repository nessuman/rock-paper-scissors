from random import randint

options = ['rock', 'paper', 'scissors']

def isWinner(computerSelection, playerSelection):
    if computerSelection == 'rock':
        if playerSelection == 'paper':
            return -1
        elif playerSelection == 'scissors':
            return 1
        elif playerSelection == "rock":
            return 0
    elif computerSelection == 'paper':
        if playerSelection == 'rock':
            return 1
        elif playerSelection == 'scissors':
            return -1
        elif playerSelection == "paper":
            return 0
    elif computerSelection == 'scissors':
        if playerSelection == 'paper':
            return 1
        elif playerSelection == 'rock':
            return -1
        elif playerSelection == "scissors":
            return 0
    else:
        return None

def computerPlay():
    randIdx = randint(0, len(options)-1)
    return options[randIdx]

def playRound(computerSelection, playerSelection):
    computerSelection = computerSelection.lower()
    playerSelection = playerSelection.lower()
    if playerSelection not in options:
        return None

    roundResult = None
    roundResultText = ""

    roundResult = isWinner(computerSelection, playerSelection)

    if roundResult == 1:
        roundResultText = "You Win! {player} beats {computer}.".format(player=playerSelection.capitalize(), computer=computerSelection.capitalize())
    elif roundResult == -1:
        roundResultText = "You Lose! {computer} beats {player}.".format(player=playerSelection.capitalize(), computer=computerSelection.capitalize())
    elif roundResult == 0:
        roundResultText = "It's a tie!"

    print(roundResultText + "\n")
    return roundResult

def game():
    winCount = 0
    numReps = 5

    for i in range(numReps):
        result = None
        while result == None:

            playerSelection = input("Rock, Paper, Scissors?: ")
            computerSelection = computerPlay()

            result = playRound(computerSelection, playerSelection)

        if result == 1:
            winCount += result

    finalText = "The final score is {winCount}/{numReps}.".format(winCount=winCount, numReps=numReps)

    if winCount >= (numReps/2):
        finalText += " You won!"
    else:
        finalText += " You lose!"

    return finalText

print(game())