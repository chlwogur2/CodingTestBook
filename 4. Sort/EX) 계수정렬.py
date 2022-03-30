array = [1,5,3,2,6,7,1,8,6,6,9,0,0,0,7,8,2,4,9,3,6]
sorted_array = []
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        sorted_array.append(i)

print(sorted_array)        