import random

DINO_NAMES = (
    "Alenossauro Rex",
    "Lucirodonte",
    "Alex Raptor",
    "Caiquerátops",
    "Raphazilla",
    "Gustarodáctilo",
)

"""
FORMA MAIS BASICA =>
    def generate_dino_deck():
        dino_cards = []

        for dino_name in DINO_NAMES:
            dino_dict = {"name": dino_name, "strength": 2, "agility": 4, "heigth": 1}

            dino_cards.append(dino_dict)
        return dino_cards
"""


def generate_dino_deck():
    """
    LIST COMPREHENSION => LOGICA:
        - PEGAR TODOS O NOMES DENTRO DO DINO_NAMES
        - ENTRUTURAR NOVA LISTA COM NOVAS PRORPIEDADES: "strength, agility, heigth"
        - RETORNAR A NOVA LISTA
    """

    dino = [
        {
            "name": dino_name,
            "strength": random.randint(1, 10),
            "agility": round(random.uniform(0, 10), 1),
            "heigth": round(random.uniform(0, 10), 2),
        }
        for dino_name in DINO_NAMES
    ]

    return dino


def split_deck(deck: list[dict]) -> tuple[list[dict], list[dict]]:
    # BARRA DUPLA " // " PEGA A PARTE INTEIRA DA DIVISÃO
    half_deck = len(deck) // 2

    random.shuffle(deck)  # EMBARALHANDO O DECK

    print("deck 1")
    for card in deck[:half_deck]:  # deck[:3]
        print(card)

    print()

    print("deck 2")
    for card in deck[half_deck:]:  # deck[3:]
        print(card)

    return (deck[half_deck:], deck[:half_deck])
