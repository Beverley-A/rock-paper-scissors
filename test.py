# Rock Paper Scissors Game 
import random  # Provides functionality for random selections, used here for computer choices
import json    # Allows saving and loading data in JSON format, used here for storing game state
import os      # Provides functions to interact with the operating system, used to check if a save file exists

# Randomly generates the computer's choice of rock, paper, or scissors
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Determines the winner based on game rules for Rock, Paper, Scissors
def determine_winner(player1_choice, player2_choice):
    # Define winning relationships: each key beats the corresponding value
    outcomes = {
        "rock": "scissors",  # Rock beats Scissors
        "scissors": "paper",  # Scissors beat Paper
        "paper": "rock"       # Paper beats Rock
    }
    if player1_choice == player2_choice:
        return "it's a Draw"  # Return "draw" if both players make the same choice
    if outcomes[player1_choice] == player2_choice:
        return "player1"      # Return "player1" if player1 wins
    else:
        return "player2"      # Otherwise, return "player2" as the winner

# Saves the current game state (player names and scores) to a JSON file
def save_game(player1, player2, scores):
    """Save the current game state to a JSON file."""
    game_data = {
        "player1": player1,
        "player2": player2,
        "scores": scores  # Include player names and scores in the saved data
    }
    # Write the game data to 'score_dump.json'
    with open("score_dump.json", "w") as file:
        json.dump(game_data, file)
    print("Game saved.")  # Confirm that the game has been saved successfully

# Loads a saved game if it exists and matches the provided player names
def load_game(player1_name, player2_name):
    # Check if save file exists to load previous game data
    if os.path.exists("score_dump.json"):
        with open("score_dump.json", "r") as file:
            data = json.load(file)  # Load JSON data from the file
        # Confirm players' names match saved game data, then return it
        if data["player1"] == player1_name and data["player2"] == player2_name:
            print("Game loaded successfully.")
            return data["player1"], data["player2"], data["scores"]
    # If no matching saved game is found, start a new game with 0 scores
    print("No saved game found. Starting a new game.")
    return player1_name, player2_name, {player1_name: 0, player2_name: 0}

# Main function to run the Rock, Paper, Scissors game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    # Get player names or allow "computer" as the opponent
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name or type 'computer' to play against the computer: ")
    
    # Ask if players want to load a previously saved game
    if input("Do you want to load a saved game? (y/n): ").lower() == "y":
        saved_player1, saved_player2, scores = load_game(player1, player2)
        if saved_player1 is None:
            scores = {player1: 0, player2: 0}  # Initialize new game scores if no saved data found
    else:
        scores = {player1: 0, player2: 0}  # Start with zeroed scores if no load requested

    choices = ["rock", "paper", "scissors"]  # Valid choices for the game

    # Loop to continue rounds until players choose to end
    while True:
        # Get player1's choice and validate it
        player1_choice = input(f"{player1}, choose rock, paper, or scissors: ").lower()
        if player1_choice not in choices:
            print("Invalid choice. Try again.")  # Notify on invalid input
            continue  # Restart loop if input invalid

        # Get player2's choice or random choice if player2 is computer
        player2_choice = get_computer_choice() if player2.lower() == "computer" else input(f"{player2}, choose rock, paper, or scissors: ").lower()
        if player2_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        # Determine round winner
        winner = determine_winner(player1_choice, player2_choice)
        if winner == "it's a Draw":
            print("It's a draw!")  # Announce if draw
        else:
            # Announce round winner and update their score
            print(f"{player1 if winner == 'player1' else player2} wins this round!")
            scores[player1 if winner == 'player1' else player2] += 1

        # Display current scores
        print(f"Score: {player1} - {scores[player1]}, {player2} - {scores[player2]}")

        # Offer to save game progress after each round
        if input("Do you want to save the game? (y/n): ").lower() == "y":
            save_game(player1, player2, scores)

        # Option to play another round or end game
        if input("Play another round? (y/n): ").lower() != "y":
            break

    # Display final scores when game ends
    print("Thanks for playing!")
    print(f"Final Score: {player1} - {scores[player1]}, {player2} - {scores[player2]}")

# If the script is executed directly, start the game
if __name__ == "__main__":
    play_game()

