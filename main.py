import time
import random

MAX_BOARD_VAL = 100

#placing the snakes
snakes = {
    36: 6,
    32: 10,
    48: 26,
    62: 18,
    88: 24,
    95: 56,
    97: 78
}

# ladder takes you up from 'key' to 'value'
ladders = {
     4: 14,
     8: 30,
    21: 42,
    28: 76,
    50: 67,
    80: 99,
    71: 92,
}

#prints prompt msgs
player_text = [
    "Your turn",
    "GO!!",
    "Roll it",
]
#prints msg when you take a ladder
ladder_text = ["Up up and away", "WHOOOOOP"]
#prints msg when you hit a snake
snake_text = ["Ouchieee", "Loser"]


#prints welcome msg
def welcome_msg():
    msg = """"
  Welcome to snakes and ladders
  Hit enter and roll away
  """
    print(msg)


#gets the name of the players
def get_player_names():
    player1_name = None
    playerNames = ['', '']
    while not player1_name:
        player1_name = input("Player 1, please enter a name: ")

    player2_name = None
    while not player2_name:
        player2_name = input("Player 2, please enter a name: ")

    print("#####################################################\n")

    print("Are ya ready? '" + player1_name + "' and '" + player2_name + "'\n")

    print("#####################################################")
    playerNames[0] = player1_name
    playerNames[1] = player2_name
    return playerNames


#roll the dice
def roll_dice():
    time.sleep(1)
    dice_value = random.randint(1, 6)
    print("\n#####################################################")
    print("\n You have rolled a: " + str(dice_value))
    print("\n#####################################################")

    return dice_value


def got_snake(old_val, new_val, player_name):

    print("\n" + str(player_name) + " got bit by the snake ane fell from" +
          str(old_val) + "to " + str(new_val))
    print("\n#####################################################")
    print("\n" + str(player_name) + " is on " + str(new_val))
    print("\n" + random.choice(snake_text).upper())
    print("\n#####################################################")


def got_ladder(old_val, new_val, player_name):
    print("\n" + random.choice(ladder_text).upper())
    print("\n" + str(player_name) + " took the ladder and climbed from " +
          str(old_val) + "to " + str(new_val))
    print("\n" + str(player_name) + " is on " + str(new_val))
    
    print("\n#####################################################")


def game_logic(player_name, new_val, dice_val):
    time.sleep(1)
    old_val = new_val
    new_val = new_val + dice_val

    if new_val > MAX_BOARD_VAL:
        print("\n You'll need " + str(MAX_BOARD_VAL - old_val) +
              " to win the game")

        print("\n" + str(player_name) + " is on " + str(old_val))
        print("\n#####################################################")
        return old_val

    else:
        print("\n" + str(player_name) + " moved from " + str(old_val) +
              " to " + str(new_val))

        print("\n" + str(player_name) + " is on " + str(new_val))
        print("\n#####################################################")
        

    if new_val in snakes:
        final_value = snakes.get(new_val)
        got_snake(new_val, final_value, player_name)

    elif new_val in ladders:
        final_value = ladders.get(new_val)
        got_ladder(new_val, final_value, player_name)

    else:
        final_value = new_val

    return final_value


def check_win(player_name, position):
    time.sleep(1)
    if MAX_BOARD_VAL == position:
        print("\n#####################################################")
        print("\n Congratulations!!! " + str(player_name) +
              " has won the game")
        print("\n#####################################################")
        print("\n Goooodbye")
        print("\n#####################################################")
        exit()


def start_game():
    welcome_msg()
    time.sleep(1)
    player_name = get_player_names()
    #player2_name = get_player_names()

    player1_curr_pos = 0
    player2_curr_pos = 0

    while True:

        time.sleep(1)
        input_break = input("\n" + player_name[0] + ": \n" +
                            random.choice(player_text) +
                            "\nHit the enter to roll dice: ")

        print("\nRolling Dice")

        while True:
            dice_value = roll_dice()
            
            if (dice_value != 6):
                break
            else:
              print(
                  "\n" + player_name[0] + " has rolled a 6 and therefore will have another turn")
              print(str(player_name[0]) + " moving...")
              player1_curr_pos = game_logic(player_name[0], player1_curr_pos,
                                      dice_value)



        print(str(player_name[0]) + " moving...")
        player1_curr_pos = game_logic(player_name[0], player1_curr_pos,
                                      dice_value)
        check_win(player_name[0], player1_curr_pos)

        input_break2 = input("\n" + player_name[1] + ": \n" +
                             random.choice(player_text) +
                            "\nHit the enter to roll dice: ")

        print("\n Dice rolling")

        while True:
            dice_value = roll_dice()
            
            if (dice_value != 6):
                break
            else:
              print(
                  "\n" + player_name[1] + " has rolled a 6 and therefore will have another turn"
              )
              print(str(player_name[1]) + " moving...")
              player2_curr_pos = game_logic(player_name[1], player2_curr_pos,
                                      dice_value)

        print(str(player_name[1]) + " moving...")
        player2_curr_pos = game_logic(player_name[1], player2_curr_pos,
                                      dice_value)
        check_win(player_name[1], player1_curr_pos)


if __name__ == "__main__":
    start_game()
