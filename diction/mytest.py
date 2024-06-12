import unittest
from account import account:


class account(unittest.TestCase):
    def test_that_stack_can_add_element(self):
        stack = myStack()
        stack.add_to_stack("semicolon.africa")
        stack.add_to_stack("google.com")
        self.assertEqual(len(stack.stack),2) # add assertion here


if __name__ == '__main__':
    unittest.main()
