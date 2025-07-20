from app.referrnce import reference
from app.main import main


def tricards():
    card1 = main()

    card2 = main()

    card3 = main()


    print('过去：')
    print(card1)
    print(reference(card1))
    print('现在：')
    print(card2)
    print(reference(card2))
    print('未来：')
    print(card3)
    print(reference(card3))
