import sys

n = int(sys.stdin.readline())
parts = list(map(int, sys.stdin.readline().rstrip().split()))
parts.sort()
m = int(sys.stdin.readline())
needs = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(start,end,target):
    if start > end:
        return False

    mid = (start+end)//2
    
    if parts[mid] == target:
        return True
    elif parts[mid] < target:
        binary_search(mid+1,end,target)
    else:
        binary_search(start,mid-1,target)

for need in needs:
    if binary_search(0,len(parts)-1,need) == True:
        print("yes", end=" ")
    else:
        print("no", end= " ")
