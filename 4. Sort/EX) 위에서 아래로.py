N = int(input())
array= []

for _ in range(N):
    array.append(int(input()))

for x in sorted(array):
    print(x, end=' ')