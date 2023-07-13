#!/usr/bin/python3
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_email(self):
        emp_1 = Employee('corey', 'schafer', 20000)
        emp_2 = Employee('sue', 'smith', 23444)

        self.assertEqual(emp_1.email, 'corey.schafer@gmail.com')
        self.assertEqual(emp_2.email, 'sue.smith@gmail.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.schafer@gmail.com')
        self.assertEqual(emp_2.email, 'Jane.smith@gmail.com')

    def test_fullname(self):
        emp_1 = Employee('corey', 'schafer', 20000)
        emp_2 = Employee('sue', 'smith', 23444)

        self.assertEqual(emp_1.fullname, 'corey schafer')
        self.assertEqual(emp_2.fulname, 'sue smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John schafer')
        self.assertEqual(emp_2.fullname, 'Jane smith')

    def test_apply_raise(self):
        emp_1 = Employee('corey', 'schafer', 20000)
        emp_2 = Employee('sue', 'smith', 23444)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52000)
        self.assertEqual(emp_2.pay, 32444)

if __name__ == "__main__":
    unittest.main()
