def consist_of_zero(vector):
    of_zero = True
    for i in vector:
        if i != 0:
            of_zero = False
            break
    return of_zero


def number_of_rows(matrix):
    return len(matrix)


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
    pass


def check(matrix):
    pass


def add_vector(vector):
    pass