chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
money = int(input())
if money >= sheep:
    print(money // sheep, "sheep")
elif money >= cow:
    if money // cow > 1:
        print(money // cow, "cows")
    else:
        print(money // cow, "cow")
elif money >= pig:
    if money // pig > 1:
        print(money // pig, "pigs")
    else:
        print(money // pig, "pig")
elif money >= goat:
    if money // goat > 1:
        print(money // goat, "goats")
    else:
        print(money // goat, "goat")
elif money >= chicken:
    if money // chicken > 1:
        print(money // chicken, "chickens")
    else:
        print(money // chicken, "chicken")
else:
    print("None")