# 리스트 내 요소들의 순서를 거꾸로 뒤집으려고 한다.
# numbers라는 리스트가 주어졌을 때, for 문을 사용하여 리스트를 거꾸로 뒤집어라.

# 나의 아이디어
# 1. 빈 리스트를 하나 생성한다.
# 2. 기존 리스트를 for 문으로 순회한다.
# 3. 순회하면서 기존 리스트의 요소를 새로 만든 빈 리스트의 맨 앞에 추가한다.
# 4. 순회가 끝나면 새로 만든 리스트가 기존 리스트의 요소들이 거꾸로 뒤집힌 형태가 된다.
# 5. 새로 만든 리스트를 기존 리스트에 할당한다.

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 여기에 코드를 작성하세요
numbers_revert = []

for i in numbers:
    numbers_revert.insert(0, i)

numbers = numbers_revert
    
print("뒤집어진 리스트: " + str(numbers))



# 답안 1
# 1. 리스트의 왼쪽 인덱스와 오른쪽 인덱스를 서로 대칭되도록 설정한다.
# 2. 왼쪽 값과 오른쪽 값을 서로 교환(swap)한다.
# 3. 리스트의 양쪽에서 가운데 방향으로 이동하며 같은 작업을 반복한다.
# 4. 이미 교환된 값은 다시 바꿀 필요가 없으므로 리스트 길이의 절반까지만 반복한다.
# 5. 홀수 길이 리스트의 경우 가운데 값은 자기 자신과 대칭이므로 그대로 둔다.

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))

# 이 때, 튜플 자료형을 이용하면 41~44번 줄의 위치 바꾸기 코드를 더 간결하게 작성할 수 있다.
# numbers[right], numbers[left] = numbers[left], numbers[right]