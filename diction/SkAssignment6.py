def calculating_average_of_list(numbers):
    total = 0
    for value in numbers:
        total += value
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
average = calculating_average_of_list(my_list)
print(average)


