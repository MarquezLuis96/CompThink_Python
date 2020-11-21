#   Date: 2020/11/21
#   Author: Luis Marquez
#   Description:
#           This is a simple program to learn how does it black-box works
##

#import
import unittest


def plus(n1, n2):
    return n1+n2


#class cajanegra
class black_box_test(unittest.TestCase):
    def test_plus_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = plus(num_1, num_2)

        self.assertEqual(result, 15)


    def test_plus_two_negatives(self):
        num1 = -10
        num2 = -7

        result = plus(num1, num2)

        self.assertEqual(result, -17)


#run(): This function runs all the other functions written on the program
def run():
    unittest.main()


#main(): This is the main function of the program
if __name__ == "__main__":
    run()