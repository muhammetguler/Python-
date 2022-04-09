money_Requested = int(input())
numberOf_5TL = int(input())

if (money_Requested // 5) <= numberOf_5TL:
    print(money_Requested // 5, money_Requested % 5)
else:
    print(numberOf_5TL, money_Requested - (5 * numberOf_5TL))



