#   Date: 2020/11/17
#   Author: Luis Marquez
#   Description:
#           This is a simple program to learn how data structures can store functions inside
# #


#on_data_S: This is a function that store a functions on a data structure
def on_data_S(num):
    operations = [abs, float]

    result = []

    for operation in operations:
        result.append(operation(num))
    
    return result


#run: on this function we will run the other functions written on this program
def run(): 
    num = int(input(f"type a number: "))
    print(on_data_S(num))


#main: This is the main function
if __name__ == "__main__":
    run()