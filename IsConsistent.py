def consist_of_zero(vector):
    of_zero = True
    for i in vector:
        if i != 0:
            of_zero = False
            break
    return of_zero


def number_of_rows(matrix):
    return len(matrix)


def number_of_colums(matrix):
    return len(matrix[0])

def check_matrix(matrix):
    a = len(matrix[0])
    for i in matrix:
        print(i)
        if len(i) != a:
            return False
    return True


def main(matrix_a, vector_b):
    # написати функцію для перевірки чи правильна введена матриця
    if check_matrix(matrix_a):
        if number_of_rows(matrix_a) == number_of_rows(vector_b):
            if consist_of_zero(vector_b):
                return "System is always consistent."
            else:
                final_matrix = matrix_a.add_vector(vector_b)
                final_matrix = to_return(final_matrix)
                final_matrix = check_system(final_matrix)
        else:
            return "System is inconsistent."
    else:
        return "Wrong size of matrix"
    
    
def to_return(matrix):#Викликати цю функцію!!!Вона забирає "-0.0" і ставить натомість "0.0"
    A = to_reduced_row_echelon_form(matrix)
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == -0.0:
                A[i][j] = 0.0
    return A


def to_reduced_row_echelon_form(matrix):
    if not matrix: return
    lead = 0
    row_count = number_of_rows(matrix)
    column_count = number_of_colums(matrix)
    for r in range(row_count):
        if lead >= column_count:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == row_count:
                i = r
                lead += 1
                if column_count == lead:
                    return
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
        for i in range(row_count):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
        lead += 1
    return matrix


def sum_of_row(row):
    a = row[:(len(row)-1)]
    return sum(a)


def is_consistent(matrix):# перевіряє зведену матрицю. Аби не було що 0x = 3
    is_consistent = True
    for i in matrix:
        print (i)
        if sum_of_row(i) == 0 and i[-1] != 0:
            is_consistent = False
    return is_consistent



def add_vector(matrix, vector):
    if number_of_rows(matrix) == number_of_rows(vector):
        for i in range(len(vector)):
            matrix[i].append(vector[i])
        return matrix
    else:
        return "Wrong vector"
