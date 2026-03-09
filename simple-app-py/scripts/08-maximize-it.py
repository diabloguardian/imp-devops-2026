

def maximize(k,m):
    list_of_lists = list()
    for x in range(k):
        input_string = input().split()
        list_of_lists.append(list(input_string[1:]))
    print (list_of_lists)

    results = list()
    for i in range(len(list_of_lists)):
        current_list = list_of_lists[i:i+1]
        print("current list", current_list)
        print("list of lists", list_of_lists)
        




maximize(3,100)









#  pseudocode
#  
#  define a function for receive K(number of lines) and M (module) parameters
#      for every line, receive the number of elements in the list as a first integer, then the list of elements in the same input
#          create an list with elements for every line
#      
#       perform the squares, sum and module operations with one element of every list and keep the results into a list 
#  
#      sort desc the list with the results 
#      print the first value 
#  
#  call the function
#  


