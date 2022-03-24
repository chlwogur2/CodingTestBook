n, m = map(int, input().split())
ice = []

for _ in range(n):
    ice.append(list(map(int, input())))

def dfs(x,y):

    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    else:
        return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            count += 1

print(count)        