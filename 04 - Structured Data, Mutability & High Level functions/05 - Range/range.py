#   Date: 2020/11/19
#   Author: Luis Marquez
#   Description:
#           This is a simple program to learn how to use ranges
##

import random


#print_l(): This function print a list
def print_rand_l():
    l = []
    l = fill_list()
    for n in range(0, 10, 1):
        print(f"N({n}) = {l[n]}\n")


#fill_list(): On this function we use ranges to run over the the list with random numbers
def fill_list():
    _list = []

    for n in range(0,10,1):
        _list.append(round(((((n+1)*(random.randint(1,2048)/1024))*5)/2), 2))
    
    return _list


#run(): This functions runs all the other functions written on this program
def run():
    print_rand_l()


#main(): This is the main function of the program
if __name__ == "__main__":
    run()