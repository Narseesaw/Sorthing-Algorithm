# Bubble Sort

def sorter(arr):

    length = len(arr)
    x = 0
    while(x!= length):
        x+=1
        for i in range(0, length-1):
            if (arr[i+1])<=arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


arr = [44, 523, 9, 9, 46, 47]
print(f'actual array: {arr}')
sorter(arr)
print(f'sorted array: {arr}')