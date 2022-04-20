city_number = int(input())

load_length = list(map(int, input().split()))

oil_price = list(map(int, input().split()))

# 처음엔 기름이 없어서 첫 주유소부터 출발하기 때문에 첫 주유소에 있는 가격을 넣어준다.
first_price = oil_price[0]
# 처음 부터 끝까지 확인해주어야된다.


total = 0
for i in range(len(load_length)):

  # 
  if oil_price[i] >= first_price:
    total += first_price * load_length[i]

  elif oil_price[i] < first_price:
    first_price = oil_price[i]
    total += first_price * load_length[i]
    
print(total)