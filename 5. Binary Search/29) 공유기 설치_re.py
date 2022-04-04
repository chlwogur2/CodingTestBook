import sys

n, c = map(int, sys.stdin.readline().rstrip().split())

house = []
for _ in range(n):
    house.append(int(sys.stdin.readline().rstrip()))

house.sort()

min_distance = 1
max_distance = house[-1] - house[0]
result = 0

def binary_search(min_distance,max_distance):
    global result
    while min_distance <= max_distance:
        mid = (min_distance+max_distance) // 2
        value = house[0]
        count = 1

        for i in range(1,n):
            if house[i] >= value + mid:
                value = house[i]
                count += 1
        
        if count >= c:
            min_distance = mid + 1
            result = mid
        else:
            max_distance = mid - 1

binary_search(min_distance,max_distance)
print(result)