import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards():
    rand1 = random.randint(0, 12)
    rand2 = random.randint(0, 12)
    return [cards[rand1], cards[rand2]]
    


def sum_cards(_cards):
    total = 0
    for card in _cards:
        total += card
    return total


users_cards = draw_cards()
computer_cards = draw_cards()


def game_board():
    is_continue_playing = True
    while is_continue_playing:
        users_sum_cards = sum_cards(users_cards)
        computer_sum_cards = sum_cards(computer_cards)
        user_cards_length = len(users_cards)
        comp_cards_length = len(computer_cards)

        print(f"Your cards: {users_cards}. Sum = {users_sum_cards}")
        print(f"Computer cards: {computer_cards}. Sum = {computer_sum_cards}")
        print('\n\n')
        
        if computer_sum_cards == 21:
            return print("Game Over! Computer Won\n")
        elif users_sum_cards == 21:
            return print("You Won!\n")
        elif users_sum_cards > 21:
            return print(f"You Lost, the sum: {users_sum_cards}\n")
        elif computer_sum_cards > 21:
            return print(f"The computer risked it, and lost. The sum: {computer_sum_cards}\n")
        elif user_cards_length > 2 and comp_cards_length > 2:
            if users_sum_cards > computer_sum_cards:
                print("User won")
            elif computer_sum_cards > users_sum_cards:
                print("Computer won")
            else:
                print("Draw!!!")
        elif comp_cards_length == 2:
            another_card = input('Do you want another card? "y": yes, "n": no\n')
            if another_card == "y":
                rand = random.randint(0, 12)
                users_cards.append(cards[rand])
                game_board()
            elif another_card == "n":
                if computer_sum_cards < 17:
                    rand = random.randint(0, 12)
                    computer_cards.append(cards[rand])
                elif computer_sum_cards > 17:
                    if computer_sum_cards > users_sum_cards:
                        return print("Computer won")
                    elif users_sum_cards > computer_sum_cards:
                        print("User won")
                    else:
                        print("Draw!!!")
                else:
                    is_continue_playing = False
                    



yORn = input('Hello Player, are you ready? "y": yes, "n": no\n')

if yORn == "y":
    game_board()
elif yORn == "n":
    print("Okay")
