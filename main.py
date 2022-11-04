# Author: Mason Hernandez
# Date: 11/4/2022
# Description: Will look through all pass winning numbers and select 5 most comment numbers and 1 mega number.
# Share winnings if you win ;)

import pandas as pd
from collections import Counter

# Create two empty lists to hold maga and winning prediction
numbers_to_play = []
mega_number_to_play = []


def convert_past_winning_numbers_to_list():
    file_data = pd.read_excel("one.xlsx", "Sheet1")
    list_of_rows = file_data.values.tolist()  # Create a list that has list's of past numbers
    list_of_numbers = [] # empty list to hold all past winning numbers in single list
    for row in list_of_rows:  # iterate through main list, that has list for each set of 5 past winning numbers
        for num in row:  # iterate through each list holding 5 past winning numbers
            list_of_numbers.append(num)  # append winning numbers to create 1 single list with all past winning numbers
    return list_of_numbers  # returns single list with all previous winning numbers


def convert_past_winning_maga_numbers_to_list(): # This function does same as above but for Mega past numbers on sheet2
    file_data = pd.read_excel("one.xlsx", "Sheet2")
    list_of_rows = file_data.values.tolist()
    list_of_maga = []
    for row in list_of_rows:
        for mega in row:
            list_of_maga.append(mega)
    return list_of_maga


def future_winners(past_winners):  # parameter will accept single list with all past winning numbers
    counter = Counter(past_winners)  # pass single winning number list to Counter class
    most_common = counter.most_common(5)  # use .most_common() method and pass number you want to determine
    # will return a tuple (8, 6)  first number is common and second is amount of times it appears

    for number, count in most_common:  # for each tuple with the highest number
        numbers_to_play.append(number)  # append the 5 most common numbers to our first empy list
    numbers_to_play.sort()  # Sort the five most common numbers from small to large
    print(f"Super lotto Numbers to Play: {numbers_to_play}")  # print the list of most common possible winning numbers


def future_maga_numbers(past_mega):  # Does same as above but for Mega
    counter = Counter(past_mega)
    most_common_maga = counter.most_common(1)

    for number, count in most_common_maga:
        mega_number_to_play.append(number)
    mega_number_to_play.sort()
    print(f"Mega Numbers to Play: {mega_number_to_play}")


past_numbers = convert_past_winning_numbers_to_list()
future_winners(past_numbers)


past_mega_numbers = convert_past_winning_maga_numbers_to_list()
future_maga_numbers(past_mega_numbers)

