N = int(input())
result = 0             # 총 결성된 그룹 수
count = 0             # 현재 그룹에 포함된 모험가의 수

data = list(map(int, input().split()))

data.sort()

for x in data:              # 모든 모험가에 대하여
    count += 1              # 일단 각자 그룹을 결성 해봄
    if count >= x:                  # *** 만약 현재 그룹 구성원이 지금 구성원 공포도보다 크거나 같은순간 ***
        result += 1         # 결성된 그룹 그대로 출발
        count = 0           # 다시 그룹 초기화

print(result)        