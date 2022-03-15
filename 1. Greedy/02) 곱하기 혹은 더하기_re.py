data = list(map(int, input()))
result = data[0]        # 맨 첫번째 값을 결과에 대입

for i in range(1,len(data)):        
    if data[i] <= 1 or result <= 1:     # 만약 연산되는 두 숫자 중 하나라도 0 또는 1이면
        result += data[i]               # 더하기 수행
    else:       
        result *= data[i]               # 그거 아니면 곱하기

print(result)        



