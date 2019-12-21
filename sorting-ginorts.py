def get_lower_case_letters(s):
    return ''.join(c for c in s if c.islower())


def get_upper_case_letters(s):
    return ''.join(c for c in s if c.isupper())


def get_odd_digits(s):
    return ''.join(c for c in s if c.isdigit() and int(c) % 2 == 1)


def get_even_digits(s):
    return ''.join(c for c in s if c.isdigit() and int(c) % 2 == 0)


def process(s):
    return ''.join(sorted(get_lower_case_letters(s))) + ''.join(sorted(get_upper_case_letters(s))) + ''.join(
        sorted(get_odd_digits(s))) + ''.join(sorted(get_even_digits(s)))


if __name__ == '__main__':
    string = input()
    sorted_str = process(string)
    print(sorted_str)
