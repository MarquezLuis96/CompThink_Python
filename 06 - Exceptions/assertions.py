#   Date: 2020/11/22
#   Author: Luis Marquez
#   Description:
#           A simple program to learn how to use assertions in python
##


#first_letters(): This is a function that return in a list all the first letters of a word list
def first_letters(list_pal):
    first_letters = []

    for pal in list_pal:
        assert type(pal) == str, f"The word {pal} is not an str"
        assert len(pal) > 0 , f"The len can't not be 0"
        first_letters.append(pal[0])

    return first_letters


#run(): This functions runs all the other functions written on this program.
def run():
    _list = {
        "Lebanon",
        "Uruguay",
        "Irlanda",
        "Servia",
        "Autralia",
        "Nueva Zelanda",
        "Turkey",
        "Omán",
        "Noruega",
        "Italia",
        "Orden de Malta"
    }

    print(first_letters(_list))


#main(): Main function
if __name__ == "__main__":
    run()