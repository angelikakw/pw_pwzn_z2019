def count_letters(msg):
    stworzenie_listy = list(msg)
    posortowana_lista = sorted(stworzenie_listy)
    slownik = {}

    for litera in posortowana_lista:
        if litera not in slownik.keys():
            slownik[litera] = 1
        else:
            slownik[litera] += 1

    for litera, zliczenie in slownik.items():
        if zliczenie == max(slownik.values()):
            krotka = (litera, int(zliczenie))
            break

    return krotka

    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)