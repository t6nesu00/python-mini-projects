# scissor paper rock game user vs computer
import random

user_won_count = 0
comp_won_count = 0
game_played = 0
tie_game = 0
def win():
    global user_won_count
    global game_played
    print("Congratulation! you won.")
    user_won_count += 1
    game_played += 1


def lose():
    global comp_won_count
    global game_played
    print("Sorry! you lose.")
    comp_won_count += 1
    game_played += 1


def tie():
    global tie_game
    global game_played
    print("Its a tie!")
    tie_game += 1
    game_played += 1


def main():
    condition = True
    while condition:
        options = ["scissor", "paper", "rock"]
        users_choice = input("It's your turn, please select one\n"
                             "(scissor, paper, rock, quit): ")
        computers_choice = random.choice(options)
        print("Computer has chosen: ", computers_choice)

        if users_choice == computers_choice:
            tie()
        elif users_choice == "scissor" and computers_choice == "paper":
            win()
        elif users_choice == "paper" and computers_choice == "rock":
            win()
        elif users_choice == "rock" and computers_choice == "scissor":
            win()
        elif users_choice == "paper" and computers_choice == "scissor":
            lose()
        elif users_choice == "rock" and computers_choice == "paper":
            lose()
        elif users_choice == "scissor" and computers_choice == "rock":
            lose()
        elif users_choice == "quit":
            break
        else:
            print("Please provide suitable value.")

    print("You played:", game_played, "game, you won:", user_won_count, "game, you lose:", comp_won_count, "game and", tie_game, "game tie.")


if __name__ == "__main__":
    main()
# created by Suman Nepali May, 2019
