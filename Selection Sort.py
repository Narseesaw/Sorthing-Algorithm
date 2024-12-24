# Selection Sort

def sorter(arr):
    arr_length = len(arr)
    for i in range(arr_length-1):
        selected_index = i

        for j in range(i+1, arr_length):
            if arr[selected_index]>arr[j]:
                selected_index = j

        arr[i], arr[selected_index] = arr[selected_index], arr[i]


    return arr

arr = [44, 523, 9, 13, 46, 47]
print(f'actual array: {arr}')
x = sorter(arr)
print(f'sorted array: {arr}')