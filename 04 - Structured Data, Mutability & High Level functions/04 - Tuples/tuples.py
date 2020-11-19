#   Date: 2020/11/19
#   Author: Luis Marquez
#   Description:
#           This is a simple program to learn how to use tuples in python
# #


#tuple: This is a inmutable data structure
my_tuple = ("1) +","2) -","3) x","4) /")


#run(): This function runs all the other functions written on this program
def run():
    option = int(input(f"Options:\n\t{my_tuple[0]}\n\t{my_tuple[1]}\n\t{my_tuple[2]}\n\t{my_tuple[3]}\nType: "))

    if option == 1:
        print(f"Your option was: {my_tuple[0]}")
    elif option == 2:
        print(f"Your option was: {my_tuple[1]}")
    elif option == 3:
        print(f"Your option was: {my_tuple[2]}")
    else:
        print(f"Your option was: {my_tuple[3]}")


#main(): This is the main function of the program
if __name__ == "__main__":
    run()