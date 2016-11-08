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
        if len(i) != a:
            return False
    return True


def main(matrix_a, vector_b):
    if check_matrix(matrix_a):
        if number_of_rows(matrix_a) == number_of_rows(vector_b):
            if consist_of_zero(vector_b):
                return "System is always consistent."
            else:
                final_matrix = add_vector(matrix_a,vector_b)
                final_matrix = to_return(final_matrix)
                tmp = final_matrix
                final_matrix = is_consistent(final_matrix)
                if final_matrix:
                    return for_arsen(tmp), "System is consistent"
                else:
                    return "System is inconsistent"
        else:
            return "System is inconsistent."
    else:
        return "Wrong size of matrix"
    
    
def to_return(matrix):
    A = to_reduced_row_echelon_form(matrix)
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == -0.0:
                A[i][j] = 0.0
    return A


def to_reduced_row_echelon_form(matrix):
    if not matrix: 
        return
    lead = 0
    row_сount = number_of_rows(matrix)
    column_сount = number_of_colums(matrix)
    for r in range(row_сount):
        if lead >= column_сount:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == row_сount:
                i = r
                lead += 1
                if column_сount == lead:
                    return
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
        for i in range(row_сount):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
        lead += 1
    return matrix


def sum_of_row(row):
    a = row[:(len(row)-1)]
    return sum(a)


def is_consistent(matrix):
    is_сonsistent = True
    for i in matrix:
        if sum_of_row(i) == 0 and i[-1] != 0:
            is_сonsistent = False
    return is_сonsistent


def add_vector(matrix, vector):
    if number_of_rows(matrix) == number_of_rows(vector):
        for i in range(len(vector)):
            matrix[i].append(vector[i])
        return matrix
    else:
        return "Wrong vector"
    
    
def for_arsen(matrix):
    only_matrix = []
    augmented_part = []
    for i in matrix:
        only_matrix.append(i[:len(i)-1])
        augmented_part.append(i[-1])
    return only_matrix, augmented_part
