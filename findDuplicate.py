
def binarySearch(arr, num):
    begin = 0
    end = len(arr) - 1
    
    while begin <= end:
        mid = int((begin+end)/2)
        if arr[mid] < num:
            begin = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            return mid
    return -1

def find_duplicates(arr1, arr2):
    result = []
    for i in arr1:
        if binarySearch(arr2, i) != -1: result.append(i)
    return result


arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates(arr1, arr2))
