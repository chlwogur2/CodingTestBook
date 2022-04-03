def binary_search(start,end,target,array):
    if start > end:
        return None
    
    # 중간인덱스: 소수 첫째 자리는 버림
    mid = (start+end) // 2
    # 답을 찾은 경우: 중간 인덱스 반환
    if array[mid] ==  target:
        return mid
    elif array[mid] < target:
        return binary_search(start,mid-1,target,array)
    else:
        return binary_search(mid+1,end,target,array)

n,target = map(int,input().split())
array = list(map(int,input().split()))
print(binary_search(0,len(array)-1,target,array))

