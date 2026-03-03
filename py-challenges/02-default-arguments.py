
def print_from_stream(n, stream="even"):
    if stream == "even":
        evenStream(n)
    elif stream == "odd":
        oddStream(n)


def evenStream(n):
    number = 0
    counter = 0
    while counter < n:
        number = number + 1
        if number%2 == 0:
            print (number)
            counter = counter + 1


def oddStream(n):
    number = 0
    counter = 0
    while counter < n:
        number = number + 1
        if number%2 != 0:
            print (number)
            counter = counter + 1

print_from_stream(2,"odd")
print_from_stream(3)
print_from_stream(5, "odd")


#
# Pseudocode
#
#
#first function for receive the inputs(streamname=evenStream, n):
#    eval streamname == evenStream:
#        evenStream(n)
#    else:
#        oddStream(n)
#    
#    
#function evenStream(n):
#    loop x from 0 to n:
#        if  x%2 == 0
#           print x
#
#
#function oddStream(n):
#    loop x from 0 to n:
#        if  x%2 != 0
#           print x

