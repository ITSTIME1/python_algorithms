N = int(input())
a_number = list(map(int, input().split()))
b_number = list(map(int, input().split()))

a_number.sort(reverse=True)
b_number.sort()
result = 0

for i in range(N):
  result += a_number[i] * b_number[i]

  if(i > N):
    break
print(result)
    