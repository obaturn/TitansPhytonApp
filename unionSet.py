def create_union_of_two_sets(set1,set2):
    return set1.union(set2)
def check_either_first_set_is_subset_to_the_secon_set(set1, set2):
    return set1.issubset(set2)
def remove_element_of_the_first_set(my_set):
    my_set.clear()
    return my_set
def find_the_max_and_min_in_the_second_set(set1, set2):
    max_value = max(set2)
    min_value = min(set2)
    return max_value, min_value


