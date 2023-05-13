from collections import Counter

def buy_shoe(size: int, shoes: Counter):
    status: int = shoes[size]
    if status != 0:
        shoes[size] -= 1
    
    return 1 if status != 0 else 0

nShoes: int = int(input())
shoesSize: Counter = Counter(map(int, input().split(" ")[:nShoes]))
nClients: int = int(input())
total: int = 0

for i in range(nClients):
    request: list = list(map(int, input().split(" ")[:2]))
    status: int = buy_shoe(request[0], shoesSize)
    if status == 1:
        total += request[1]

print(total)
