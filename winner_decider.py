def decide_winner(player_hand, computer_hand):
    winner = ""

    if player_hand == "rock" and computer_hand == "hand":
        winner = "Computer"
    elif player_hand == "rock" and computer_hand == "scissors":
        winner = "Player"
    elif player_hand == "scissors" and computer_hand == "rock":
        winner = "Computer"
    elif player_hand == "scissors" and computer_hand == "hand":
        winner = "Player"
    elif player_hand == "hand" and computer_hand == "scissors":
        winner = "Computer"
    elif player_hand == "hand" and computer_hand == "rock":
        winner = "Player"
    else:
        winner = "Draw"
    
    color = (0, 255, 0) if winner == "Player" else ((255, 0, 0) if winner == "Computer" else (0, 0, 255))

    return winner, color