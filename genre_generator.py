from random import randint

genre_lists = [
    [
        "аллегоричный", "апокалиптический", "аутентичный", "грязный", "дественный", "деструктивный", "дикий",
        "допотопный", "ебучий", "загробный", "задорный", "классический", "креационистический", "крикливый",
        "крупногабаритный", "меланхоличный", "нигилистический", "ностальгический", "позитивный", "пошлый",
        "прогрессивный", "ревущий", "светлый", "светский", "сельский", "современный", "суицидальный", "тёмный",
        "утрированный", "фанковый", "футуристичный"
    ],
    [
        "пост", "трилл", "хаус", "даун", "синт", "поп", "фолк", "эмо", "сэд", "глитч", "порно", "электро", "олд",
        "техно", "нью", "стрит", "клауд", "блэк", "хард", "аква", "нейчарал", "гей", "укро", "пхонк", "дип", "некро",
        "психо", "трэш", "софт", "лайт", "шэдоу"
    ],
    [
        "рэп", "рок", "фанк", "джаз", "хардкор", "фолк", "металл", "панк", "битдаун", "ска", "вейв", "транс",
        "арэнби", "рэгги", "дабстэп", "драм эн бэйз"
    ]
]
zlist = zip(range(3), map(lambda i: randint(0, len(genre_lists[i]) - 1), range(3)))
print('{} {} {}'.format(*map(lambda i: genre_lists[i[0]][i[1]], zlist)))