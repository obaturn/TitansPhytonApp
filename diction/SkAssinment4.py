def odd_numbers(number):
    sum_of_odd_numbers = 0
    for values in number:
        if values % 2 != 0:
            sum_of_odd_numbers += values
    return sum_of_odd_numbers  

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_total = odd_numbers(my_list)
print(my_list_total)

