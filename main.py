from sudoku import *
from OnePlayerMode import *
from random import sample
from TwoPlayerMode import *
import re
import datetime
N = 9
'''try:
    file = input("Enter file name\n")
    f = open("file",  "r")
    sudoku = []
    line0 = f.read().replace(" ", "")
    if re.search('[a-zA-Z]', line0):
        raise Exception
    oo = line0.replace(",", ",0").split("\n")
    for j in range(9):
        list = []
        for i in range(len(oo[j].split(","))):
            if oo[j].split(",")[i] == "":
                list.append(0)
            else:
                list.append(int(oo[j].split(",")[i]))
        if len(oo[j].split(",")) < 9:
            for x in range(abs(len(oo[j].split(",")) - 9)):
                list.append(0)
        sudoku.append(list)
    print(sudoku)
    f.close()
except IOError:
    print("Error: can\'t find file or read data")
except Exception:
    print("Error: the data is incorrect ")'''
print("/////////////")
print(sudoku)
base = 3
side = base*base

# pattern for a baseline valid solution
def pattern(r, c):
    return (base*(r % base)+r//base+c) % side
# randomize rows, columns and numbers (of valid base pattern)

def shuffle(s): return sample(s, len(s))
rBase = range(base)
rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base*base+1))

# produce board using randomized baseline pattern
board = [[nums[pattern(r, c)] for c in cols] for r in rows]


def copyArray(arr):
    newArray = copy.deepcopy(arr)
    return newArray

def hent(arr1, arr2):
    for i in range(N):
        for j in range(N):
            if arr1[i][j] == 0:
                arr1[i][j] = arr2[i][j]
                print("the column ", i+1, "the row ", j+1, "replace 0 with ", arr2[i][j])
                return

print("*****************")
'''print("full array")
for line in board:
    print(line)'''
'''palyer = onePlayerMode(sudoku)
#palyer.level1()
palyer.printing()
print("*****************")
new = copyArray(sudoku)
palyer.solveSuduko(new)
print("*****************")

''''''''for line in board:
    print(line)'''
#print("*****************")
'''for line in new:
    print(line)''''''''
print("*****************")
point = 0
palyer.printing()'''
'''while not palyer.isSolve():

    x = int(input("if you need hent enter 1"))
    if x == 1:
        hent(palyer.arr, new)
        palyer.printing()
        point -= 2
    col, row, num = map(int, input("Enter column, row, num to add:").split())

    if palyer.isSafe(col-1, row-1, num):
        palyer.arr[col-1][row-1] = num
        point += 1

    else:
        print("invalid ")


    palyer.printing()'''

player2 = twoPlayerMode(board)
player2.level1()

new1 = copyArray(board)
player2.solveSuduko(new1)

point1 = 0
point2 = 0
time1 = 0
time2 = 0
turn = 1

#start1 = datetime.datetime.now()

def passFun(time1,time2,turn):

    end1 = datetime.datetime.now()
    houer1 = abs((end1.hour) - (start1.hour))
    min1 = abs((end1.minute) - (start1.minute))
    sec1 = abs((end1.second) - (start1.second))
    if (houer1 > 0):
        houer1 = houer1 * 60 * 60
    if (min1 > 0):
        min1 = min1 * 60

    if turn == 1:
        time1 += houer1 + min1 + sec1
        turn = 2
    else:
        time2 += houer1 + min1 + sec1
        turn = 1

    return turn, time1, time2




while not player2.isSolve():
    start1 = datetime.datetime.now()

    x = int(input("1 => solve , 2 => pass , 3=> to fill the cell"))

    if x == 1:
        player2.solveSuduko(player2.arr)
    elif x == 2:
        turn, time1, time2 = passFun(time1, time2, turn)
    elif x == 3:
        player2.printing()
        col, row, num = map(int, input("Enter column, row, num to add:").split())
        if player2.isSafe(col - 1, row - 1, num):
            player2.arr[col - 1][row - 1] = num
            if turn == 1:
                point1 += 1
                print("point1 : ", point1)
                print("time1 : ", time1)
                turn = 2
            else:
                point2 += 1
                print("point2 : ", point2)
                print("time2 : ", time2)
                turn = 1


        else:
            print("invalid ")

    else:
        print("invalid input")
    #player2.printing()