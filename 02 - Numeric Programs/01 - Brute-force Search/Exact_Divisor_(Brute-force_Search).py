#   Date: 2020/11/05
#   Author: Luis Marquez
#   Description:
#           This program evaluates an exact divisor for a number using
#           the Brute-Force Search Algorithm, modularizing the solution
# 

#validate
def validate():
    pass

#e_divisor():  It's the foundamental function of the program
def e_divisor():
    #candidate
    candidate = 1
    #number to evaluate
    number = int(input(f"\nType an integer number to find its exact divisor.\nNumber:"))
    print(f"\n")

    if (number == 0):
        print(f"0 doesn't have a divisor")
    else:
        while (candidate <= number):
            if (number%candidate == 0):
                print(f"{number}/{candidate} = {number/candidate}\n")
            candidate += 1


#run
def run():
    e_divisor()

#main()
if __name__ == "__main__":
    run()