
def read_input(input_string):
    input_splitted = input_string.splitlines()
    xyz = input_splitted[0:3]
    n = int(input_splitted[3])
    return xyz, n


def permutations(input_string):
    xyz, n = read_input(input_string)
    print(int(xyz[0]))
    print(int(xyz[1]))
    print(int(xyz[2]))
    permutations = [[int(val),int(val2),int(val3)] for val in range(int(xyz[0])+1) for val2 in range(int(xyz[1])+1) for val3 in range(int(xyz[2])+1)]
    
    result = [row for row in permutations if sum(row) != n]
    print(result)



if __name__ == '__main__':
    permutations(input())

