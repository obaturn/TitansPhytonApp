import unittest

from dictionaryOne import create_student_records, sorting_of_the_keys_in_the_dictionary


class dictionaryOne(unittest.TestCase):
    def test_creating_of_an_empty_dictionary(self):
        my_dict = {}
        self.assertTrue(bool , my_dict)
    def test_value_types(self):
        student_dict = create_student_records()
        for name, age in student_dict.items():
            self.assertIsInstance(name, str)
            self.assertIsInstance(age, int)
    def test_sorting_of_keys(self):
        my_dict = {'b': 2, 1: 'a', 4.5: 'd', 3: 'c'}
        result = sorting_of_the_keys_in_the_dictionary(my_dict)
        expected_result = {1: 'a', 3: 'c', 'b': 2, 4.5: 'd'}
        self.assertEqual(result, expected_result)




if __name__ == '__main__':
    unittest.main()
