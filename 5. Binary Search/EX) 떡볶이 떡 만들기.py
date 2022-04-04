import sys
n, m = map(int,sys.stdin.readline().rstrip().split())

dduk = list(map(int,sys.stdin.readline().rstrip().split()))

# 정렬
dduk.sort()

start = 0   # dduk[0] 이 아닌 이유: 만약 주어진 떡 길이대로 가져가려면 절단기로 자르면 안됨
end = dduk[-1]

result = 0

while start <= end:
    
    # 잘린 길이 총합
    total = 0
    # 절단기 길이
    mid = (start+end) // 2

    for x in dduk:
        if x > mid:
            total += x - mid
    
    # 만약 잘린 길이 총합이 손님이 원하는 것보다 많거나 같으면,
    if total >= m:
        # 일단 결과 저장
        result = mid
        # 절단기 길이를 늘려서 실험
        start = mid + 1

    # 만약 잘린 길이 총합이 손님이 원하는 것보다 적으면,
    else:
        # 절단기 길이를 줄여서 실험
        end = mid - 1

print(result)