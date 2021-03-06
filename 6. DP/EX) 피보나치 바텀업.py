# 앞서 계산된 결과를 저장하기 위한 리스트 초기화
d = [0] * 100           # dp 테이블

# Bottum-up (반복문)
# 작은 문제부터 차근차근 해결해나감

d[1] = 1
d[2] = 1

# 피보나치 함수 반복문으로 구현
for i in range(3, 100):
    d[i] = d[i-1] + d[i-2]

print(d[99])    