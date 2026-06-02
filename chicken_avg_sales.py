# 12월 매출이 정리되어 있는 파일을 읽어 하루 평균 매출을 출력하세요.
# 제공된 파일을 31일이지만 어떤 달은 31일이 아닐 수도 있습니다.
# 확장성 있는 코드를 작성하세요.

total_sales = 0
day = 0

with open("codeit_practice\\data\\chicken.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = line.strip().split(": ")

        sales = int(data[1])
        total_sales += sales
        day += 1

print(total_sales / day)