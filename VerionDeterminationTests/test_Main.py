
from unittest import TestCase

from VerionDetermination.Main import Main


class TestMain(TestCase):

    def test_add(self):
        main = Main()
        result = main.add(2, 2)
        assert result == 4
        pass

    pass
