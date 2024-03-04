def interpolationSearch(arr, n, x): 
    # Find indexs of two corners 
    lo = 0
    hi = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            hi = pos - 1; 
      
    return -1
  
# Driver Code 
# Array of items oin which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, \ 
                22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 
  
x = 18 # Element to be searched 
index = interpolationSearch(arr, n, x) 
  
if index != -1: 
    print "Element found at index",index 
else: 
    print "Element not found"



#PHIÊN BẢN ĐỆ QUI

def interpolationSearch(arr, lo, hi, x): 
      
    # Since array is sorted, an element present  
    # in array must be in range defined by corner  
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]): 
          
        # Probing the position with keeping  
        # uniform distribution in mind.  
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                                       (x - arr[lo])) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
  
        # If x is larger, x is in right subarray 
        if arr[pos] < x: 
            return interpolationSearch(arr, pos + 1, 
                                       hi, x) 
          
        # If x is smaller, x is in left subarray 
        if arr[pos] > x: 
            return interpolationSearch(arr, lo,  
                                       pos - 1, x) 
    return -1
  
# Driver code 
  
# Array of items in which  
# search will be conducted 
arr = [ 10, 12, 13, 16, 18, 19, 20, \ 
        21, 22, 23, 24, 33, 35, 42, 47 ]  
n = len(arr)  
  
# Element to be searched 
x = 18  
index = interpolationSearch(arr, 0, n - 1, x)  
  
if index != -1:  
    print("Element found at index", index) 
else:  
    print("Element not found")
