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


def main(matrix_a, vector_b):
    if number_of_rows(matrix_a) == number_of_rows(vector_b):
        if consist_of_zero(vector_b):
            return "System is always consistent."
        else:
            final_matrix = matrix_a.add_vector(vector_b)
            final_matrix = to_reduced_row_echelon_form(final_matrix)
            final_matrix = check(final_matrix)
    else:
        return "System is inconsistent."


def to_reduced_row_echelon_form(matrix):
    if not matrix: return
    lead = 0
    rowCount = number_of_rows(matrix)
    columnCount = number_of_colums(matrix)
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
        for i in range(rowCount):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
        lead += 1
    return matrix


def check(matrix):
    pass


def add_vector(vector):
    pass
