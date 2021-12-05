FILE_NAME = "input.txt"
GAMMA = "GAMMA"
EPSILON = "EPSILON"

input = open(FILE_NAME, "r")
VECTOR_SIZE = len(input.readline()) - 1

def read_input():
    open(FILE_NAME, "r")
    return input.readlines()

values = read_input()

counted_values =  [0] * VECTOR_SIZE
XOR_MASK = '1' * VECTOR_SIZE

def count_bits(value):
    for i in range(0, VECTOR_SIZE):
        if value[i] == '1':
            counted_values[i] = counted_values[i] + 1 

def calculate_gamma():
    gamma = ""
    for i in range (0, VECTOR_SIZE):
        if counted_values[i] >= len(values)/2:
            gamma = gamma + '1'
        else:
            gamma = gamma + '0'
    return gamma

def calculate_epsilon(gamma):
    return gamma ^ int(XOR_MASK,2)

def reset_bit_counter():
    for i in range(0, VECTOR_SIZE):
        counted_values[i] = 0

def count_all_vectors():
    for value in values:
        count_bits(value)

def eliminate_by_bit_criteria(i, criteria):
    indexes_to_delete = []
    for j in range(0,len(values)):
        if criteria[i] != (values[j])[i]:
            indexes_to_delete.append(j)

    for k in range(len(indexes_to_delete)-1, -1, -1):
        if(len(values) == 1):
            break
        del values[indexes_to_delete[k]]

def recount_and_eliminate(calculate_by):
    while len(values) > 1:
        for i in range(0, VECTOR_SIZE):
            reset_bit_counter()
            count_all_vectors()
            gamma = calculate_gamma()
            if(calculate_by == "GAMMA"):
                criteria = gamma
            else:
                epsilon = calculate_epsilon(int(gamma,2))
                criteria = str.zfill(str(bin(epsilon)).split('b')[1], VECTOR_SIZE)
            eliminate_by_bit_criteria(i, criteria)


count_all_vectors()
gamma = int(calculate_gamma(),2)
print("gamma " + str(gamma))
epsilon = calculate_epsilon(gamma)
print("epsilon " + str(epsilon))
# part one solution
print(gamma * epsilon)

values = (open(FILE_NAME, "r")).readlines()

recount_and_eliminate(GAMMA)
oxygen = int(values[0],2)
print("oxy " + str(oxygen))

values = (open(FILE_NAME, "r")).readlines()

recount_and_eliminate(EPSILON)
co2 = int(values[0], 2)
print("co2 " + str(co2))

# part two solution
print(oxygen*co2)