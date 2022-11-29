# IMPORT RELATIVO =>
from .battle import battle_printing
from .deck import generate_dino_deck, get_random_attr, split_deck

# IMPORT ABSOLUTO =>
# from top_dino.deck import generate_dino_deck
# import top_dino -> NESSE CASO PRECISA REFERENCIAR NO __init__.py


def play():
    # 1 - Gerar o baralho
    dino_deck = generate_dino_deck()

    # 2 - Embaralhar e dividir o baralho em 2
    p1_deck, p2_deck = split_deck(dino_deck)
    # p1_deck, p2_deck => DESEMPACOTA O RETORNO

    for index, p1_card in enumerate(p1_deck):
        attr_to_compare = get_random_attr(p1_card)
        p2_card = p2_deck[index]

        print()
        battle_printing(p1_card, p2_card, attr_to_compare)
