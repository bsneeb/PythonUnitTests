import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('Set Up')
        self.emp1 = Employee('Brady', 'Neeb', 50000)
        self.emp2 = Employee('John', 'Doe', 60000)

    def tearDown(self):
        print('Tear down\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email, 'Brady.Neeb@email.com')
        self.assertEqual(self.emp2.email, 'John.Doe@email.com')

        self.emp1.first = 'Mike'
        self.emp2.first = 'Joe'

        self.assertEqual(self.emp1.email, 'Mike.Neeb@email.com')
        self.assertEqual(self.emp2.email, 'Joe.Doe@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp1.fullname, 'Brady Neeb')
        self.assertEqual(self.emp2.fullname, 'John Doe')

        self.emp1.first = 'Mike'
        self.emp2.first = 'Joe'

        self.assertEqual(self.emp1.fullname, 'Mike Neeb')
        self.assertEqual(self.emp2.fullname, 'Joe Doe')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
