import itertools

vekt = [6, 5, 5, 7, 6, 2, 4, 7, 3, 5, 20, 11, 2, 3]
volum = [6, 16, 4, 5, 12, 7, 10, 5, 13, 6, 17, 5, 17, 12]

result = [seq for i in range(len(vekt), 0, -1) for seq in itertools.combinations(vekt, i) if sum(seq) > 30]
print (len(result))
result = [seq for i in range(len(volum), 0, -1) for seq in itertools.combinations(volum, i) if sum(seq) > 81]
print (len(result))

val1 = 0
val2 = 0
result1 = []
result2 = []

for i in range(len(vekt), 0, -1):
    for seq in itertools.combinations(vekt, i):
        val1 +=1
        if sum(seq) > 30:
            result1.append(val1)
            
for j in range(len(volum), 0, -1):
    for seq in itertools.combinations(volum, j):
        val2 +=1
        if sum(seq) > 81:
            result2.append(val2)
            
            
print(len(set(result2) & set(result1)))