# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

# Top-down (재귀)
# 큰 문제를 해결하기 위해 작은 문제를 호출함
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 피보나치 수열이면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산한 적 없는 피보나치 수열이면 점화식
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))            