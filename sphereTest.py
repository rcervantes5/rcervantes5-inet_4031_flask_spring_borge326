import unittest
import sphere

class cylinderTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(sphere.volume(10) == 4188.7902047864)

    def test_volume2(self):
        assert(sphere.volume(15) == 14137.166941154)

    #failing test
    #def test_volume3(self):
        #assert(cylinder.volume(10,1000) == 0)


if __name__ == '__main__':
    unittest.main()
