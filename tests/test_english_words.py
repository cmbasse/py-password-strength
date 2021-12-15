import unittest
from password_strength.tests import EnglishWord
from password_strength import PasswordStats


class EnglishWordTestCase(unittest.TestCase):

    def test_should_return_false_when_is_dictionary_word(self):
        password_test = EnglishWord()
        self.assertEqual(password_test.test(PasswordStats("apple")), False)
        self.assertEqual(password_test.test(PasswordStats("applE")), False)
        self.assertEqual(password_test.test(PasswordStats("appLe")), False)
        self.assertEqual(password_test.test(PasswordStats("apPle")), False)
        self.assertEqual(password_test.test(PasswordStats("aPple")), False)
        self.assertEqual(password_test.test(PasswordStats("Apple")), False)
        self.assertEqual(password_test.test(PasswordStats("bat")), False)
        self.assertEqual(password_test.test(PasswordStats("bridge")), False)
        self.assertEqual(password_test.test(PasswordStats("Fred")), False)
        self.assertEqual(password_test.test(PasswordStats("Abraham")), False)

    def test_should_return_true_when_not_dictionary_word(self):
        password_test = EnglishWord()
        self.assertEqual(password_test.test(PasswordStats("@pple")), True)
        self.assertEqual(password_test.test(PasswordStats("appl3")), True)
        self.assertEqual(password_test.test(PasswordStats("Fr3d")), True)
        self.assertEqual(password_test.test(PasswordStats("thecatjumpedoverthehat")), True)
