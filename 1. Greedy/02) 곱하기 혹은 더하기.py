data = list(map(int,input())) 
result = 0      # 결과

for x in data:      # 데이터들 순회하면서
    if x == 0:      # 만약 0이면 스킵
        continue
    elif x == 1:        # 1이면 곱하기말고 더하기
        result += 1
    else:               # 2~9 중 하나면
        if result == 0:     # 만약 현재 값이 0 이면 곱하면 안되니까
            result += x     # 더하기
        else:
            result *= x

print(result)