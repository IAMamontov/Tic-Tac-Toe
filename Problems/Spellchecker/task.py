dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
s = input()
all = True
for ss in s.split():
    if ss not in dictionary:
        print(ss)
        all = False
if all:
    print("all correct")
