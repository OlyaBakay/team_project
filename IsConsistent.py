import unittest
from IsConsistent import *

class Test(unittest.TestCase):
    def test_1_consist_of_zero(self):
        expected = True
        actual = consist_of_zero([0,0,0])
        self.assertEqual(expected, actual, "Error")

    def test_2_consist_of_zero(self):
        expected = False
        actual = consist_of_zero([0,1,0,0,0])
        self.assertEqual(expected, actual, "Error")

    def test_3_consist_of_zero(self):
        expected = True
        actual = consist_of_zero([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(expected, actual, "Error")

    def test_4_consist_of_zero(self):
        expected = False
        actual = consist_of_zero([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(expected, actual, "Error")

    def test_1_number_of_rows(self):
        expected = 3
        actual = number_of_rows([[3,2,1],[0,0,0],[4,6,5]])
        self.assertEqual(expected, actual, "Error")

    def test_2_number_of_rows(self):
        expected = 9
        actual = number_of_rows([[3,2,4,4,3,1],[0,5,4,4,0,0],[4,4,4,4,6,5],[3,2,4,4,4,1],[0,0,5,5,5,0],[4,4,4,4,6,5],[3,4,4,4,2,1],[0,0,5,5,5,0],[4,6,6,6,6,5]])
        self.assertEqual(expected, actual, "Error")

    def test_1_number_of_columns(self):
        expected = 4
        actual = number_of_colums([[3,2,5,1],[5,0,0,0],[5,4,6,5]])
        self.assertEqual(expected, actual, "Error")

    def test_2_number_of_columns(self):
        expected = 9
        actual = number_of_colums([[3,2,4,4,5,5,5,4,1],[0,0,5,5,5,5,5,5,0],[4,5,5,5,4,4,4,6,5],[3,4,5,5,5,4,4,2,1],[0,0,5,5,5,5,5,5,0],[4,6,5,5,5,6,6,6,5]])
        self.assertEqual(expected, actual, "Error")

    def test_1_check_matrix(self):
        expected = False
        actual = check_matrix([[3,2,4,4,5,5,5,4],[0,0,5,5,5,5,5,5,0],[4,5,5,5,4,4,4,6,5],[3,4,5,5,5,4,4,2,1],[0,0,5,5,5,5,5,5,0],[4,6,5,5,5,6,6,6,5]])
        self.assertEqual(expected, actual, "Error")

    def test_2_check_matrix(self):
        expected = True
        actual = check_matrix([[3,2,4,4,5,5,5,4,1],[0,0,5,5,5,5,5,5,0],[4,5,5,5,4,4,4,6,5],[3,4,5,5,5,4,4,2,1],[0,0,5,5,5,5,5,5,0],[4,6,5,5,5,6,6,6,5]])
        self.assertEqual(expected, actual, "Error")

    def test_3_check_matrix(self):
        expected = False
        actual = check_matrix([[3,2,4],[5,4],[6,5,4]])
        self.assertEqual(expected, actual, "Error")

    def test_4_check_matrix(self):
        expected = True
        actual = check_matrix([[4,3,5],[8,7,6],[9,8,7]])
        self.assertEqual(expected, actual, "Error")

    def test_1_main(self):
        expected = "Wrong size of matrix"
        actual = main([[3,2,4,4,5,5,5,4],[0,0,5,5,5,5,5,5,0],[4,5,5,5,4,4,4,6,5],[3,4,5,5,5,4,4,2,1],[0,0,5,5,5,5,5,5,0],[4,6,5,5,5,6,6,6,5]],[2,4,6,3])
        self.assertEqual(expected, actual, "Error")

    def test_2_main(self):
        expected = "Wrong size of matrix"
        actual = main([[3,2,4],[0,0,5],[4,5,5],[3,4,2,1]],[2,4,6,3])
        self.assertEqual(expected, actual, "Error")

    def test_3_main(self):
        expected = "System is inconsistent."
        actual = main([[3,2,4,4,5,5,5,4,1],[0,0,5,5,5,5,5,5,0],[4,5,5,5,4,4,4,6,5],[3,4,5,5,5,4,4,2,1],[0,0,5,5,5,5,5,5,0],[4,6,5,5,5,6,6,6,5]],[2,4,6,3])
        self.assertEqual(expected, actual, "Error")

    def test_4_main(self):
        expected = "System is inconsistent."
        actual = main([[3,2,4],[0,0,5],[4,5,5],[3,4,2]],[2,4,6])
        self.assertEqual(expected, actual, "Error")

    def test_5_main(self):
        expected = "System is always consistent."
        actual = main([[1,2,3],[2,4,5],[3,2,1]],[0,0,0])
        self.assertEqual(expected, actual, "Error")

    def test_6_main(self):
        expected = "System is always consistent."
        actual = main([[1,2,3],[5,5,5],[7,6,5],[6,5,4],[6,5,4],[2,4,5],[3,2,1]],[0,0,0,0,0,0,0])
        self.assertEqual(expected, actual, "Error")

    def test_7_main(self):
        expected = ([[1,0,0,1],[0,1,0,0],[0,0,1,0]],"System is consistent")
        actual = main([[1,0,0],[1,2,0],[1,2,3]],[1,1,1])
        self.assertEqual(expected, actual, "Error")

    def test_8_main(self):
        expected = ([[1, 0, 0,0,0,0,0.4], [0, 1, 0,0,0,0,1.8], [0, 0, 1,0,0,0,0.4],[0, 0,0,1,0,0,1],[0,0,0,0,1,0,-1],[0,0,0,0,0,1,-0.8]], 'System is consistent')
        actual = main([[1,2,0,0,3,0],[3,0,2,0,0,0],[1,1,0,1,0,4],[3,0,2,0,2,0],[0,1,2,0,1,2],[0,0,0,2,0,0]],[1,2,0,0,0,2])
        self.assertEqual(expected, actual, "Error")

    def test_9_main(self):
        expected = "System is inconsistent"
        actual = main([[1,1,1],[1,2,3],[2,3,4]],[150,100,200])
        self.assertEqual(expected, actual, "Error")

    def test_10_main(self):
        expected = "System is inconsistent"
        actual = main([[2,0,2,0,0,1],[0,2,0,1,0,3],[2,0,0,0,3,0],[0,1,0,2,0,1],[1,0,3,0,1,0],[0,0,0,0,0,0]],[100,100,100,100,100,100])
        self.assertEqual(expected, actual, "Error")

    def test_1_to_return(self):
        expected = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        actual = to_reduced_row_echelon_form([[1,0,-0,0,0,0],[0,1,-0,0,0,0],[-0,-0,1,-0,-0,-0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,-0,0,0,1]])
        self.assertEqual(expected, actual, "Error")

    def test_2_to_return(self):
        expected = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        actual = to_reduced_row_echelon_form([[1,-0,-0,-0,-0,-0],[-0,1,-0,-0,-0,-0],[-0,-0,1,-0,-0,-0],[-0,-0,-0,1,-0,-0],[-0,-0,-0,-0,1,-0],[-0,-0,-0,-0,-0,1]])
        self.assertEqual(expected, actual, "Error")

    def test_3_to_return(self):
        expected = [[1,0,0],[0,1,0],[0,0,1]]
        actual = to_reduced_row_echelon_form([[1,-0,-0],[-0,1,-0],[-0,-0,1]])
        self.assertEqual(expected, actual, "Error")

    def test_1_to_reduced_row_echelon_form(self):
        expected = None
        actual = to_reduced_row_echelon_form(None)
        self.assertEqual(expected, actual, "Error")

    def test_2_to_reduced_row_echelon_form(self):
        expected = None
        actual = to_reduced_row_echelon_form([[0,0,0],[0,1,0],[0,0,1]])
        self.assertEqual(expected, actual, "Error")

    def test_3_to_reduced_row_echelon_form(self):
        expected = None
        actual = to_reduced_row_echelon_form([[0,0,0],[0,0,0],[0,0,0]])
        self.assertEqual(expected, actual, "Error")

    def test_4_to_reduced_row_echelon_form(self):
        expected = [[1,0,0],[0,1,0],[0,0,1]]
        actual = to_reduced_row_echelon_form([[5,1,0],[2,1,0],[3,0,1]])
        self.assertEqual(expected, actual, "Error")

    def test_5_to_reduced_row_echelon_form(self):
        expected = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
        actual = to_reduced_row_echelon_form([[1,0,0,0,0,0],[1,2,0,0,0,0],[1,2,3,0,0,0],[1,2,3,4,0,0],[1,2,3,4,5,0],[1,2,3,4,5,6]])
        self.assertEqual(expected, actual, "Error")

    def test_1_sum_of_row(self):
        expected = 13
        actual = sum_of_row([7,6,5])
        self.assertEqual(expected, actual, "Error")

    def test_2_sum_of_row(self):
        expected = 51
        actual = sum_of_row([7,4,6,9,7,5,4,4,5,6])
        self.assertEqual(expected, actual, "Error")

    def test_1_is_consistent(self):
        expected = False
        actual = is_consistent([[0,4,6],[1,4,0],[0,0,2]])
        self.assertEqual(expected, actual, "Error")

    def test_2_is_consistent(self):
        expected = True
        actual = is_consistent([[0,4,6],[1,4,0],[0,0,0]])
        self.assertEqual(expected, actual, "Error")

    def test_3_is_consistent(self):
        expected = True
        actual = is_consistent([[0,4,6],[1,4,0],[5,1,2]])
        self.assertEqual(expected, actual, "Error")

    def test_4_is_consistent(self):
        expected = False
        actual = is_consistent([[0,4,6],[1,4,0],[-7,7,5]])
        self.assertEqual(expected, actual, "Error")

    def test_5_is_consistent(self):
        expected = False
        actual = is_consistent([[0,4,6,6,5,7,4,5,6],[1,4,0,7,6,5,8,7,6],[0,0,0,0,0,0,0,0,2]])
        self.assertEqual(expected, actual, "Error")

    def test_6_is_consistent(self):
        expected = True
        actual = is_consistent([[0,4,6,7,6,5,8,7,9],[1,2,3,5,4,3,1,4,0],[0,0,0,0,0,0,0,0,0]])
        self.assertEqual(expected, actual, "Error")

    def test_7_is_consistent(self):
        expected = True
        actual = is_consistent([[0,4,6,7,6,5,8,7,9],[1,2,3,5,4,3,1,4,0],[0,7,6,8,7,6,8,6,7]])
        self.assertEqual(expected, actual, "Error")

    def test_8_is_consistent(self):
        expected = False
        actual = is_consistent([[0,4,6,7,6,5,8,7,9],[1,2,3,5,4,3,1,4,0],[6,7,6,8,-7,-6,-8,-6,7]])
        self.assertEqual(expected, actual, "Error")

    def test_1_add_vector(self):
        expected = ([[1,5,3,5,7,3,6,5,6,7,4],[5,3,8,6,1,4,7,6,5,4,5],[7,4,6,9,7,5,4,4,5,6,7]])
        actual = add_vector([[1,5,3,5,7,3,6,5,6,7],[5,3,8,6,1,4,7,6,5,4],[7,4,6,9,7,5,4,4,5,6]],[4,5,7])
        self.assertEqual(expected, actual, "Error")

    def test_2_add_vector(self):
        expected = ([[2,4,3,7],[4,6,5,6],[6,5,4,5]])
        actual = add_vector([[2,4,3],[4,6,5],[6,5,4]],[7,6,5])
        self.assertEqual(expected, actual, "Error")

    def test_3_add_vector(self):
        expected = "Wrong vector"
        actual = add_vector([[2,4,3],[4,6,5],[6,5,4]],[7,6,5,7])
        self.assertEqual(expected, actual, "Error")

    def test_4_add_vector(self):
        expected = "Wrong vector"
        actual = add_vector([[2,4,3,7,6,5,8,6,5,7],[4,6,5,8,7,6,5,5,4,6],[6,5,4,6,5,4,3,4,5,6]],[7,6,5,7])
        self.assertEqual(expected, actual, "Error")

if __name__ == "__main__":
    unittest.main()
