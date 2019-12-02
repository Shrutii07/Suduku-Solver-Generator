import random


# checks if number is already in row or not
# Returns true if already in row
def row_check(sud, row, num):
    if num in sud[row]:
        return True
    return False


# checks if number is already in column or not
# Returns true if already in row
def column_check(sud, j, num):
    list2 = []
    for b in range(0, 9, 1):
        list2.append(sud[b][j])
    if num in list2:
        return True
    return False


# checks if number is already in 3x3 grid or not
# Returns true if already in grid
def grid_check(sud, i, j, num):
    list2 = []
    for numm in range(3, 10, 3):
        if i < numm:
            a = numm - 3
            b = numm
            break
    for numm in range(3, 10, 3):
        if j < numm:
            c = numm - 3
            d = numm
            break
    for s in range(a, b, 1):
        for t in range(c, d, 1):
            list2.append(sud[s][t])
    if num in list2:
        return True
    return False


# Checks possibility of a number at particular row & column by checking rowwise,columnwise & gridwise
# Returns True if number is possible at ith row & jth column
def possibility(sud, i, j, num):
    if not row_check(sud, i, num) and not column_check(sud, j, num) and not grid_check(sud, i, j, num):
        return True
    return False


# checks for blank space in sudoku grid
# Returns true if blankspace is in suduku grid
def blank_space(sud):
    # row and column are declared as global so that values stored in both can be used in sudokusolver function
    global row, col
    for i in range(9):
        for j in range(9):
            if sud[i][j] == '_':
                row = i
                col = j
                return True
    return False


row = '_'
col = '_'


# Function to solve any suduku
def sudokusolver(sud):
    if blank_space(sud):
        i = row
        j = col
        # checks possibilty for (1,9) numbers at (i,j) position
        for sol in range(1, 10, 1):
            if possibility(sud, i, j, sol):
                # if any number in (1,9) satisfies possibility,insert that number at (i,j)th position
                sud[i][j] = sol
                # now go for next blank space in sudoku and check everytime that after inserting new number,it is satisfying possibility or not return true if yes
                if sudokusolver(sud):
                    return True
                # if not satisfying possibility then make it blank space again and go for next number frm 1 to 9
                else:
                    sud[i][j] = '_'
        # if no number satisfies (i,j) position return False
        return False
    # if no blank space return true i.e. sudoku solved
    else:
        return True


# function to check random 9x9 number grid if it can be a sudoku or not
def sudchecker(list):
    # checks rows of given grid
    # if elements in row r repeated returns false
    def rowcheck(list):
        for i in list:
            list2 = []
            for j in i:
                if j not in list2 and j != '_':
                    list2.append(j)
                elif j in list2:
                    return False
                elif j == '_':
                    continue
        return True

    # checks columns of given grid
    # returns false if number is repeated in a column
    def colucheck(list, k):
        if k >= len(list):
            return True
        else:
            list3 = []
            for j in range(0, 9, 1):
                list3.append(list[j][k])
            list2 = []
            for i in list3:
                if i not in list2 and i != '_':
                    list2.append(i)
                elif i in list2:
                    return False
                elif i == '_':
                    continue
            return colucheck(list, k + 1)

    # checks every 3x3 grid
    # returns false if number is repeated in 3x3 grid
    def gridcheck(list, c, d, a, b):
        list5 = []
        for i in range(c, d, 1):
            for j in range(a, b, 1):
                list5.append(list[i][j])
        list6 = []
        for h in list5:
            if h not in list6 and h != '_':
                list6.append(h)
            elif h in list6:
                return False
            elif h == '_':
                continue
        return True

    def grcheck(k, list):
        for i in range(0, k, 3):
            for j in range(0, k, 3):
                if not gridcheck(list, i, i + 3, j, j + 3):
                    return False
        return True

    # returns true if grid is possible else false
    if rowcheck(list) and colucheck(list, 0) and grcheck(9, list):
        return True
    return False


# Function to make random grid
# random numbers r inserted in random ith & jth position
def randomgen():
    list5 = [['_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_', '_']]

    i = 1
    while (0 < i < 16):
        rw = random.randint(0, 8)
        colu = random.randint(0, 8)
        ran = random.randint(1, 9)
        list5[rw][colu] = ran
        i += 1
    return list5


# function to create random suduku
# if grid by randomgen is possible & has unique solution returns list
def creater(list2):
    temp = True
    while temp:
        if sudchecker(list2):
            if sudokusolver(list2):
                temp = False
            else:
                list2 = randomgen()
                continue
        else:
            list2 = randomgen()
            continue
    return list2


list3 = randomgen()
list4 = creater(list3)

# creates empty spaces in the random sudoku created by creator
# randomly removes  numbers from ith & jth position of sudoku
if (sudokusolver(list4)):
    i = 1
    while (0 < i < 63):
        rw = random.randint(0, 8)
        colu = random.randint(0, 8)
        ran = random.randint(1, 9)
        if list4[rw][colu] != '_':
            list4[rw][colu] = '_'
            i += 1
        else:
            continue


# function to print sudoku
def checker_board(listt):
    l = 0
    for i in listt:
        h = 0
        l += 1
        n = -1
        for j in i:
            h += 1
            if h < 9:
                if j == 0:
                    n += 1
                    if n % 3 == 0:
                        print(' ||', end=' ')
                        print('_', end='')
                    else:
                        print('|', end=' ')
                        print('_', end='')
                else:
                    n += 1
                    if n % 3 == 0:
                        print(' ||', end=' ')
                        print(j, end='')
                    else:
                        print('|', end=' ')
                        print(j, end='')
            elif h == 9:
                if l % 3 == 0:
                    if j == 0:
                        print('|', end=' ')
                        print('_', end=' ')
                        print('||\n')
                    else:
                        print('|', end=' ')
                        print(j, end=' ')
                        print('||\n')
                else:
                    if j == 0:
                        print('|', end=' ')
                        print('_', end=' ')
                        print('||')
                    else:
                        print('|', end=' ')
                        print(j, end=' ')
                        print('||')


print("HI there!!!\nHere's ur SUDOKU genius")
checker_board(list4)
while True:
    ans = input('Wanna know solution of this:  ')
    if ans == 'yes' or ans == 'y' or ans == 'YES' or ans == 'Y':
        sudokusolver(list4)
        print('SUDOKU ')
        checker_board(list4)
        break
    elif ans == 'no' or ans == 'n' or ans == 'NO' or ans == 'N':
        print('Okie,GoodBye')
        break
    else:
        print('sry couldnt get u.... YES or NO????')
        continue