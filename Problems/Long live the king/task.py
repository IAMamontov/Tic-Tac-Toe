column = int(input())
row = int(input())

if row >= 8 or row <= 1:
    if column >= 8 or column <= 1:
        print("3")
    else:
        print("5")
elif column >= 8 or column <= 1:
    print("5")
else:
    print("8")