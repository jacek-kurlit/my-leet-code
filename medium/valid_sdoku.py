from typing import List


def has_unique_digits(digits: List[str]) -> bool:
    v = [0] * 10
    for d in digits:
        if d != ".":
            v_index = ord(d) - ord("0")
            if v[v_index] != 0:
                return False
            v[v_index] = 1
    return True


def all_rows_are_valid(board: List[List[str]]) -> bool:
    for row in board:
        if not has_unique_digits(row):
            return False
    return True


def all_columns_are_valid(board: List[List[str]]) -> bool:
    for column in range(9):
        column_digits = [board[row][column] for row in range(9)]
        if not has_unique_digits(column_digits):
            return False
    return True


def all_cells_are_valid(board: List[List[str]]) -> bool:
    for cell_row in range(3):
        for cell_column in range(3):
            cell_digits = []
            cell_range_start = 3 * cell_column
            cell_range_end = cell_range_start + 3
            cell_digits.extend(board[3 * cell_row][cell_range_start:cell_range_end])
            cell_digits.extend(board[3 * cell_row + 1][cell_range_start:cell_range_end])
            cell_digits.extend(board[3 * cell_row + 2][cell_range_start:cell_range_end])
            if not has_unique_digits(cell_digits):
                return False
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            all_rows_are_valid(board)
            and all_columns_are_valid(board)
            and all_cells_are_valid(board)
        )


if __name__ == "__main__":
    s = Solution()
    result = s.isValidSudoku(
        [
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )

    print(result)
