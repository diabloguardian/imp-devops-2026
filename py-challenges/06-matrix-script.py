

alfanumerics = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

def decode_matrix(n,m):
    matrix = list()
    message = ""
    message_decoded = ""
    for i in range(n):
        matrix.append(list(input()))

    
    for index_col in range(len(matrix[0])):
        for index_row in range(len(matrix)):
            message = message + matrix[index_row][index_col]

    first_char_index = -1
    last_char_index = -1
    for index, char in enumerate(message):
        if char in alfanumerics and first_char_index == -1:
            first_char_index = index
        if char in alfanumerics and first_char_index != -1:
            last_char_index = index


    for index, char in enumerate(message):
        if ((index >= first_char_index and index <= last_char_index) and char not in alfanumerics):
            message_decoded = message_decoded + " "
        else:
            message_decoded = message_decoded + char

    print(message_decoded)
            
    





decode_matrix(7,3)






# https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
#
#
# Pseudocodigo
#
#
# Crear funcion que recibe dos valores para determinar el tamaño de la matriz
#    declarar variable matrix
#    ciclo del tamaño de las filas para llenar con valores la variable matrix
#        leer cada fila de caracteres de entrada
#        Guardar cada fila en la variable matrix
#
#
#    crear variable message para almacenar el resultado
#    ciclo del tamaño de las columnas para leer el contenido de la matrix 
#        ciclo del tamaño de las filas 
#            concatenar a la variable message el valor de matrix[indice_fila][indice_columna]
# 
#   ****** con regex reemplazar todos los simbolos que están entre dos caracteres alfanumericos por espacios en blanco, en la variable message
#    buscar los indices del primer y ultimo caracter alfanumerico
#    reemplazar todos los caractares no alafanumericos que están entre los indices anteriores
#    imprimir resultado de la variable message