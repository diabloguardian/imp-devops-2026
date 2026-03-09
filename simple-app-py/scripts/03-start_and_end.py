

def start_and_end(mainstring, substring):
    length_substring = len(substring)
    is_found = False
    for init_index in range(len(mainstring)):
        extractedchars = mainstring[init_index:(init_index + length_substring)]
        if extractedchars == substring:
            print("(" + str(init_index) + ", " + str(init_index + length_substring - 1) +")")
            is_found = True

    if not is_found:
        print("(-1, -1)")


start_and_end("aaadaa","aa")


#
#
# Pseudocode
#
#functionn(main_string, substring):
#    loop x in len(main_string):
#        extractedchars = main_string[x:len(subtring)]
#        compare the extractedchars with subtring:
#            print ( x , x +len(substring))


            