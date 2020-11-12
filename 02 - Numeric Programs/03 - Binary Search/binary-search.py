#   Date: 2020/11/12
#   Author: Luis Marquez
#   Description:
#           This is a simple program in which the binary search will be implemented to calculate a square root result
# 


#BINARY_SEARCH(): This function realize a binary search
def binary_search():
    #objective:  The number in which the root will be calculated
    objective = int(input(f"\nType a number: "))
    print(f"\n")
    
    #epilson: Margin of error
    epsilon = 0.01
    
    #low: The lowest number of the current binary search range
    low = 0.0
    
    #high: The highest number of the currente binary search range
    high = max(1.0, objective)
    
    #answer:
    answer = ((high + low)/(2))
    
    #while: on this wile we will do a walk throught, cutting the numerical set in half
    while (abs(answer**2 - objective) >= (epsilon)):
        print(f"Low={round(low, 2)} \t high={round(high, 2)} \t Answer={round(answer, 2)}\n")
        if (answer**2 < objective):
            low = answer
        else:
            high = answer
        
        answer = ((high + low)/(2))
    
    #printing the answer
    print(f"The square root of {objective} is {answer}")


#RUN(): On this function the program run
def run():
    binary_search()


#MAIN: Main function
if __name__ == "__main__":
    run()