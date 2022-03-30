array = [1,5,0,7,8,2,4,9,3,6]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]

print(array)