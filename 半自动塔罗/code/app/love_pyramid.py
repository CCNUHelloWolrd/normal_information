from app.referrnce import reference
from app.main import main


def love_pyramid():
    card1 = main()

    card2 = main()

    card3 = main()

    card4 = main()
    print('本人：')
    print(card1)
    print(reference(card1))
    print('对方：')
    print(card2)
    print(reference(card2))
    print('关系：')
    print(card3)
    print(reference(card3))
    print('发展：')
    print(card4)
    print(reference(card4))
