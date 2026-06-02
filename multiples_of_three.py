# 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.

# 내가 작성한 코드
def print_multiples_of_three(n):
  if n % 3 == 0:
    for i in range(1, n // 3 + 1):
      print(3 * i)
      i += 1
  else:
    remain = n % 3
    n = n - remain
    for i in range(1, n // 3 + 1):
      print(3 * i)
      i += 1


# 강사님 답안
def print_multiples_of_three(n):  
  for i in range(1, n + 1):  
    if i % 3 == 0:  
      print(i)

print_multiples_of_three(7)

# 주어진 수가 3의 배수인지 아닌지 판별 후 그에 맞게 코드를 작성했지만,
# 주어진 수가 아닌 범위라 생각하면, 주어진 범위 내에서 3의 배수만 출력하면 되는 것이었다.