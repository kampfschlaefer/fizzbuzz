
def fizzbuzz_ternary(number):
    output = not(number % 3) and 'Fizz' or ''
    output += not(number % 5) and 'Buzz' or ''
    return output or str(number)


def fizzbuzz_list(number):
    l = [str(number), 'Fizz', 'Buzz', 'FizzBuzz']
    return l[(not(number % 3)) + 2 * (not(number % 5))]
