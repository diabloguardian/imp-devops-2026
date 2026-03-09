

def finding_percentage(num_of_records):
    dictionary = {}
    
    for x in range(int(num_of_records)):
        record = input().split()
        name = record[0]
        marks = record[1:]
        dictionary[name] = marks
    
    query = input()

    values_queried = dictionary[query]

    sum = 0
    for mark in values_queried:
        sum = sum + int(mark)
    
    average = sum / len(values_queried)

    print(f"{average:.2f}")






finding_percentage(input())


# https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
#
#
# create a function for receive the amount of records of names and marks
#       read every name and marks splitting ever enrty
#       read the query
#       create a dictionary for keep the records with name as key
#       from dictionary get the record that contains the query
#       calculate the percentage of values
#       print the result
#
