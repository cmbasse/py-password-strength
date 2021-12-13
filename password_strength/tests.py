""" These objects perform individual tests on a password, and report `True` of `False`. """

from .tests_base import ATest
from .bad_passwords import bad_password_lst

class MinLength(ATest):
    """ Tests whether password length >= `length` """

    def __init__(self, length):
        super(MinLength, self).__init__(length)
        self.length = length

    def test(self, ps):
        return ps.length >= self.length

    def __str__(self):
        return "Your password must be a minimum of {} characters.".format(self.length)


class MaxLength(ATest):
    """ Tests whether password length <= `length` """

    def __init__(self, length):
        super(MaxLength, self).__init__(length)
        self.length = length

    def test(self, ps):
        return ps.length <= self.length

    def __str__(self):
        return "Your password must not be greater than {} characters.".format(self.length)


class Uppercase(ATest):
    """ Test whether the password has >= `count` uppercase characters """

    def __init__(self, count):
        super(Uppercase, self).__init__(count)
        self.count = count

    def test(self, ps):
        return ps.letters_uppercase >= self.count

    def __str__(self):
        return "Your password must contain at least {} uppercase characters.".format(self.count)


class Numbers(Uppercase):
    """ Test whether the password has >= `count` numeric characters """

    def test(self, ps):
        return ps.numbers >= self.count

    def __str__(self):
        return "Your password must contain at least {} numbers.".format(self.count)


class Special(Uppercase):
    """ Test whether the password has >= `count` special characters """

    def test(self, ps):
        return ps.special_characters >= self.count

    def __str__(self):
        return "Your password must contain at least {} special characters.".format(self.count)


class NonLetters(Uppercase):
    """ Test whether the password has >= `count` non-letter characters """

    def test(self, ps):
        non_letters = ps.length - ps.letters
        return non_letters >= self.count

    def __str__(self):
        return "Your password must contain at least {} non-letter characters.".format(self.count)


class NonLettersLc(Uppercase):
    """ Test whether the password has >= `count` non-lowercase characters """

    def test(self, ps):
        non_lowercase_letters = ps.length - ps.letters_lowercase
        return non_lowercase_letters >= self.count

    def __str__(self):
        return "Your password must contain at least {} non-lowercase characters.".format(self.count)


class EntropyBits(ATest):
    """ Test whether the password has >= `bits` entropy bits.

    Entropy bits is the number of bits that is required to store the alphabet that's used in a password.
    It's a measure of how long is the alphabet.

    """

    def __init__(self, bits):
        super(EntropyBits, self).__init__(bits)
        self.bits = bits

    def test(self, ps):
        return ps.entropy_bits >= self.bits

    def __str__(self):
        return "Your password does not contain enough unique characters."


class Strength(ATest):
    """ Test whether the password has >= `strength` strength.

        A password is evaluated to the strength of 0.333 when it has `weak_bits` entropy bits,
        which is considered to be a weak password. Strong passwords start at 0.666.
    """

    def __init__(self, strength, weak_bits=30):
        super(Strength, self).__init__(strength, weak_bits)
        self.strength = strength
        self.weak_bits = weak_bits

    def test(self, ps):
        return (1 - ps.weakness_factor) * ps.strength(self.weak_bits) >= self.strength

    def __str__(self):
        return "Your password is not strong enough"


class DoesNotContain(ATest):
    """
    Tests whether or not the illegal phrase is in the password.
    It also checks that the illegal phrase backwards is not in the password.
    """

    def __init__(self, illegal_phrase, case_dependent=True):
        super(DoesNotContain, self).__init__(illegal_phrase)
        self.illegal_phrase = illegal_phrase
        self.case_dependent = case_dependent

    def test(self, ps):
        if self.case_dependent:
            return self.illegal_phrase not in ps.password and\
                   self.illegal_phrase[::-1] not in ps.password
        else:
            return self.illegal_phrase.lower() not in ps.password.lower() and\
                   self.illegal_phrase.lower()[::-1] not in ps.password.lower()

    def __str__(self):
        return "Your password can not contain {}".format(self.illegal_phrase)


class TrivialVariant(ATest):
    """
    Checks to see if there are at least min_difference number of characters
    positionally different between the password and the illegal phrase.
    """

    def __init__(self, illegal_phrase, min_difference=2):
        super(TrivialVariant, self).__init__(illegal_phrase)
        self.illegal_phrase = illegal_phrase
        self.min_difference = min_difference

    def test(self, ps):
        count = sum(1 for a, b in zip(ps.password.lower(), self.illegal_phrase.lower()) if a != b) + abs(len(ps.password) - len(self.illegal_phrase))
        return count > self.min_difference

    def __str__(self):
        return "You can not use trivial variations of {}".format(self.illegal_phrase)


class BadPassword(ATest):
    """
    Make sure the password isn't on the list of bad passwrods
    """

    def __init__(self):
        super(BadPassword, self).__init__()

    def test(self, ps):
        if ps.password.lower() in bad_password_lst:
            return False

        return True

    def __str__(self):
        return "That password is to weak and can not be used"
