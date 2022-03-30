from collections import deque

n, m = map(int, input().split())
ice = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for _ in range(n):
    ice.append(list(map(int,input())))

def bfs(x,y):
    queue = deque()
    queue.appendleft((x,y))

    if ice[x][y] == 1:
        return False

    while(queue):
        cur_x, cur_y = queue.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if ice[nx][ny] == 1:
                continue
            if ice[nx][ny] == 0:
                queue.appendleft((nx,ny))
                ice[nx][ny] = 1
    return True

count = 0
for i in range(n):
    for j in range(m):
        if bfs(i,j):
            count += 1
print(count)