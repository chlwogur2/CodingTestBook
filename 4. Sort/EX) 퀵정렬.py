array = [1,5,0,7,8,2,4,9,3,6]

def quick_sort(start,end,array):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot],array[right] = array[right], array[pivot]
        else:
            array[left],array[right] = array[right],array[left]

    quick_sort(start,start,right-1)
    quick_sort(right+1,end,array)

quick_sort(0,len(array)-1,array)
print(array)