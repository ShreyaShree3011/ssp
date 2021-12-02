def binary_search(arr, low, high, x):
   if high >= low:
      mid = (high + low) // 2
      if arr[mid] == x:
         return mid
      elif arr[mid] > x:
         return binary_search(arr, low, mid - 1, x)
      else:
         return binary_search(arr, mid + 1, high, x)
   else:
      return -1
arr = [ 5, 25, 35, 50, 100, 150, 160 ]
x = 35
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
   print("Element",x,"is present at index", str(result))
else:
   print("Element is not present in array")
