

def merge_the_tools(string,size_substring):
    splits = len(string) / size_substring
    for x in range(int(splits)):
        start_index = x * size_substring
        end_index = start_index + size_substring
        substring = string[start_index:end_index]
        remove_duplicates(substring)

def remove_duplicates(substring):
    result = ""
    for char in substring:
        if char not in result:
            result = result + char
    print(result)



merge_the_tools("AABCAAADA",3)


#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
#
#### Pseudocodigo
#
#
# crear funcion que recibe la cadena y el tamaño de substring:
#     calcular la cantidad de veces que cabe el substring en la cadena
#     iterar el numero de veces de splits
#        calcular el indice de inicio de cada split
#        calcular el indice de fin de cada split
#        obtener substring
#        llamar la funcion que remueve los caracteres duplicados
#
#
#crear funcion que remueve duplicados recibiendo el substring como parametro:
#     crear variable para concatenar el resultado final
#     iterar sobre el substring recibido
#        validar si cada caracter no está en el resultado final
#           agregar el caracter al resultado 
#     imprimir resultado
