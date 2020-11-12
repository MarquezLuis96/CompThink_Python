#   Date: 2020/11/05
#   Author: Luis Marquez
#   Description: 
#           This is a demostration of brute-force Search algorithm, in this program we'll calculate
#           an exact square root of a number 'n' -> Objective


#run
def run():
    answer = 0
    objective = int(input(f"Type an integer: "))

    while answer**2 < objective:
        #print(answer)
        answer += 1
    
    if answer**2 == objective:
        print(f"\nThe square root of {objective} is {answer}\n")
    else:
        print(f"\n{objective} doesn't have an exact square root\n")


#main
if __name__ == "__main__":
    run()