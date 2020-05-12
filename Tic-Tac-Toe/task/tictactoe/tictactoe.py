# write your code here

def fill_from_cells(cells):
    display = [[0 for j in range(9)] for i in range(5)]
    for i in range(5):
        for j in range(9):
            if i == 0 or i == 4:
                display[i][j] = "-"
            elif j == 0 or j == 8:
                display[i][j] = "|"
            elif j % 2 == 1:
                display[i][j] = " "
            else:
                display[i][j] = cells[j//2 - 1 + (i - 1) * 3]
    return display

def show_dispay(display):
    for i in range(5):
        for j in range(9):
            print(display[i][j], end="")
        print()

def check_xxx(display):
    if ([display[1][2], display[2][4], display[3][6]] == ["X", "X", "X"]) \
            or ([display[3][2], display[2][4], display[1][6]] == ["X", "X", "X"]):
        return True
    for i in range(1, 4):
        if ([display[i][2], display[i][4], display[i][6]] == ["X", "X", "X"]) \
            or ([display[1][i * 2], display[2][i * 2], display[3][i * 2]]
                == ["X", "X", "X"]):
            return True
    return False

def check_ooo(display):
    if ([display[1][2], display[2][4], display[3][6]] == ["O", "O", "O"]) \
            or ([display[3][2], display[2][4], display[1][6]] == ["O", "O", "O"]):
        return True
    for i in range(1,4):
        if ([display[i][2], display[i][4], display[i][6]] == ["O", "O", "O"]) \
            or ([display[1][i * 2], display[2][i * 2], display[3][i * 2]]
                == ["O", "O", "O"]):
            return True
    return False

xxx = False
ooo = False
cells_in = "_________"
display_out = fill_from_cells(cells_in)
show_dispay(display_out)
moves = 0

while True:
    while True:
        y, x = input("Enter the coordinates: > ").split()
        if not("0" < x < "9") or not("0" < y < "9"):
            print("You should enter numbers!")
        elif int(x) not in range(1,4) or int(y) not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
        elif display_out[4 - int(x)][int(y) * 2] != "_":
            print("This cell is occupied! Choose another one!")
        else:
            if moves % 2 == 0:
                display_out[4 - int(x)][int(y) * 2] = "X"
                moves += 1
                break
            else:
                display_out[4 - int(x)][int(y) * 2] = "O"
                moves += 1
                break
    show_dispay(display_out)
    xxx = check_xxx(display_out)
    ooo = check_ooo(display_out)
    if xxx:
        print("X wins")
        break
    if ooo:
        print("O wins")
        break
    if moves >= 9:
        print("Draw")
        break
