# Tuple Out Game
Line one Imports the random module to simulate dice rolls

Lines 2–4 define a function to roll a specified number of 6-sided dice.

Lines 6–13 prompt the user to enter the number of players (1–6).
Includes a while loop to validate the input and ensure it is an integer within the valid range.

Lines 15–25 prompt the user to enter a score limit for the game (50–100).
Uses a while loop to validate the input and ensure it is an integer within the valid range.

Lines 27–124 are the main function for running the game.

Calls the players() and max_score() functions to determine the number of players and score limit.
scores = [0] * num_players
Initializes a list of scores for each player, starting at 0.
end_game = False
A flag to determine if the game should end.

Lines 37–38 iterate through all players, allowing each to take a turn.

The count_roll() function runs the code for each player to roll all 3 dice

A player is allowed to roll each dice until they tuple out or until that dice is the same as another dice, where it is 'locked' as shown in line 62 with dice 1 and 2.
The score after the player chooses to end their turn or they tuple out is calculated by adding the three dice scores together, like in line 70, or by setting the score for that round to zero in the case of a tuple, like in line 76

I need to figure out a way to end the game and make it so that if max score is reached, the game ends and that player is the winner