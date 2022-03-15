n = int(input())

map = [[0 for _ in range(n)] for _ in range(n) ] 
curX, curY = 1,1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
move = ['U','D','L','R']

command = list(input().split())

for x in command:
    for i in range(len(move)):
        if x == move[i]:
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx > n or ny > n or nx < 1 or ny < 1:        # 시작 좌표가 (0,0) 이 아니고 (1,1) 이므로 좌표값은 (n,n) 까지 가능
                continue
            curX, curY = nx, ny
            continue

print(curX, curY)
