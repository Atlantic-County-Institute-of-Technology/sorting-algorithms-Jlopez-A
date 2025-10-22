
import random
import os
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
# from selection_sort import selection_sort

numbers = [random.randint(1,100) for i in range(10)]


def main_menu():
    print(
        "[-] 0.Exit \n"
        "[-] 1.Bubble sort \n"
        "[-] 2.Insertion sort \n"
        "[-] 3.Selection sort")
    try:
        # user inputs option #
        selection = int(input("please select an option:"))
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("invalid")
        main_menu()

    if selection == 1:
        print(numbers)
        print(bubble_sort(numbers))
    elif selection == 2:
        print(numbers)
        print(insertion_sort(numbers))
    # elif selection == 3:

main_menu()


# print(numbers)
# #
# # outer_pass = 0
# # inner_pass = 0
# #
# print(f"sorted values {bubble_sort(numbers)}")
