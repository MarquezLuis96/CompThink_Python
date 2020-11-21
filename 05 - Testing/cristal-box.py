#   Date: 2020/11/21
#   Author: Luis Marquez
#   Description: 
#           This is a simple program to learn how to use cristal boxes in python
##


#import
import unittest


#is_older(): Verify if the person is older
def is_older(age):
    if age >= 18:
        return True
    else:
        return False


#Class
class cristal_box_test(unittest.TestCase):
    def test_is_older(self):
        age = 20

        result = is_older(age)
    

    def test_is_younger(self):
        age = 15
        result = is_older


#run(): This function runs all the other functions in the program
def run():
    unittest.main()


#main(): This is the main function of the program
if __name__ == "__main__":
    run()