def index_equals_value_search(arr):
  begin = 0
  end = len(arr) -1
  
  while begin <= end:
    mid = int((begin+end)/2)
    if arr[mid] < mid:
      begin = mid + 1
    elif arr[mid] > mid:
      end = mid - 1
    else:
      return mid
  return -1

#time o(log n)
#space o(1)
