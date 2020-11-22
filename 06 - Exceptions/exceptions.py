#   Date: 2020/11/21
#   Author: Luis Marquez
#   Description:
#           This is a program in which i'll learn how to handle exceptions in python
# #


#div_list_elements(): This functions divide all the elements that belong to a list
def div_list_elements(_list, div):
    try:
        return[i / div for i in _list]
    except ZeroDivisionError as e:
        print(f"{e}")
        return _list


#run(): This function runs all the other functions written on this program
def run():
    
    _list = list(range(0, 10, 1))
    div = 0

    print(div_list_elements(_list, div))


#main(): This is the main function of the program
if __name__ == "__main__":
    run()