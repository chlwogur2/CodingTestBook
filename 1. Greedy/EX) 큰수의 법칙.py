n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

arr.sort()

first = arr[n-1]
second = arr[n-2]

while m>0:
    result += (first*k)
    result += second
    m -= k+1

print(result)
