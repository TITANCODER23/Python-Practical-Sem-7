#Write a program to implement a two-player rock-paper-scissors game with input validation.
def rock_paper_scissors(player1, player2):
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if player1 == player2:
        return "It's a tie!"
    elif rules[player1] == player2:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Example usage:
choice1 = input("Player 1, enter rock, paper, or scissors: ").lower()
choice2 = input("Player 2, enter rock, paper, or scissors: ").lower()
result = rock_paper_scissors(choice1, choice2)
print(result)
