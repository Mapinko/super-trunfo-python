def battle_printing(p1_card, p2_card, attr_to_compare):
    print("p1_card -> ", p1_card)
    print("p2_card -> ", p2_card)
    print("attr_to_compare -> ", attr_to_compare)

    if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
        print(f'{p1_card["name"]} WINS!')
    elif p2_card[attr_to_compare] > p1_card[attr_to_compare]:
        print(f'{p2_card["name"]} WINS!')
    else:
        print("DRAW")
