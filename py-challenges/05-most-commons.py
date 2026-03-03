

def most_commons(string):
    ocurrences = {}
    if len(string) > 3:
        for char in string:
            ocurrence_key = ocurrences.get(char, "Not found")
            if ocurrence_key == "Not found":
                ocurrences[char] = 1
            else:
                ocurrences[char] = ocurrences[char] + 1

        sorted_by_ocurrence = {k: v for k, v in sorted(ocurrences.items(), key=lambda item: item[1], reverse=True)}

        counter = 0
        for key, value in sorted_by_ocurrence.items():
            print (key, value)
            counter = counter + 1
            if counter == 3:
                break




#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
#
#
# Pseudocodigo
#
#
# Crear funcion que recibe una cadena
#     crear un diccionario para almacenar cada caracter como llave y el numero de ocurrencias como valor
#     validar que la cadena tenga al menos 3 caracteres
#     Iterar sobre la cadena recorriendo cada caracter
#         buscar en el diccionario el cada caracter
#         si no se encuentra:
#             agregar el caracter al diccionario con valor de ocurrencia = 1
#         de lo contrario:
#             incrementar el valor de cocurrencia del caracter en el diccionario
#     
#         ordenar diccionario de manera descendente de acuerdo al valor de cada elemento del diccionario
#     
#     Iterar sobre el diccionario ordenado
#         Imprimir la llave y el valor
#         Detener el ciclo a la tercer iteración
#
#
#








most_commons("aabbbccde")







