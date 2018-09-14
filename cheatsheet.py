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
