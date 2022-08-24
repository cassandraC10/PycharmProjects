import unittest

List1 = ["a", "b", "c"]
List2 = [1, 2, 3]

concatenate = List1 + List2
print(concatenate)


#  I wasted time on this because I didn't know I could join a string and int together

class UnitTests(unittest.TestCase):
    def test_concatenate(self):
        actual = concatenate
        self.assertEqual(actual, concatenate)


if __name__ == "__main__":
    unittest.main()
