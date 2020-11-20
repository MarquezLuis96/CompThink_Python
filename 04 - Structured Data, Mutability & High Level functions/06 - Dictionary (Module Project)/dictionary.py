#   Date: 2020/11/20
#   Author: Luis Marquez
#   Description:
#           This is a program that is the project of the module.
#           On this program we will code a dectionary in which you can add, modify and change de meaning of a word
# #


#dictionary: This is a global variable in which we will store all the words that the user type with it's meaning
dictionary = {
}


#print_d(): This is a function that prints the whole dictionary
def print_d():
    print(f"Printing dictionary...\n")
    for word, means in dictionary.items():
        print(f"{word}:\t{means}\n")


#add_w(): This function adds a word with it's meaning
def add_w():
    word = input("\nType the new word: ")
    if (dictionary.get(word,False) == False):
        meaning = input(f"\nType the meaning of '{word}': ")
        dictionary[word] = meaning
    else:
        print(f"\nThe word '{word}'' already exist on this dictionary...")


#change_k(k, nk): This function change the name of a word (k) for another (nk)
def change_k(k, nk):
    dictionary[nk] = dictionary.pop(k)


#change_k(k, nk): This function change the name of a word (k) for another (nk)
def change_m(k, nm):
    dictionary[k] = nm


#change_w(): This function will verify if the word is on the dictionary to:
# opt = 1 -> change the key
# opt = other value -> change the meaning of the word
def change_w(opt):
    k = input(f"Type the key you want to change: ")
    if (dictionary.get(k, True)):
        if opt == 1:
            nk = input(f"Type the new key: ")
            change_k(k, nk)
        else:
            nm = input(f"Type the new meaning: ")
            change_m(k, nm)
    else:
        print(f"'{k}' wasn't found on the dictionary")


#run(): This is a function in which we will run all the other functions written on the program
def run():
    add_w()
    add_w()
    add_w()
    add_w()
    print_d()
    change_w(1)
    print_d()
    change_w(0)
    print_d()


#main(): This is the main function
if __name__ == "__main__":
    run()