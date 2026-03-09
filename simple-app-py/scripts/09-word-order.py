
def read_input(input_string):
    input_splitted = input_string.split()
    return input_splitted[1:]

#  "bcdef","abcdefg","bcde","bcdef"

def word_order(input_string):
    input_words = read_input(input_string)
    words = {}
    output = ""
    for word in input_words:
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] = words[word] + 1

    
    for key, value in words.items():
        output = output + str(value) + " " 
    
    
    print(len(words.items()))
    print(output)


word_order("4\nbcdef\nabcdefg\nbcde\nbcdef")






#
#  https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
#
#  pseudocode
#
# create a function that receive the amount of words for order it
#   read every word and save it on a dictionary with the word as key and a counter as value, for increment counter check if the word exist in dictionary
#   print key and values of the dictionary
#
#
#
#
#