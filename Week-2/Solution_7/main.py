requestedMoney = int(input())
banknotes = int(requestedMoney / 5) # requestedMoney // 5
coins = requestedMoney % 5

print(banknotes, coins)
