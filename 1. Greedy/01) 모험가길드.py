N = int(input())
cnt = 0             # 총 결성된 그룹 수
cur = 0             # 현재 인덱스 위치

data = list(map(int, input().split()))

data.sort()


if N < data[0]:     # 만약 제일 낮은 공포도가 전체 모험가 수 이상이라면, 그룹 결성 불가
    print(cnt)
else:
    while data[cur] + cur - 1 < N:      # (현재 인덱스 위치의 공포도 + 현재 인덱스 위치 - 1)  ->  현재 인덱스의 모험가가 데려가야하는 인원 중 제일 큰 공포도
        if data[data[cur] + cur - 1] <= data[cur]:         # 현재 그룹 중 제일 큰 공포도도 포함이 가능하면
            cnt += 1                                        # 그룹 결성
            cur += data[cur]                                
        else:
            break;
    print(cnt)


