def find_the_largest_number_in_the_index(numbers):

    max_number = numbers[0]


    for value in numbers:
        if value > max_number:
            max_number = value

    return max_number

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_answer = find_the_largest_number_in_the_index(my_list)
print(my_answer)
