import random

words_dict = {}

with open("codeit_practice\\data\\voca.txt", "r", encoding="utf-8") as f:
    for voca in f:
        words = voca.strip().split(": ")
        eng = words[0]
        kor = words[1]

        words_dict[eng] = kor

while True:
    eng = random.choice(list(words_dict.keys()))
    kor = words_dict[eng]

    answer = input("{}: ".format(kor))

    if answer == "q":
        break

    if answer == eng:
        print("맞았습니다!")

    else:
        print("틀렸습니다. 정답은 {}입니다.".format(eng))


# 딕셔너리는 key -> value 형태로 저장함.
# dict[key]를 통해 value를 조회할 수 있음.
# 반대인 value로 key를 찾을 수 없음.
# random.choice()는 random.choice(리스트)처럼 사용해야 함.
# 문제에서 요구한 것은 한국어로 출제하고 영어로 답안을 제출하는 것임.
# 따라서 한국어를 랜덤 선택하는 방식이 직관적임.
# 다만 현재 작성된 딕셔너리의 키가 영어이므로 영어를 랜덤으로 출제하고
# 그 영어인 키를 딕셔너리에서 값을 찾아 출제를 함.