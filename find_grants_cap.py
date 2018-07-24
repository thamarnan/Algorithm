def find_grants_cap(grantsArray, newBudget):
  sortedArray = sorted(grantsArray)
  
  sum_array = sum(sortedArray)
  
  lower = 0
  max_cap = 0
  
  for i in range(len(sortedArray)):
    #compute the capped sum
    cappedSum = capTheSum(sortedArray, sortedArray[i])
    if cappedSum < newBudget:
      lower = sortedArray[i]
    
    if cappedSum > newBudget:
      print(i)
      break
  print(lower, " is the lower bound")
  
  lowerBoundCapSum = capTheSum(sortedArray,lower)*1.0
  print(lowerBoundCapSum)
  return (newBudget-lowerBoundCapSum )/(len(sortedArray)-i)
  
  
def capTheSum(arr, cap):
  #apply cap to array and return the sum
  sumArr = 0
  for i in range(len(arr)):
    sumArr += min(arr[i], cap)
  return sumArr

