n, m = map(int, input().split())

result = 0 

for _ in range(n):
    card = list(map(int, input().split()))
    min_value = min(card)
    result = max(result,min_value) 

# min_card = []
# for i in range(n):
#     min_card.append(min(card[i]))

print(result)