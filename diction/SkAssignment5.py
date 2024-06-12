def multiplying_of_third_element(index_numbers):
    values = 0
    product_numbers = 1

    for values in range(0, len(index_numbers), 3):
        product_numbers *= index_numbers[values]
    return product_numbers

index_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_index_numbers = multiplying_of_third_element(index_numbers)
print(my_index_numbers)
