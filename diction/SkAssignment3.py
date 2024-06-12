def even_position(numbers):
    sum_of_evens = 0

    for value in numbers:
        if value % 2 == 0:
            sum_of_evens += value

    return sum_of_evens


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_even_numbers = even_position(my_list)
print(my_even_numbers)
