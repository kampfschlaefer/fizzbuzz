
def fizzbuzz(number):
    # print(number, number % 3, not(number % 3), number % 5, not(number % 5))
    output = not(number % 3) and 'Fizz' or ''
    output += not(number % 5) and 'Buzz' or ''
    return output or str(number)
