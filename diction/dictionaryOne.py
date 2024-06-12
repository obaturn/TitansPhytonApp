def creating_of_an_empty_dictionary():
    empty_dict = {}
def create_student_records():
    student_records = {}
    for _ in range(10):
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_records[student_name] = student_age
    return student_records
def sorting_of_the_keys_in_the_dictionary(my_dict):
    sorted_dict = dict(sorted(my_dict.items()))
    return sorted_dict
def sorting_of_the_values_in_the_dictionary(my_dict):
    sorted_dict = {}
