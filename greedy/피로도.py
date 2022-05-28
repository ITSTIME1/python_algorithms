a, b, c, m = map(int, input().split())


piro = 0
work = 0
for i in range(1, 25):
  if piro + a <= m:
    piro += a
    work += b
  else:
    if piro-c >= 0:
      piro-=c
    else:
      piro = 0


print(work)
    
    