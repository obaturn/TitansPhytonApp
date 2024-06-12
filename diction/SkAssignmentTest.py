import unittest
from SkAssignment import get_random_numbers
from SkAssigment2 import my_len
from SkAssignment3 import even_position
from SkAssinment4 import odd_numbers
from SkAssignment5 import multiplying_of_third_element
from SkAssignment6 import calculating_average_of_list
from SkAssigmnent7 import find_the_smallest_index
from SkAssignment8 import find_the_largest_number_in_the_index

class MyTestCase(unittest.TestCase):
    def test_get_random_numbers(self):
        self.assertEqual(get_random_numbers(), [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
                         )
    def test_my_len(self):
        nuu = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
        self.assertEqual(my_len(nuu), 10)
    def test_even_position(self):
        number = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
        self.assertEqual(even_position(number),168)
    def test_odd_numbers(self):
        nums = [32, 18, 24, 41, 16, 45, 31, 50, 22, 6]
        self.assertEqual(odd_numbers(nums), 117)
    def test_multiplying_of_third_element(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(multiplying_of_third_element(values),28)
    def test_calculating_average_of_list(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(calculating_average_of_list(values),5.0)
    def test_find_the_smallest_index(self):
        my_list =[8,7,7,4,2,6,7,8,9]
        self.assertEqual(find_the_smallest_index(my_list),2)
    def test_find_the_largest_number_in_the_index(self):
        my_list =[1,2,3,4,5,6,7,8,9]
        self.assertEqual(find_the_largest_number_in_the_index(my_list),9)
if __name__ == '__main__':
    unittest.main()


