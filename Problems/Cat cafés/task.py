maxcats = 0
while True:
    instr = input()
    if instr.split()[0] == "MEOW":
        break
    if len(instr.split()) > 1:
        name, count = instr.split()
        if int(count) > maxcats:
            maxname = name
            maxcats = int(count)
print(maxname)
