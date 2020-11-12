#   Date: 2020/11/05
#   Author: Luis Marquez
#   Description:
#           ##
# 


#
def square():
    #DEFINING EPSILON (MARGIN OF ERROR)
    epsilon = 0.01

    #DEFINING STEP (HOW MUCH I CAN APPROXIMATE IN EACH STEP)
    step = epsilon**2

    #DEFINFING ANSWER
    answer = 0.0

    #DEFINING OBJECTIVE (TO CALCULATE SQUARE)
    objective = int(input(f"\nType an integer number.\nNumber: "))
    print(f"\n")

    while ((abs(answer**2 - objective) >= epsilon) and (answer <= objective)):
        # print(f"abs(answer**2 - objective) = {abs(answer**2 - objective)}\nanswer = {answer}\n")
        answer += step


    if (abs(answer**2 - objective) >= epsilon):
        print(f"We didn't find the square of the number {objective}")
    else:
        print(f"The square of {objective} is {answer}")


#RUN(): ON THIS FUNCTION WE'LL RUN OUR CODE
def run():
    square()


#MAIN(): MAIN FUNCTION
if __name__ == "__main__":
    run()