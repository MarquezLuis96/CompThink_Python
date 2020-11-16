#   Date: 2020/11/16
#   Author: Luis Marquez
#   Description: On this simple program i'll learn how to use recursion
# #


#factorial: Function that calculate a number factorial using recursion
def factorial(n):
    """
    On this function we'll calculate the factorial of a number n using recursion
    """

    if n == 1:
        #base case. Avoiding the infinity loop
        return 1
    else:
        #calling itself
        result = ((n) * (factorial(n-1)))
        #returning the value of n!
        return result


#RUN: On this function we will run the functions of our program
def run():
    """
    On this function we will run the different functions written in our program
    """
    n = int(input(f"\ntype a number: "))
    print(f"\n{n}! = {factorial(n)}\n")


#MAIN: This is the main function
if __name__ == "__main__":
    """
    This is the main funtion
    """
    run()