







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
#        ciclo del tamaño de las columnas
#            Guardar cada caracter en la variable matrix
#
#
#    crear variable decode para almacenar el resultado
#    ciclo del tamaño de las columna para leer el contenido de la matrix 
#        ciclo del tamaño de las filas 
#            concatenar a la variable decode el valor de matrix[indice_fila][indice_columna]
# 
#    con regex reemplazar todos los simbolos que están entre dos caracteres alfanumericos por espacios en blanco, en la variable decode
#    imprimir resultado de la variable decode