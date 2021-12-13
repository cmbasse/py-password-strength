import unittest
from password_strength.tests import TrivialVariant
from password_strength import PasswordStats


class NotTrivialTestCase(unittest.TestCase):

    def test_should_return_false_when_illegal_phrase_present(self):
        password_test = TrivialVariant("apple")
        self.assertEqual(password_test.test(PasswordStats("@pple")), False)
        self.assertEqual(password_test.test(PasswordStats("*pple")), False)
        self.assertEqual(password_test.test(PasswordStats("*ppl3")), False)
        self.assertEqual(password_test.test(PasswordStats("Appl3")), False)
        self.assertEqual(password_test.test(PasswordStats("APPLE")), False)

        password_test = TrivialVariant("character")
        self.assertEqual(password_test.test(PasswordStats("ch@racter")), False)
        self.assertEqual(password_test.test(PasswordStats("ch*racter")), False)

        password_test = TrivialVariant("fred")
        self.assertEqual(password_test.test(PasswordStats("fr3d")), False)
        self.assertEqual(password_test.test(PasswordStats("fr3d1")), False)
        self.assertEqual(password_test.test(PasswordStats("fr$d")), False)

        password_test = TrivialVariant("input")
        self.assertEqual(password_test.test(PasswordStats("1nput")), False)
        self.assertEqual(password_test.test(PasswordStats("!nput")), False)
        self.assertEqual(password_test.test(PasswordStats("|nput")), False)

        password_test = TrivialVariant("inside")
        self.assertEqual(password_test.test(PasswordStats("ins1de")), False)
        self.assertEqual(password_test.test(PasswordStats("ins!de")), False)
        self.assertEqual(password_test.test(PasswordStats("ins|de")), False)

        password_test = TrivialVariant("ladder")
        self.assertEqual(password_test.test(PasswordStats("1adder")), False)
        self.assertEqual(password_test.test(PasswordStats("!adder")), False)
        self.assertEqual(password_test.test(PasswordStats("|adder")), False)

        password_test = TrivialVariant("yellow")
        self.assertEqual(password_test.test(PasswordStats("ye1low")), False)
        self.assertEqual(password_test.test(PasswordStats("ye!low")), False)
        self.assertEqual(password_test.test(PasswordStats("ye|low")), False)

        password_test = TrivialVariant("option")
        self.assertEqual(password_test.test(PasswordStats("opti0n")), False)
        self.assertEqual(password_test.test(PasswordStats("opti@n")), False)
        self.assertEqual(password_test.test(PasswordStats("opti*n")), False)

        password_test = TrivialVariant("outside")
        self.assertEqual(password_test.test(PasswordStats("0utside")), False)
        self.assertEqual(password_test.test(PasswordStats("@utside")), False)
        self.assertEqual(password_test.test(PasswordStats("*utside")), False)

        self.assertEqual(password_test.test(PasswordStats("0uts1de")), False)
        self.assertEqual(password_test.test(PasswordStats("0utsid3")), False)

        password_test = TrivialVariant("leep")
        self.assertEqual(password_test.test(PasswordStats("l33p")), False)

    def test_should_return_true_when_different(self):
        password_test = TrivialVariant("apple")
        self.assertEqual(password_test.test(PasswordStats("fred")), True)
        self.assertEqual(password_test.test(PasswordStats("adqzf")), True)
        self.assertEqual(password_test.test(PasswordStats("lmnop")), True)
        self.assertEqual(password_test.test(PasswordStats("12345")), True)

        password_test = TrivialVariant("a")
        self.assertEqual(password_test.test(PasswordStats("fred")), True)

        password_test = TrivialVariant("a!@$GS~")
        self.assertEqual(password_test.test(PasswordStats("fred")), True)

        password_test = TrivialVariant("asdfasdfaslk;j;asa")
        self.assertEqual(password_test.test(PasswordStats("a")), True)
