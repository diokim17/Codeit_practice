# 주민등록번호 YYMMDD-abcdefg는 총 열세 자리인데요.
# 주민등록번호의 마지막 네 자리 defg만 가려 주는 보안 프로그램을 만들려고 합니다.
# mask_security_number라는 함수를 정의하려고 하는데요. 이 함수는 파라미터로 문자열 security_number를 받고, 
# security_number의 마지막 네 글자를 '*'로 대체한 새 문자열을 리턴합니다.
# 참고로 파라미터 security_number에는 작대기 기호(-)가 포함될 수도 있고, 포함되지 않을 수도 있는데요.  
# 작대기 포함 여부와 상관 없이, 마지막 네 글자가 '*'로 대체되어야 합니다!

# 내가 작성한 답
def mask_security_number(security_number):
    # 여기에 코드를 작성하세요
    if "-" in security_number:
        mask_number = security_number[10:]
        mask_number = "****"
        security_number = security_number[:10] + mask_number
    else:
        mask_number = security_number[9:]
        mask_number = "****"
        security_number = security_number[:9] + mask_number
        
    
    return security_number


# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

# 그냥 마지막 네자리만 ****로 작성하면 되는 거 아닌가 하고 아래와 같이 작성했었다.
def mask_security_number(security_number):
    # 여기에 코드를 작성하세요
    mask_number = security_number[10:]
    mask_number = "****"
    security_number = security_number[:10] + mask_number
    
    return security_number

# 이 때, 문제가 발생했다. 
# security_number에 작대기(-)가 포함되어 있지 않은 경우, 주민번호가 14자리가 되어버리는 것이다.
# 그래서 security_number에 작대기(-)가 포함되어 있는지에 꽂혀서 if문을 작성했다.

# 하지만 더 간단한 방법이 있었다.
# 원래 생각한 아이디어대로 security_number의 마지막 네 글자를 ****로 대체하면 되는 것이었다.
# 즉, 앞에서부터 슬라이싱하는 것이 아닌 뒤에서 슬라이싱을 하여 마지막 네 글자를 ****로 대체하면 되는 것이었다.

# 그럼 아래와 같이 작성할 수 있다.
def mask_security_number(security_number):
    return security_number[:-4] + '****'


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

