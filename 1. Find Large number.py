array = [50, 600, 780, 90, 8672]
n = len(array)
max = array[0]
for i in range(1,n):
    if array[i] > max:
        max = array[i]

print(max)

