import pyupbit

access = "ZbStbj0rtWGSkpjlIcX5jjRQnxAdlaawAZyqShXV"          # 본인 값으로 변경
secret = "yrlsqT6URMWxm4N1MxyVqfXpKAPmMzEPpWt0aTtg"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETH"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회