import unittest
from password_strength import PasswordPolicy, tests


class PolicyTestCase(unittest.TestCase):
    """ Test: PasswordPolicy """
    longMessage = True

    def test(self):
        policy = PasswordPolicy.from_names(
            minlength=8,
            maxlength=20,
            uppercase=2,
            numbers=2,
            special=2,
            nonletters=2,
            nonletterslc=2,
            entropybits=30,
            strength=(0.333, 30)
        )

        passwords = {
            'qazwsx':           {'minlength', 'uppercase', 'numbers', 'special', 'nonletters', 'nonletterslc', 'entropybits', 'strength'},
            'qazwsxrfv':        {             'uppercase', 'numbers', 'special', 'nonletters', 'nonletterslc', 'entropybits', 'strength'},
            'qazwsxrfvTG':      {                          'numbers', 'special', 'nonletters',                                          },
            'qazwsxrfvTG94':    {                                     'special',                                                        },
            'qazwsxrfvTG94@#$asddfA@#$asd':    {'maxlength',},
            'qazwsxrfvTG94@$':  set(),
        }

        for password, expects in passwords.items():
            self.assertEqual(
                {t.name() for t in policy.test(password)},
                expects,
                'Testing {}'.format(password)
            )
