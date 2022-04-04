import random
import math
import copy
from sudoku import *
N = 9
class onePlayerMode(sudoku):
    def __init__(self, arr):
        self.arr = arr
    def level1(self):
        list_i = [i for i in range(0, 9)]
        v1 = int(math.sqrt(49)) + 1
        for i in range(7):
            if len(list_i) == 0:
                break
            list_j = [j for j in range(0, 9)]
            r1 = random.choice(list_i)
            list_i.remove(r1)
            for j in range(7):
                if len(list_j) == 0:
                    break
                r2 = random.choice(list_j)
                list_j.remove(r2)
                self.arr[r1][r2] = 0


    def level2(self):
        list_i = [i for i in range(0, 9)]
        v1 = int(math.sqrt(61)) + 1
        for i in range(v1):
            if len(list_i) == 0:
                break
            list_j = [j for j in range(0, 9)]
            r1 = random.choice(list_i)
            list_i.remove(r1)
            for j in range(int(math.sqrt(61)) + 1):
                if j >= v1 - 3 and i == v1 - 1:
                    break
                if len(list_j) == 0:
                    break
                r2 = random.choice(list_j)
                list_j.remove(r2)
                self.arr[r1][r2] = 0

    def level3(self):
        list_i = [i for i in range(0, 9)]
        for i in range(9):
            if len(list_i) == 0:
                break
            list_j = [j for j in range(0, 9)]
            r1 = random.choice(list_i)
            list_i.remove(r1)
            for j in range(8):
                if len(list_j) == 0:
                    break
                r2 = random.choice(list_j)
                list_j.remove(r2)
                self.arr[r1][r2] = 0




    # Checks whether it will be
    # legal to assign num to the
    # given row, col
    def isSafe(self, row, col, num):
        # Check if we find the same num
        # in the similar row , we
        # return false
        for x in range(9):
            if self.arr[row][x] == num:
                return False

        # Check if we find the same num in
        # the similar column , we
        # return false
        for x in range(9):
            if self.arr[x][col] == num:
                return False

        # Check if we find the same num in
        # the particular 3*3 matrix,
        # we return false
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.arr[i + startRow][j + startCol] == num:
                    return False
        return True

    # Takes a partially filled-in grid and attempts
    # to assign values to all unassigned locations in
    # such a way to meet the requirements for
    # Sudoku solution (non-duplication across rows,
    # columns, and boxes) */





    def solveSuduko(self, array, row = 0, col = 0):
        # Check if we have reached the 8th
        # row and 9th column (0
        # indexed matrix) , we are
        # returning true to avoid
        # further backtracking
        if (row == N - 1 and col == N):
            return True

        # Check if column value  becomes 9 ,
        # we move to next row and
        # column start from 0
        if col == N:
            row += 1
            col = 0

        # Check if the current position of
        # the grid already contains
        # value >0, we iterate for next column
        if array[row][col] > 0:
            return self.solveSuduko(array, row, col + 1)
        #return False
        for num in range(1, N + 1, 1) :

            # Check if it is safe to place
            # the num (1-9)  in the
            # given row ,col  ->we
            # move to next column
            if self.isSafe(row, col, num):

                # Assigning the num in
                # the current (row,col)
                # position of the grid
                # and assuming our assigned
                # num in the position
                # is correct
                array[row][col] = num

                # Checking for next possibility with next
                # column
                if self.solveSuduko(array, row, col + 1):
                    return True

            # Removing the assigned num ,
            # since our assumption
            # was wrong , and we go for
            # next assumption with
            # diff num value
            array[row][col] = 0
        return False

    def printing(self):
        for line in self.arr:
            print(line)


    def isSolve(self):
        for i in range(N):
            for j in range(N):
                if self.arr[i][j] == 0:
                    return False
        return True

