# IMPORT RELATIVO =>
from .deck import generate_dino_deck, get_random_attr, split_deck

# IMPORT ABSOLUTO =>
# from top_dino.deck import generate_dino_deck
# import top_dino -> NESSE CASO PRECISA REFERENCIAR NO __init__.py


def play():
    # 1 - Gerar o baralho
    dino_deck = generate_dino_deck()

    # 2 - Embaralhar e dividir o baralho em 2
    p1_deck, p2_deck = split_deck(dino_deck)
    # p1_deck, p2_deck => desempacotando o retorno

    print("deck 1")
    for card in p1_deck:
        print(card)

    print()

    print("deck 2")
    for card in p2_deck:
        print(card)
