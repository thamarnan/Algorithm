#cheatsheet

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

arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates (arr1, arr2))

myList=[]
for i in range(10):
	myList.append(i)

myList.append()
myList.sort(reverse=True)

#add to second position
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")

#list - sequence in specific order 
thislist[3]

#tuple - immutable, cannot remove or replace
thistuple = tuple(("apple", "banana", "cherry"))
thistuple[3]

#set - no order, check element contain faster, no repeat value
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#dictionary - mapping key to value
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)



a = "Hello, World!"
a[1]
b[2:5]
a.strip() #trim surround whitesp
len(a)
	str = "abc"
	for i in range(len(str)):
a.lower()
a.upper()
a.replace("F","R")
a.split(",")
"Hello" + a


with open('filename.txt') as fp:
    for line in fp:
        print line


import sys
print "script name: ", sys.argv[0]
print "# of arguments: ", len(sys.argv)
print "all argument: " , str(sys.argv)

from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'https://httpbin.org/post' # Set destination URL here
post_fields = {'foo': 'bar'}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)


for i in range(5):
	print(i)
	
for x in range(0, 10,3): # 0,3,6,9
	print "we are at %d" % (x)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])

x = 1
while True:
    print "we are at %d " % (x)
    x += 1

if expression1:
   statement(s)
elif expression2:
   statement(s)
else:
   statement(s)



