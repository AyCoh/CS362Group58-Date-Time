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


def conv_int_or_fp(num_str):
    """
    Takes passed string with integer or floating point number and returns a number value.
    If the passed string contains invalid digits or multiple decimal points, returns None.
    Called as helper function by conv_num().
    """
    integer_value = 0
    fraction_value = 0

    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    sign = 1
    decimal = False
    fraction_counter = 1
    decimal_count = 0
    for digit in num_str:
        if digit not in value:
            if digit == '-':
                sign = -1
            elif digit == '.':
                decimal_count += 1
                if decimal_count > 1:
                    return None
                decimal = True
            else:
                return None
        elif decimal:
            fraction_value = (fraction_value * 10) + value[digit]
            fraction_counter *= 10
        else:
            integer_value = integer_value * 10 + value[digit]

    if decimal:
        integer_value = integer_value + (fraction_value / fraction_counter)

    integer_value = integer_value * sign
    return integer_value


def leap_year(val):
    """
    Takes passed value of a year and returns whether it is a leap year. Called as helper function by months().
    """
    if (val % 4 == 0 and val % 100 != 0) or val % 400 == 0:
        return True
    return False


def months(year, month):
    """
    Takes integer values for year and month and returns the number of days in that particular month.
    Called as helper function by my_datetime().
    """
    day_count = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days = day_count[month]
    if leap_year(year) and month == 2:
        return month_days + 1
    else:
        return month_days


def conv_num(num_str):
    """
    Takes a string and converts it into a base 10 number which is then returned.
    Can handle strings representing: integers, floating-point numbers, and integer hexadecimals with prefix '0x'.
    """

    # Validate that num_str is not empty
    if len(num_str) == 0:
        return None

    # Check if num_str is positive hexadecimal and call conversion helper function
    if num_str[:2] == '0x':
        return conv_hex(num_str[2:])

    # Check if num_str is negative hexadecimal and call conversion helper function
    elif num_str[:3] == '-0x':
        integer_value = conv_hex(num_str[3:])
        if integer_value is not None:
            return integer_value * -1
        return integer_value

    # Else, string is an integer or floating point. Call conversion helper function.
    else:
        return conv_int_or_fp(num_str)


def my_datetime(num_sec):
    num_days = num_sec // (24 * 60 * 60)
    month = 1
    day = 1
    year = 1970

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
    Takes an integer value and endian flag then converts and returns as a hexadecimal string.
    If no flag is given, defaults to big endian.
    """
    dec_hex = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    pairs = []
    hex_list = []
    hex_string = ""
    num_string = str(num)
    quotient_remainder = (abs(num), 0)

    if endian != "big" and endian != "little":
        return None

    while quotient_remainder[0] != 0:
        quotient_remainder = divmod(quotient_remainder[0], 16)
        if quotient_remainder[1] < 10:
            hex_list.append(str(quotient_remainder[1]))
            continue
        hex_list.append(dec_hex[quotient_remainder[1]])

    hex_list.reverse()

    if len(hex_list) % 2 != 0:
        hex_list.insert(0, "0")

    for i in range(0, len(hex_list), 2):
        pairs.append(hex_list[i] + hex_list[i + 1])

    if endian == "little":
        for i in range(len(pairs), 0, -1):
            hex_string = hex_string + pairs[i - 1] + " "
    else:
        for i in range(len(pairs)):
            hex_string = hex_string + pairs[i] + " "

    if num_string[0] == "-":
        hex_string = "-" + hex_string

    return hex_string.strip()
