
# Solution 1
number = int(input())
start = 1
room = 1
count = 0

def solution(number):
  global start
  global room
  global count 

  
  while number > room:
    room += count * 6
    count += 1

solution(number)
print(count)



# Solution 2
number = int(input())
start = 1
room = 1
count = 0

while number > room:
  room += count * 6
  count += 1

print(count)

