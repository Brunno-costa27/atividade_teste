
import sys

sys.path.append('src/')
from atividade import ThisIsTriangle


class TestSidesValues:

    def test_differentSides(self):
        assert ThisIsTriangle.verificaTriangulo(5, 4, 3) == True

    def test_containingZero(self):
        assert ThisIsTriangle.verificaTriangulo(5, 0, 3) == False

    def test_equalSides(self):
        assert ThisIsTriangle.verificaTriangulo(5, 5, 5) == True

    def test_allZero(self):
        assert ThisIsTriangle.verificaTriangulo(0, 0, 0) == False
