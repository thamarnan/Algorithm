import math
'''
|       |
|       |
|---x---|
|       |
|       |
'''
def drawHTree(x,y,length,depth):
  if depth < 1:
    return 0

  x0 = x-length/2.0
  y0 = y-length/2.0

  x1 = x+length/2.0
  y1 = y+length/2.0

  drawLine(x0, y0, x0, y1)  #L
  drawLine(x1, y0, y1, y1)  #R
  drawLine(x0, y , x1,  y)  #Line
  

  drawHTree(x0, y0, length/math.sqrt(2), depth-1) 
  drawHTree(x0, y1, length/math.sqrt(2), depth-1)    
  drawHTree(x1, y0, length/math.sqrt(2), depth-1)   
  drawHTree(x1, y1, length/math.sqrt(2), depth-1)    

def drawLine(x1,y1,x2,y2):
  print(x1,y1,x2,y2)


drawHTree(0,0,2,2)

#time O(4^D)
#space O(D)
