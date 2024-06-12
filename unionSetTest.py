import unittest
from unionSet import create_union_of_two_sets, check_either_first_set_is_subset_to_the_secon_set, \
    remove_element_of_the_first_set, find_the_max_and_min_in_the_second_set


class unionSet(unittest.TestCase):
    def test_create_union_of_two_setsself(self):
        set1 = {1,3,4}
        set2 = {5,2,6}
        union_result = create_union_of_two_sets(set1, set2)
        expected_union = {1, 2, 3, 4, 5,6}
        self.assertEqual(union_result, expected_union)
    def test_check_either_first_set_is_subset_to_the_secon_set(self):
        set1 ={1,2,5,7}
        set2 = {3,4,}
        self.assertFalse(check_either_first_set_is_subset_to_the_secon_set(set1,set2))

        set1 ={1,2,3}
        set2 = {1,2,3,4,5}
        self.assertTrue(check_either_first_set_is_subset_to_the_secon_set(set1,set2))
    def test_remove_element_of_the_first_set(self):
        set1 ={1,2,3}
        set2 = {1,2,3,4,5}
        original_set = remove_element_of_the_first_set(set1-set2)
        result_set = (original_set)
        self.assertEqual(result_set, set())
    def test_find_max_min_in_second_set(self):
        set1 = {1,2,3}
        set2 = {1,2,3,4,5}
        max_value , min_value = find_the_max_and_min_in_the_second_set(set1,set2)
        self.assertEqual(max_value, 5)
        self.assertEqual(min_value,1)


if __name__ == '__main__':
    unittest.main()
