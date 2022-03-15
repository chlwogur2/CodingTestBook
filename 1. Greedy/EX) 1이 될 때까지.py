n, k = map(int, input().split())
cnt = 0

while n > 1:
    if n%k != 0:
        n -= 1
        cnt += 1
    else:
        n /= k    
        cnt += 1        

# target = (n//k) * k  
# 이런 식으로 짜면 n 에 제일 가까운 배수가 됨

print(cnt)