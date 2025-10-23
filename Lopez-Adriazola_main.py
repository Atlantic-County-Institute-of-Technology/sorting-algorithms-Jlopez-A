
import random
import os
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


def options(x,y,z):
    numbers = [random.randint(x,y) for i in range(z)]
    print(
        "[-] 0.Exit \n"
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
        print("invalid")




def main_menu():
    try:
        find_range = int(input("howmany numbers:"))
        find_max = int(input("highest number:"))
        find_min = int(input("lowest number:"))
        options(find_min,find_max,find_range)

    except:
        print("invalid")
    main_menu()



main_menu()