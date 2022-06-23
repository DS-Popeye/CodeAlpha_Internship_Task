arr = [1,4,3,5,46,10,54]
arr.sort()

low = 0
high = len(arr)-1
found = False

key = 7

while low <= high and not found:
    mid = (low + high) // 2
    if key == arr[mid]:
        found = True

    elif key > arr[mid]:
        low = mid+1

    else:
        high = mid-1

if found == True:
    print("Found")
else:
    print("Not Found")

