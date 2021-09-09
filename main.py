import random

import art


def draw_card(count):    
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_cards = []
    for _ in range(count):
        drawn_cards.append(random.choice(card_deck))
    return drawn_cards


def calculate_score(card_list):
    temp_card_list = card_list.copy()
    temp_card_list.sort(reverse=True)
    score = 0
    if temp_card_list == [11, 10]:
        return score
    else:
        score = sum(temp_card_list)
        while score > 21 and temp_card_list[0] == 11:
            temp_card_list.pop(0)
            temp_card_list.append(1)
            score = sum(temp_card_list)
        return score


def display_score(plyr_list, game_over):

    if plyr_list[0]["has_blackjack"]:
        print(f"Dealer's cards: {fix_aces(plyr_list[0]['cards'])} BLACKJACK!")
    elif game_over:
        print(f"Dealer's cards: {fix_aces(plyr_list[0]['cards'])} Score: {plyr_list[0]['score']}")
    else:
        print(f"Dealer's first card: {fix_aces(plyr_list[0]['revealed_cards'])} Score: ??")

    if plyr_list[1]["has_blackjack"]:
        print(f"Your cards: {fix_aces(plyr_list[1]['cards'])} BLACKJACK!")
    else:
        print(f"Your cards: {fix_aces(plyr_list[1]['cards'])} Score: {plyr_list[1]['score']}")


def fix_aces(card_list):
    
    formatted_list = []
    for val in card_list:
        if val == 11:
            formatted_list.append("[A]")
        else:
            formatted_list.append(f"[{val}]")
    return "".join(formatted_list)


def play():

    cpu = {
        "cards": [],
        "revealed_cards": [],
        "score": 0,
        "has_blackjack": False,
    }
    user = {
        "cards": [],
        "score": 0,
        "has_blackjack": False,
    }
    list_of_players = [cpu, user]

    is_game_over = False


    for player in list_of_players:
        player["cards"] = draw_card(2)
        player["score"] = calculate_score(player["cards"])
        if player["score"] == 0:
            player["has_blackjack"] = True

    list_of_players[0]["revealed_cards"] = [list_of_players[0]["cards"][0]]


    if cpu["has_blackjack"] or user["has_blackjack"]:
        is_game_over = True

 
    if not is_game_over:
        user_done = False
        while not user_done:
            display_score(list_of_players, is_game_over)
            print("\nType \"y\" to get another card, type \"n\" to pass.")
            card_choice = input("> ")
            if card_choice == "y":
                print("You draw a card.\n")
                user["cards"].extend(draw_card(1))
                user["score"] = calculate_score(user["cards"])
                if user["score"] > 21:
                    user_done = True
                    is_game_over = True
            else:
                user_done = True

    if not is_game_over:
        while cpu["score"] < 17:
            print("The dealer draws a card.\n")
            cpu["cards"].extend(draw_card(1))
            cpu["score"] = calculate_score(cpu["cards"])

    is_game_over = True
    display_score(list_of_players, is_game_over)

  
    if cpu["has_blackjack"] and not user["has_blackjack"]:
        print("\nDealer has a blackjack, DEALER wins.\n")
    elif cpu["has_blackjack"] and user["has_blackjack"]:
        print("\nYou both have a blackjack, it's a tie!\n")
    elif user["has_blackjack"]:
        print("\nYou have a blackjack, YOU win.\n")
    elif cpu["score"] > 21:
        print("\nDealer went over. YOU win.\n")
    elif user["score"] > 21:
        print("\nYou went over. DEALER wins.\n")
    elif user["score"] == cpu["score"]:
        print("\nIt's a tie!\n")
    elif user["score"] > cpu["score"]:
        print("\nYOU win.\n")
    else:
        print("\nDEALER wins.\n")



while True:
    print(art.logo)
    play()
    print("Do you want to to play another round?")
    quit_choice = input("> ")
    if quit_choice != "y":
        break

    print("\n" * 100)

print("Thanks for playing!")
