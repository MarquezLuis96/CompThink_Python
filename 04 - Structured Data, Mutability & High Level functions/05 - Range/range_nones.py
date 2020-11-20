#   Date: 2020/11/20
#   Author: Luis Marquez
#   Description:
#           This is a program in which we will gonna use the numbers of a range and store in a list only the none numbers
# #


#verify(): This is a function that verify if the number is none
def verify(n):
    if(n%2 != 0):
        return True
    else:
        return False


#store_nones(): This funtion use a range and store only the none numbers
def store_nones(n):
    _list = []
    for i in range(0, n, 1):
        if (verify(i)):
            _list.append(int(i))
    
    return _list


#run(): This is a function in which we will run all te other functions on this program
def run():
    n = int(input(f"\nType the upper range of the number you want to evaluate: "))
    print(f"\n")
    none_list = store_nones(n)
    print(f"{none_list}")


#main():
if __name__ == "__main__":
    run()