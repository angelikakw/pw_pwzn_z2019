"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""
import math


class Figure:

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area():.3f}, '
            f'perimeter={self.perimeter():.3f}'
        )


class Circle(Figure):

    def __init__(self, r):
        self._r = r

    @property
    def r(self):
        return self._r

    @staticmethod
    def _area(r):
        return math.pi * r * r

    def area(self):
        return self._area(self.r)

    def set_r(self, r):
        self._r = r

    def perimeter(self):
        return math.pi * self.r * 2


class Rectangle(Figure):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @staticmethod
    def _area(a, b):
        return a * b

    def area(self):
        return self._area(self.a, self.b)

    def set_a(self, a):
        self._a = a

    def set_b(self, b):
        self._b = b

    def perimeter(self):
        return 2*self.a + 2*self.b


class Diamond(Figure):

    def __init__(self, e, f):
        self._e = e
        self._f = f

    @property
    def f(self):
        return self._f

    @property
    def e(self):
        return self._e

    def set_e(self, e):
        self._e = e

    def set_f(self, f):
        self._f = f

    def are_diagonals_equal(self):
        return self.f == self.e

    @staticmethod
    def _area(e, f):
        return 0.5 * e * f

    def area(self):
        return self._area(self.e, self.f)

    def side_len(self):
        return math.sqrt((0.5 * self.e) ** 2 + (0.5 * self.f) ** 2)

    def perimeter(self):
        return 4 * self.side_len()

    def to_square(self):
        if self.are_diagonals_equal():
            return Square(self.side_len())
        raise RuntimeError("Nierowne przekatne.")


class Square(Rectangle, Diamond):

    def __init__(self, a):
        super(Square, self).__init__(a, a)

    def set_a(self, a):
        self._a = a
        self._b = a
        self._e = math.sqrt(2*a*a)
        self._f = self._e

    def set_b(self, b):
        self._a = b
        self._b = b
        self._e = math.sqrt(2*b*b)
        self._f = self._e

    def set_e(self, e):
        self._e = e
        self._f = e
        self._a = math.sqrt(e * e / 2)
        self._b = self._a

    def set_f(self, f):
        self._e = f
        self._f = f
        self._a = math.sqrt(f * f / 2)
        self._b = self._a


if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'
