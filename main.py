def n_base_decimal_base(numbers, base):
    value_converted = 0
    for i, number in enumerate(numbers):
        value_converted += (numbers[i] * (base ** (len(numbers) - i - 1)))
    return value_converted


if __name__ == '__main__':
    print('Hello World')