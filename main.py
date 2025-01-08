from collections import deque
from pyspark import SparkConf, SparkContext
import sys


def n_base_decimal_base(numbers, base):
    value_converted = 0
    for i, number in enumerate(numbers):
        value_converted += (numbers[i] * (base ** (len(numbers) - i - 1)))
    return value_converted


def assign_digits(word, digits_numbers, is_min):
    digits_deque = deque(digits_numbers)

    if is_min:
        zero_digit = digits_deque.popleft()
        digits_list = list(digits_deque)
        digits_list.insert(1, zero_digit)
        digits_deque = deque(digits_list)
    else:
        digits_deque.reverse()

    letter_dict = {}
    seen = set()

    for ch in word:
        if ch not in seen:
            letter_dict[ch] = digits_deque.popleft()
            seen.add(ch)

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


def process_case(x):
    case_index, word = x
    base = get_base(word)
    base_digits_array = list(range(base))
    smallest_number_decimal, biggest_number_decimal \
        = find_smallest_and_biggest_numbers(
        word, base_digits_array, base
    )
    return case_index, biggest_number_decimal - smallest_number_decimal


def main():
    conf = SparkConf().setAppName("M41").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    data = sys.stdin.read().strip().split('\n')

    t = int(data[0])
    input_cases = data[1:]
    rdd = sc.parallelize(input_cases, t)

    indexed_rdd = rdd.zipWithIndex().map(lambda x: (x[1], x[0]))
    results = indexed_rdd.map(process_case).collect()
    results.sort(key=lambda x: x[0])

    for (case_index, val) in results:
        print("Case #{}: {}".format(case_index + 1, val))

    sc.stop()


if __name__ == '__main__':
    main()
