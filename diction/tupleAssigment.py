def creating_of_an_empty_tuple():
    return ()

def create_tuple_with_numbers_and_adding_them():
    numbers = range(1, 21)

    numbers_tuple = tuple(numbers)

    return numbers_tuple
def adding_of_all_the_numbers(tuple_collection):
    total_sum = 0
    for num in tuple_collection:
        total_sum += num
    return total_sum
def find_the_sum_of_odd_element(numbers):
    odd_number = 0
    for number in numbers:
        if number % 2 != 0:
            odd_number += number
    return odd_number
def find_the_sum_of_even_element(numbers):
    even_number = 0
    for number in numbers:
            if number % 2 == 0:
                even_number += number
    return even_number
def find_the_smallest_and_largest_in_the_tuple_and_add(numbers):
    largest_number = 0
    total_sum = 0

    for value in numbers:
        if value > largest_number:
            largest_number = value

    my_tuple = (3, 2, 4, 5, 5, 6, 7, 8, 9)
    smallest_number = min(my_tuple)

    total_sum = largest_number + smallest_number

    return total_sum

def unpacking_of_the_first_five_element():
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    first_number, second_number, third_number, fourth_number, fifth_number = my_tuple
    return first_number, second_number, third_number, fourth_number, fifth_number






