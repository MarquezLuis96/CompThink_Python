# Date: 2020/11/02
# Author: Luis Marquez
# Description: A simple program that evaluates conditions with if-elif-else

num1 = int(input("\nType a number: "))
num2 = int(input("\nType a number: "))

#Evaluating wich number is greater
if (num1 > num2):
    #Printing result
    print(f'\n{num1} is greater than {num2}')
elif (num2 > num1):
    #Printing result
    print(f'\n{num2} is grater than {num1}')
#Default case
else:
    #Printing result
    print(f'\nThe numbers are the same')