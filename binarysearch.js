function binarysearch(arr,num) {
    'use strict';
 
    var begin = 0;
    var end = arr.length - 1;
    var mid

    while (begin <= end) {
        mid = (begin + end) / 2 | 0;

        if (arr[mid] < num) {
            begin = mid + 1;
        }

        else if (arr[mid] > num) {
            end = mid - 1;
        }

        else {
            return mid;
        }
    }
    return -1;
}

array = [1,2,3,4,5,6,7,8,9,10]
console.log(binarysearch(array,7))
