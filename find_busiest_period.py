def find_busiest_period(data):

  count = 0
  busiest = 0
  a = 0
  
  for i in range(len(data)):
    #data[i] [1487799425, 14, 1] 1x - 1x
    if data[i][2] == 1:
        count += data[i][1]
    if data[i][2] == 0:
        count -= data[i][1]
        
    
    if (i < len(data)-1) and (data[i][0] == data[i+1][0]):
      continue
      
 #   else:
    if count > busiest:
        busiest = count
        a = data[i][0]

  return a
