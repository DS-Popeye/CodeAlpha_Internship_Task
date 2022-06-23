myTuple = (4, 9, 1, 7, 3, 6, 5, 2)
K = 5

sortedColl = sorted(list(myTuple))
vals = []
for i in range(K):
    vals.append(sortedColl[i])

for i in range((len(sortedColl) - K), len(sortedColl)):
    vals.append(sortedColl[i])

# Printing
print("Tuple : ", str(myTuple))
print("K maximum and minimum values : ", str(vals))