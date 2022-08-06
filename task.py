def conv_hex(num_str):
    """
    Takes passed string that has been trimmed of '0x' or '-0x' prefix and returns the positive integer value.
    If the passed value contains invalid digits, returns None. Called as helper function by conv_num().
    """
    integer_val = 0
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                  'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_exponent = len(num_str) - 1
    for digit in num_str:
        if digit in hex_digits:
            integer_val += hex_digits[digit] * 16 ** hex_exponent
            hex_exponent -= 1
        else:
            return None
    return integer_val


def conv_num(num_str):
    """
    Takes a string and converts it into a base 10 number which is then returned.
    Can handle strings representing: integers, floating-point numbers, and integer hexadecimals with prefix '0x'.
    """
    integer_value = 0
    fraction_value = 0

    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    sign = +1
    decimal = False
    fraction_counter = 1
    count = 0
    low = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', \
          'v', 'w', 'x', 'y', 'z'
    upper = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
            'U', 'V', 'W', 'X', 'Y', 'Z'

    # Check if num_str is positive hexadecimal and call conversion helper function
    if num_str[:2] == '0x':
        return conv_hex(num_str[2:])

    # Check if num_str is negative hexadecimal and call conversion helper function
    if num_str[:3] == '-0x':
        integer_value = conv_hex(num_str[3:])
        if integer_value is not None:
            return integer_value * -1
        return integer_value

    for digit in num_str:
        if digit in low or digit in upper:
            return None
        if digit == '-':
            sign = -1
            continue
        if digit == '.':
            count += 1
            if count > 1:
                return None
            decimal = True
            continue
        if decimal:
            fraction_value = (fraction_value * 10) + value[digit]
            fraction_counter *= 10
        else:
            integer_value = integer_value * 10 + value[digit]

    if decimal:
        integer_value = integer_value + (fraction_value / fraction_counter)

    integer_value = integer_value * sign
    return integer_value


def my_datetime(num_sec):
    num_days = num_sec // (24 * 60 * 60)
    month = 1
    day = 1
    year = 1970

    def leapYear(val):
        if (val % 4 == 0 and val % 100 != 0) or val % 400 == 0:
            return True
        False

    def months(year, month):
        dayCount = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthDays = dayCount[month]
        if leapYear(year) and month == 2:
            return monthDays + 1
        else:
            return monthDays

    while num_days > 0:
        num_days -= 1
        day += 1
        if day > months(year, month):
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
    return '%02d-%02d-%02d' % (month, day, year)


def conv_endian(num, endian='big'):
    """
    Takes an integer value and endian flag then converts and returns as a string.
    """
    pass
