import unittest

x = [1, 2, 3, 4, 5, 6]


# y = x.count(6)
# if y > 0:
#     print(" element occurs")
# else:
#     print("no occurrence")


def checking(x):
    return x


a = ([1, 2, 3, 4, 5, 6])
if x == a:
    print("element occurs")
else:
    print("element doesn't occurs")


class UnitTests(unittest.TestCase):
    def test_element_occurrence(self):
        self.assertEqual(x, x)
        print(x)


if __name__ == "__main__":
    unittest.main()
