def where_column(k):
    columns = ['a','b','c','d','e','f','g','h']
    for i in range(len(columns)):
        if k == columns[i]:
            return i

# column = int(ord(now[0])) - int(ord('a'))

now = input()
row = int(now[1])-1 
column = where_column(now[0])

knights = [(-2,-1),(-2,1),(1,-2),(-1,-2),(2,1),(2,-1),(1,2),(-1,2)]

result = 0

for knight in knights:
    dx = column + knight[0]
    dy = row + knight[1]
    if dx >= 0 and dy >= 0 and dx < 8 and dy < 8:
        result += 1

print(result)
