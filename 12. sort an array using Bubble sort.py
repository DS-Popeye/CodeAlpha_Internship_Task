arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
swaped = False

for i in range(0,n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print("Step : ",arr)
            print()
        else:
            print("else : ",arr)
print("Final : ",arr)

