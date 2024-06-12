import unittest
from tupleAssigment import (creating_of_an_empty_tuple,create_tuple_with_numbers_and_adding_them,
                            adding_of_all_the_numbers,
                            find_the_sum_of_odd_element,find_the_sum_of_even_element,find_the_smallest_and_largest_in_the_tuple_and_add,
                            unpacking_of_the_first_five_element)


class tupleAssignment(unittest.TestCase):
    def test_creating_of_an_empty_tuple(self):
        result = ()
        self.assertEqual(creating_of_an_empty_tuple(), ())
    def test_create_tuple_with_numbers_and_adding_them(self):
        expected = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
        result = create_tuple_with_numbers_and_adding_them()
        self.assertEqual(create_tuple_with_numbers_and_adding_them(),expected)
    def test_adding_of_all_numbers(self):
        result = adding_of_all_the_numbers((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
        self.assertEqual(result,210)
    def test_find_the_sum_of_odd_element(self):
        result = find_the_sum_of_odd_element((1, 3, 5, 7, 9))
        self.assertEqual(result,25)
    def test_find_the_sum_of_even_element(self):
        result = find_the_sum_of_even_element((1,2,3,4,5,6,7,8,9,10))
        self.assertEqual(result,30 )
    def test_find_the_smallest_and_largest_in_the_tuple_and_add(self):
        result = find_the_smallest_and_largest_in_the_tuple_and_add((4,2,3,4,5,6,7,8,9))
        self.assertEqual(result , 11)
    def test_unpacking_of_the_first_five_element(self):

        my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        result = unpacking_of_the_first_five_element()
        expected = (1, 2, 3, 4, 5)
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()





if __name__ == '__main__':
    unittest.main()
