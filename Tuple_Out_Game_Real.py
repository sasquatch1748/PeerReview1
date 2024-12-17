import random

# functions for each dice roll

# dice 1 roll
def dice_1():
    """creates a dictionary of numbers for the random function to choose from"""
    dice_1 = [1, 2, 3, 4, 5, 6]
    dice_1_roll = random.choice(dice_1)
    return(dice_1_roll)

# dice 2 roll
def dice_2():
    dice_2 = [1, 2, 3, 4, 5, 6]
    dice_2_roll = random.choice(dice_2)
    return dice_2_roll

# dice 3 roll
def dice_3():
    dice_3 = [1, 2, 3, 4, 5, 6]
    dice_3_roll = random.choice(dice_3)
    return dice_3_roll


# number of players from 1-6
def players():
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if 6 >= num_players >= 1:
                return num_players
            else:
                print("Number of players must be between 1-6")
        # Only allows for integers
        except ValueError:
            print("Please enter in a number")


# winning score from 50-100
def max_score():
    while True:
        try:
            max = int(input("Enter the score limit to win: "))
            if 100 >= max >= 50:
                return max
            else:
                print("Max score must be between 50 and 100")
        # Only allows for integers
        except ValueError:
            print("Please enter in a number")

# dice rolling intro (first roll and additional rolls if no dice are equal)
    
    
# main game loop
def game_loop():
    print("Welcome to the tuple dice game!")
    num_players = players()
    score_limit = max_score()
    scores = [0] * num_players
    end_game = False
    
    while not end_game:
        for i in range(num_players):
            score = 0
            dice1, dice2, dice3 = dice_1(), dice_2(), dice_3()
            print(f"Player {i + 1}'s turn:")
            print(f"Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}")
            
            while True:
                
                
                # Scnenario 1: all dice are the same (Tuple out)
                if dice1 == dice2 == dice3:
                    print("Sorry, you have tupled out. Your score that round is 0.")
                    score += 0
                    break

                #Adding error handling if input is something different than yes or no
                
                # Scnenario 2: two dice are the same
                elif dice1 == dice2 and dice3 != dice2:
                    print(f"Dice 1 and Dice 2 are locked with a score of {dice1}")
                    re_roll = input(f"Would you like to re-roll dice 3? It currently has a score of {dice3}. (yes/no): ")
                    if re_roll.lower() == "yes":
                        dice3 = dice_3()
                    elif re_roll.lower() == "no":
                        break
                    else:
                        print("Please enter yes/no")

                elif dice1 == dice3 and dice2 != dice3:
                    print(f"Dice 1 and Dice 3 are locked with a score of {dice1}")
                    re_roll = input(f"Would you like to re-roll dice 2? It currently has a score of {dice2}. (yes/no): ")
                    if re_roll.lower() == "yes":
                        dice2 = dice_2()
                    elif re_roll.lower() == "no":
                        break
                    else:
                        print("Please enter yes/no")
            
                elif dice2 == dice3 and dice1 != dice3:
                    print(f"Dice 2 and Dice 3 are locked with a score of {dice2}")
                    re_roll = input(f"Would you like to re-roll dice 1? It currently has a score of {dice1}. (yes/no): ")
                    if re_roll.lower() == "yes":
                        dice1 = dice_1()
                    elif re_roll.lower() == "no":
                        break
                    else:
                        print("Please enter yes/no")
                        
                        
                # Scnenario 3: all dice are different
                else:
                    print ("None of the dice are locked.")
                    re_roll_choice = input("Would you like to re-roll all dice or specific dice? Enter 'all', '1', '2', '3', or 'none': ").strip().lower()

                    if re_roll_choice == "all":
                        dice1, dice2, dice3 = dice_1(), dice_2(), dice_3()
                    elif re_roll_choice == "1":
                        dice1 = dice_1()
                    elif re_roll_choice == "2":
                        dice2 = dice_2()
                    elif re_roll_choice == "3":
                        dice3 = dice_3()
                    elif re_roll_choice == "none":
                        break
                    else:
                        print("Invalid input. Please enter 'all', '1', '2', '3', or 'none'.")
                        
                # Dice values after turn
                print(f"Updated Dice Rolls:\nDice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}")

            # Calculate final score for the round
            score = dice1 + dice2 + dice3
            print(f"Player {i + 1}'s score this round: {score}")
            scores[i] += score
            
            # Check if the player has reached the score limit
            if scores[i] >= score_limit:
                print(f"Player {i + 1} wins the game with a score of {scores[i]}!")
                end_game = True
                break
                            
            #I think a head to head scoreboard of the current game session would be a cool feature that would be beneficial
            
game_loop()
            
