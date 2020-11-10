import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Dragos', 'Neata', 50000)
        self.emp_2 = Employee('Alexandru', 'Neata', 60000)

    def tearDown(self):
        print('tearDwon\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Dragos.Neata@email.com')
        self.assertEqual(self.emp_2.email, 'Alexandru.Neata@email.com')

        self.emp_1.first = 'Gabi'
        self.emp_2.first = 'Radu'

        self.assertEqual(self.emp_1.email, 'Gabi.Neata@email.com')
        self.assertEqual(self.emp_2.email, 'Radu.Neata@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Dragos Neata')
        self.assertEqual(self.emp_2.fullname, 'Alexandru Neata')

        self.emp_1.first = 'Gabi'
        self.emp_2.first = 'Radu'

        self.assertEqual(self.emp_1.fullname, 'Gabi Neata')
        self.assertEqual(self.emp_2.fullname, 'Radu Neata')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Neata/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Neata/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()


