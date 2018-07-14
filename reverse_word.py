def reverse_words(arr):
  
  reverse_arr(arr,0,len(arr)-1)
 # print(arr)
  space = -1
  for i in range(len(arr)):
    if arr[i] == ' ':
      reverse_arr(arr,space+1,i-1)
      space = i

  reverse_arr(arr,space+1,len(arr)-1)
      
  return arr

  
  
def reverse_arr(arr, start, end): #pointer method
  l, r= start, end
  while (l < r):
    arr[l],arr[r] = arr[r],arr[l]
    l += 1
    r -= 1
    
    #time  o(n)
    #space o(1)
