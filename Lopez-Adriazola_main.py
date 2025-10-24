
import random
import os
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

# Lets users pick how they want their list sorted
def options(x,y,z):
    numbers = [random.randint(x,y) for i in range(z)]
    print(
        "[-] 0.Back \n"
        "[-] 1.Bubble sort \n"
        "[-] 2.Insertion sort \n"
        "[-] 3.Selection sort")
    try:
        # user inputs option #
        selection = int(input("please select an option:"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if selection == 1:
            print(numbers)
            print(bubble_sort(numbers))
        elif selection == 2:
            print(numbers)
            print(insertion_sort(numbers))
        elif selection == 3:
            print(numbers)
            print(selection_sort(numbers))
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("invalid")




def main_menu():

    while True:
        try:
            # allows the user to choose the range,max number, min number for the list
            find_range = int(input("how many numbers do you want in your sort? :"))
            find_max = int(input("whats the highest number you'd like? :"))
            find_min = int(input("whats the lowest number you'd like? :"))
            os.system('cls' if os.name == 'nt' else 'clear')
            # makes it so no negative number can be chosen
            if find_range > -1:
                options(find_min,find_max,find_range)

            else:
                print("range needs to be a positive number")

        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("invalid input")


main_menu()