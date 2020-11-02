# Date: 2020/11/02
# Author: Luis Marquez
# Description: This is a simple program that says which is the olderof two users


#Asking the first user data
user1_name = str(input(f'\nType the name of the first user: '))
user1_age = int(input(f'\nType how old is {user1_name}: '))


#Asking the first user data
user2_name = str(input(f'\nType the name of the second user: '))
user2_age = int(input(f'\nType how old is {user2_name}: '))


#Verifying who's older
if (user1_age > user2_age):
    #Printing that user1 is older than user2
    print(f'\n{user1_name} is older than {user2_name}')
elif (user2_age > user1_age):
    #Printing that user2 is older than user1
    print(f'\n{user2_name} is older than {user1_name}')
else:
    #Printing that user1 and user2 are the same age
    print(f'\n{user1_name} & {user2_name} are the same age')