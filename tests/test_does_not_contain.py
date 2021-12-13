import unittest
from password_strength.tests import DoesNotContain
from password_strength import PasswordStats


class DoesNotContainTestCase(unittest.TestCase):

    def test_should_return_false_when_illegal_phrase_present(self):
        password_test = DoesNotContain(["abc"])
        self.assertEqual(password_test.test(PasswordStats("abc123")), False)
        self.assertEqual(password_test.test(PasswordStats("abc")), False)
        self.assertEqual(password_test.test(PasswordStats("124abc")), False)
        self.assertEqual(password_test.test(PasswordStats("124abccba")), False)
        self.assertEqual(password_test.test(PasswordStats("abcabcabc")), False)

        password_test = DoesNotContain(["apple"])
        self.assertEqual(password_test.test(PasswordStats("elppa")), False)

        password_test = DoesNotContain(["fred"])
        self.assertEqual(password_test.test(PasswordStats("fred1")), False)
        self.assertEqual(password_test.test(PasswordStats("1fred")), False)

    def test_should_return_true_when_illegal_phrase_not_present(self):
        password_test = DoesNotContain(["abc"])
        self.assertEqual(password_test.test(PasswordStats("123")), True)
        self.assertEqual(password_test.test(PasswordStats("3")), True)
        self.assertEqual(password_test.test(PasswordStats("a1b2c3")), True)
        self.assertEqual(password_test.test(PasswordStats("bac")), True)
        self.assertEqual(password_test.test(PasswordStats("bca")), True)
        self.assertEqual(password_test.test(PasswordStats("Abc")), True)
        self.assertEqual(password_test.test(PasswordStats("ABC")), True)
        self.assertEqual(password_test.test(PasswordStats("AbC")), True)
        self.assertEqual(password_test.test(PasswordStats("abC")), True)

    def test_should_work_with_special_characters(self):
        password_test = DoesNotContain(["!@#Abc"])
        self.assertEqual(password_test.test(PasswordStats("!@#Abcasdlasd;l")), False)
        self.assertEqual(password_test.test(PasswordStats("!@#asdlasd;l")), True)

    def test_should_not_care_about_case(self):
        password_test = DoesNotContain(["abc"], False)
        self.assertEqual(password_test.test(PasswordStats("Abc")), False)
        self.assertEqual(password_test.test(PasswordStats("ABC")), False)
        self.assertEqual(password_test.test(PasswordStats("abc")), False)
        self.assertEqual(password_test.test(PasswordStats("aBc")), False)
        self.assertEqual(password_test.test(PasswordStats("asdfas234")), True)

        password_test = DoesNotContain(["apple"], False)
        self.assertEqual(password_test.test(PasswordStats("ELPPA")), False)

    def test_should_work_with_multiple_illegals(self):
        password_test = DoesNotContain(["abc", "123"])
        self.assertEqual(password_test.test(PasswordStats("abc")), False)
        self.assertEqual(password_test.test(PasswordStats("123")), False)
        self.assertEqual(password_test.test(PasswordStats("abc123")), False)
        self.assertEqual(password_test.test(PasswordStats("a1b2c3")), True)
