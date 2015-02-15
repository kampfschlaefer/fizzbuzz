
def fizzbuzz(number):
    output = ''
    if number % 3 == 0:
        output += 'Fizz'
    if number % 5 == 0:
        output += 'Buzz'
    if not output:
        output = '%i' % number
    return output
