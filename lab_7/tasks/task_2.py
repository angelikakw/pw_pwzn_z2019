import numpy as np


def calculate_neighbours(board):
    """
    Returns number of neighbours of board cells.

    Funkcja zwraca tablicę która w polu [R, C] zwraca liczbę sąsiadów którą
    ma komórka board[R, C].
    Obowiązuje sąsiedztwo Moore'a tzn. za sąsiada uznajemy żywą komórkę
    stykającą się bokiem bokach lub na ukos od danej komórki,
    więc maksymalna ilość sąsiadów danej komórki wynosi 8.
    Funkcja ta powinna być zwektoryzowana, tzn. liczba operacji w bytecodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.
    (1 pkt.)

    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczby prawych sąsiadów
    itp.
    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :param periodic
    """
    # left
    lu = np.pad(board[:-1, :-1].astype(np.int8), ((1, 0), (1, 0)))
    lc = np.pad(board[:, :-1].astype(np.int8), ((0, 0), (1, 0)))
    ld = np.pad(board[1:, :-1].astype(np.int8), ((0, 1), (1, 0)))

    # center
    down = np.pad(board[1:, :].astype(np.int8), ((0, 1), (0, 0)))
    up = np.pad(board[:-1, :].astype(np.int8), ((1, 0), (0, 0)))

    # right
    ru = np.pad(board[:-1, 1:].astype(np.int8), ((1, 0), (0, 1)))
    rc = np.pad(board[:, 1:].astype(np.int8), ((0, 0), (0, 1)))
    rd = np.pad(board[1:, 1:].astype(np.int8), ((0, 1), (0, 1)))

    return lu + lc + ld + up + down + ru + rc + rd


def iterate(board):
    """
    Returns next iteration step of given board.

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.
    Zasady Game of life są takie:
    1. Komórka może być albo żywa (True) albo martwa (False).
    2. Jeśli komórka jest martwa i ma trzech sąsiadów to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadów również umiera.
       W przeciwnym wypadku (dwóch lub trzech sąsiadów) to żyje dalej.
    (1 pkt.)

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :return: next board state
    :rtype: np.ndarray
    """
    neibs = calculate_neighbours(board)
    # return (board & ((neibs >= 2) & (neibs <= 3))) | (np.invert(board) & (neibs == 3)))
    # optimized:
    return board & (neibs == 2) | (neibs == 3)


if __name__ == '__main__':
    _board = np.array([
        [False, False, False,  True, False,  True],
        [ True, False,  True, False, False,  True],
        [ True,  True, False,  True,  True,  True],
        [False,  True,  True, False, False,  True],
        [False, False, False,  True, False, False],
        [False,  True,  True,  True, False,  True]
    ])
    print(iterate(_board))
    assert np.array_equal(calculate_neighbours(_board), np.array([
        [1, 2, 2, 1, 3, 1,],
        [2, 4, 3, 4, 6, 3,],
        [3, 5, 5, 3, 4, 3,],
        [3, 3, 4, 4, 5, 2,],
        [2, 4, 6, 3, 4, 2,],
        [1, 1, 3, 2, 3, 0,],
    ]))
    assert np.array_equal(iterate(_board), np.array([
        [False, False, False, False, True, False],
        [ True, False,  True, False, False,  True],
        [ True, False, False,  True, False,  True],
        [ True,  True, False, False, False,  True],
        [False, False, False,  True, False, False],
        [False, False,  True,  True, True, False],
    ]))

