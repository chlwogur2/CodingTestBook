n = int(input())

array = set(map(int,input().split()))

m = int(input())

needs = list(map(int,input().split()))

for i in needs:
    if i in array:
        print('yes', end= ' ')
    else:
        print('no', end=' ')