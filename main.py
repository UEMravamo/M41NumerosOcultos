def n_base_decimal_base(numbers, base):
    value_converted = 0
    for i, number in enumerate(numbers):
        value_converted += (numbers[i] * (base ** (len(numbers) - i - 1)))
    return value_converted


def assign_digits(word, digits_numbers, is_min):
    digits_copy = digits_numbers[:]

    if is_min:
        zero_digit = digits_copy.pop(0)
        digits_copy.insert(1, zero_digit)
    else:
        digits_copy = digits_copy[::-1]

    letter_dict = {}
    seen = set()
    for character in word:
        if character not in seen:
            letter_dict[character] = digits_copy.pop(0)
            seen.add(character)

    assigned_digits = [letter_dict[ch] for ch in word]

    return assigned_digits


def find_smallest_and_biggest_numbers(word, digits_numbers, base):
    smallest_assigned = assign_digits(word, digits_numbers, True)
    smallest_decimal = n_base_decimal_base(smallest_assigned, base)

    biggest_assigned = assign_digits(word, digits_numbers, False)
    biggest_decimal = n_base_decimal_base(biggest_assigned, base)

    return smallest_decimal, biggest_decimal


def get_base(s):
    return len(set(s))


def main():
    t = int(input())
    input_cases = []
    for i in range(t):
        input_cases.append(input())

    for case_number, word in enumerate(input_cases):
        base = get_base(word)
        digits = list(range(base))

        smallest_number_decimal, biggest_number_decimal \
            = find_smallest_and_biggest_numbers(word, digits, base)
        print("Case #{}: {}".format(
            case_number + 1,
            biggest_number_decimal - smallest_number_decimal)
        )


if __name__ == '__main__':
    print('Hello World')
