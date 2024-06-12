def my_len(numbers):
    count = 0
    for _ in numbers:
        count += 1
    return count
my_list = [1, 2, 3, 4, 5]
length_of_list = my_len(my_list)
print(length_of_list)
