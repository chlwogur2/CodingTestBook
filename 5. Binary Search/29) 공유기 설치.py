import sys

house = []
n, c = map(int,sys.stdin.readline().rstrip().split())

# 결과
result = 0

for _ in range(n):
    house.append(int(sys.stdin.readline().rstrip()))
    
# 집 좌표 오름차순으로 정렬    
house.sort()
    
# 공유기를 설치한 두 집 사이의 거리의 최소, 최대
# 얘네들 사이의 값이 공유기를 설치할 수 있는 거리값
min_distance = 1
max_distance = house[-1] - house[0]

# 두 집 사이의 거리를 점점 늘리거나 줄이면서, 공유기를 c대를 설치할 수 있는지 체크
def binary_search(min_distance,max_distance):
    global result
    while min_distance <= max_distance:
        
        # 현재 설치할 공유기 사이의 거리 중 가장 인접한 애
        mid = (min_distance + max_distance) // 2
        # 설치한 공유기 수 초기화
        count = 1
        # 현재 공유기를 설치한 위치
        current = 0
        
        # 공유기 거리 별로 쭈욱 설치
        for i in range(1,len(house)):
            # 만약 설치하려고 하는 집의 좌표가 현재 좌표에 거리 더한 값보다 멀면 설치
            if house[i] >= house[current] + mid:
                count += 1
                current = i
        # 만약 설치된 공유기 대수가 필요한 공유가 대수보다 적다면,
        if count < c:
            # 거리를 좁혀서 설치
            max_distance = mid - 1
        # 설치된 공유기 대수가 필요한 공유기 대수보다 많거나 같다면,
        elif count >= c:
            # 거리를 늘려도 됨
            min_distance = mid + 1
            # 거리 저장
            result = mid

binary_search(min_distance,max_distance)
print(result)