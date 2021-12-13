import unittest
from password_strength.tests import BadPassword
from password_strength import PasswordStats


class BadPasswordTestCase(unittest.TestCase):

    def test_should_return_false_when_bad_password(self):
        password_test = BadPassword()
        self.assertEqual(password_test.test(PasswordStats("hello")), False)
        self.assertEqual(password_test.test(PasswordStats("world")), False)
        self.assertEqual(password_test.test(PasswordStats("ginger")), False)
        self.assertEqual(password_test.test(PasswordStats("password")), False)
        self.assertEqual(password_test.test(PasswordStats("123")), False)

    def test_should_return_true_when_good_password(self):
        password_test = BadPassword()
        self.assertEqual(password_test.test(PasswordStats("asdfasdfaslk;j;asa")), True)
