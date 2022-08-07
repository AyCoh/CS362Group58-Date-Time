import unittest
from task import conv_num, my_datetime, conv_endian


class TestCase(unittest.TestCase):
    """
    Contains 19 tests lifted directly from the Part 2 examples. 1-8 test conv_num, 9-12 test my_datetime, and 13-19 test
    conv_endian. Additional test cases were added by our group starting with test20.
    """

    def test1(self):
        # Tests a positive integer
        self.assertEqual(conv_num('12345'), 12345)

    def test2(self):
        # Tests a negative decimal
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test3(self):
        # Tests a decimal without a leading 0
        self.assertEqual(conv_num('.45'), 0.45)

    def test4(self):
        # Tests a decimal without a trailing 0
        self.assertEqual(conv_num('123.'), 123.0)

    def test5(self):
        # Tests a hex with prefix 0x
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test6(self):
        # Tests a hex prefix 0x but with letter beyond A-H
        self.assertEqual(conv_num('0xAZ4'), None)

    def test7(self):
        # Tests a hex number without 0x prefix
        self.assertEqual(conv_num('12345A'), None)

    def test8(self):
        # Tests a string with multiple decimal points
        self.assertEqual(conv_num('12.3.45'), None)

    def test9(self):
        # Tests the epoch
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test10(self):
        # Tests one leap year
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test11(self):
        # Tests the delorean by heading into the future
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test12(self):
        # Tests if we can stick the landing on return a leap day Feb 29
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    def test13(self):
        # Tests a denoted big endian conversion of positive integer
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test14(self):
        # Tests whether big endian is default for conversion of positive integer
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test15(self):
        # Tests a big endian conversion of negative integer
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test16(self):
        # Tests a denoted little endian conversion of positive integer
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test17(self):
        # Tests a denoted little endian conversion of negative integer
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test18(self):
        # ???
        self.assertEqual(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test19(self):
        # Tests that a parameter other than 'big' or 'little' being passed for endian will return None
        self.assertEqual(conv_endian(num=-954786, endian='small'), None)

    def test20(self):
        # Tests a conv_num using hex with prefix -0x
        self.assertEqual(conv_num('-0xAD4'), -2772)

    def test21(self):
        # Tests a conv_num using hex with prefix -0x and non-hex digits
        self.assertEqual(conv_num('0xAKD4'), None)

    def test22(self):
        # Tests a conv_num using empty string
        self.assertEqual(conv_num(''), None)

    def test23(self):
        # Tests when the time lands at midnight
        self.assertEqual(my_datetime(86400), '01-02-1970')

    def test24(self):
        # Tests when the time lands at 23:59
        self.assertEqual(my_datetime(86399), '01-01-1970')


if __name__ == '__main__':
    unittest.main()
