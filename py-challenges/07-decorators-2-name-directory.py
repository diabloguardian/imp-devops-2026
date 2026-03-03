
import operator

def person_lister(f):
    def inner(people):
        sorted_list = sorted(people, key=lambda row: row[2])
        return [f(people) for people in sorted_list]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')



# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true
#
#
# Pseudocodigo
#
#
# Crear funcion que sirve como decorator para listar personas:
#    ordenar lista de personas por edad (indice 2 de cada elemento)
#    llamar a funcion func()
#    
#    
# Crear funcion "name_format" para dar formato a los nombres de las personas usando el decorador creado en la funcion anterior
#    si el valor del indice 3 es M concatenar "Mr." en caso contrario concatenar "Ms." concatenar valores de los indices 1 y 2 que corresponden al nombre y apellido
#    devolver cadena concatenada
#    
#    
# crear arreglo de personas
# imprimir el resultado de llamar a la función name_format
