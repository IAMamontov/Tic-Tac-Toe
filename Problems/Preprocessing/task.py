punct = ",.!?"
s = input()
for c in punct:
    s = s.replace(c, "")
print(s.lower())
