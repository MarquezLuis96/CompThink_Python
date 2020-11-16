#   Date: 2020/11/16
#   Author: Luis Marquez
#   Description:
#           A simple program to learn about fibonacci with recursion
# #


#fibo: This function is called when we will calculate the fibonacci serie
def fibo(iterations):
    """
        This function calculate the fibonacci serie, calling itself many times iterations says
    """
    if (iterations == 0 or iterations == 1):
        return 1
    else:
        print(f"iteration = {iterations} -> {iterations - 1} + {iterations - 2} = {(iterations-1)+(iterations-2)}")
        return (fibo(iterations-1) + fibo(iterations-2))


#run: On this function we will run all the function written on the program
def run():
    """
        On this function we will run our functions
    """
    iterations = int(input(f"\nType the number of iteration you want the program do: "))
    print(f"\nThe number of fibonacci series corresponding to iteration {iterations} is {fibo(iterations)}\n")


#Main: Main function
if __name__ == "__main__":
    """
        This is the main function
    """
    run()