"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""
import math


class Vector:

    def __init__(self, *args):
        self._dim = len(args)
        self.points = args  # Wymiar vectora

    @property
    def dim(self):
        return self._dim

    def __repr__(self):
        return str(self.points)

    def __len__(self):
        return self.dim

    @property
    def len(self):
        result = 0
        for i in self.points:
            result += i*i
        return math.sqrt(result)

    def __eq__(self, vector):
        if self.dim != vector.dim:
            return False

        for i in range(0, self.dim):
            if self.points[i] != vector.points[i]:
                return False

        return True

    def __add__(self, vector):
        result = []
        if self.dim == vector.dim:
            for i in range(0, self.dim):
                result.append(self.points[i] + vector.points[i])
        else:
            raise ValueError('Niezgodny wymiar')

        return Vector(*result)

    def __sub__(self, vector):
        result = []
        if self.dim == vector.dim:
            for i in range(0, self.dim):
                result.append(self.points[i] - vector.points[i])
        else:
            raise ValueError('Niezgodny wymiar')

        return Vector(*result)

    def __mul__(self, vector):
        if isinstance(vector, Vector):
            result = []
            if self.dim == vector.dim:
                for i in range(0, self.dim):
                    result.append(self.points[i] * vector.points[i])
            else:
                raise ValueError('Niezgodny wymiar')

            return sum(result)
        else:
            result = []
            for i in range(0, self.dim):
                result.append(self.points[i] * vector)

            return Vector(*result)


    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        result = []
        if len(beg) == len(end):
            for i in range(0, len(beg)):
                result.append(end[i] - beg[i])
        else:
            raise ValueError('Niezgodny wymiar')

        return tuple(result)

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        return cls(*Vector.calculate_vector(beg, end))


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)

    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
