# 파일의 단어들을 가지고 학생들에게 문제를 내는 프로그램을 만들려고 합니다.
# 프로그램은 터미널에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다.
# 사용자가 입력한 영어 단어가 정답이면 맞았습니다!라고 출력하고, 틀리면 아쉽습니다. 정답은 OOO입니다.가 출력되어야 합니다.
# 문제를 내는 순서는 voca.txt에 정리된 순서입니다.

with open("codeit_practice\\data\\voca.txt", "r", encoding="utf-8") as f:
    for voca in f:
        words = voca.strip().split(": ")
        # print(words[0]) # 영어
        # print(words[1]) # 한국어
        eng = words[0]
        kor = words[1]

        answer = input("{}: ".format(kor))

        if eng == answer:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(eng))
