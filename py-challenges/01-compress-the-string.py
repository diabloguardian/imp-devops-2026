
def compress(thestring):
    output = ""
    counter = 0
    the_iterable = iter(thestring)
    current_value = next(the_iterable) 
    while True:
        try:
            next_value = next(the_iterable)
            counter = counter + 1
            if current_value != next_value:
                output = output + "(" + str(counter) + ", " + current_value + ") "
                counter = 0
            current_value = next_value
        except StopIteration:
            output = output + "(" + str(counter + 1) + ", " + next_value + ") "
            break      

    print(output)


compress("1222311")


# Solution for "Compress the string" problem.
# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# I convert the string in a iter object for execute a loop manually using next function for compare de each value with de next one.