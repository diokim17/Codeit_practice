# 영단어장을 만든다.
# 1. 영어 단어를 입력 받는다.
# 2. 만약 유저가 q를 입력했으면 프로그램을 종료한다.
# 3. 한국어 뜻을 받는다.
# 4. 만약 유저가 qqq를 입력했으면 프로그램을 종료한다.
# 5. 영어 단어와 한국어 뜻을 단어: 뜻의 형태로 파일에 작성한다.

with open("codeit_practice\\data\\단어장.txt", "a", encoding="utf-8") as f:
    while True:
        eng = input("영어 단어를 입력하세요: ")
        if eng == "qqq":
            break
        kor = input("한국어 뜻을 입력하세요: ")
        if kor == "qqq":
            break

        f.write("{}: {} \n".format(eng, kor))
