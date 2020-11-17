#   Date: 2020/11/017
#   Author: Luis Marquez
#   Description:
#           This is a simple program to learn about how to use a function like an object
# #


#mult_x_2: This function return the n number multiplied by 2
def mul_x_2(n):
    """
        This function return the n number multiplied by 2

        The n number is the number that will be rmultiplied

        This function return the value after the operation
        Example: mult-x_2(2) -> 4
    """
    return n*2


#plus_x_2: This function return the n number multiplied by 2
def plus_x_2(n):
    """
        This function return the n number plus 2

        The n number is the number that will be plused

        This function return the value after the operation
        Example: plus_x_2(3) -> 5
    """
    return n+2


#operation: This function make the operation
def op(f, numbers):
    results = []
    for number in numbers:
        result = f(number)
        results.append(result)
    return results


#Run: This is the function in which we'll run other functions written on this program
def run():
     """
         This funtion run other functions written on our program

         Doesn't have any parameter

         Doesn't return anything
     """


# #Main: This is the main function of the program
if __name__ == "__main__":
     run()