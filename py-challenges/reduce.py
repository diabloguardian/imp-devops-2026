

def product(number_of_rational_num):
    numerator_product = 1
    denominator_product = 1
    
    for i in range(int(number_of_rational_num)):
        rational_number = input().split()
        numerator_product = numerator_product * int(rational_number[0])
        denominator_product = denominator_product * int(rational_number[1])
    
    rational_reduced = [numerator_product,denominator_product]

    for i in range(5):
        rational_reduced = reduce(rational_reduced)

    print(int(rational_reduced[0]),int(rational_reduced[1]))




def reduce(rational_number):
    numerator_reduced = 0 
    denominator_reduced = 0
    for i in [2,3,5,7,9]:
        numerator_divided = rational_number[0]%i
        denominator_divided = rational_number[1]%i
        if numerator_divided == 0 and denominator_divided == 0:
            numerator_reduced = rational_number[0] / i
            denominator_reduced = rational_number[1] / i
            break

    if numerator_reduced == 0 and denominator_reduced == 0:
        numerator_reduced = rational_number[0]
        denominator_reduced = rational_number[1]
        
    return [numerator_reduced, denominator_reduced]
            



product(input())
    










# https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
#
#
# create a function for receive the amount of rational numbers 
#       read every rational number splitting ever enrty
#       multiply all nominators of rational number
#       multiply all denominators of rational number
#       call a function a few times for reduce the product
#       print the result
#
#  create a function for reduce the product
#       iterate over divisible common numbers:
#           validate if denominator and numerator has a common divisible number and break the loop
#        if there are not divisible number, return the entry numbers
#
# 
#
