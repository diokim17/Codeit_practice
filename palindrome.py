# "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 '팰린드롬(palindrome)'이라고 부릅니다.
# 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성하려고 하는데요. 
# is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.
# 예를 들어서 "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 합니다. 
# 그리고 "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야 하는 거죠.

# 내가 작성한 코드
def is_palindrome(word):
    # 여기에 코드를 작성하세요
    reverse_word = []
    
    for w in word:
        reverse_word.insert(0, w)
    
    reverse_word = ''.join(reverse_word)
    
    if reverse_word == word:
        
        return True
    else:
        return False


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

# 빈 리스트를 만들어서 for문으로 word의 각 글자를 순회하면서 빈 리스트의 맨 앞에 글자를 추가하는 방식으로 reverse_word를 만들었다.
# 이 때, reverse_word = ''.join(reverse_word)를 작성하지 않아서 reverse_word가 ['r', 'a', 'c', 'e', 'c', 'a', 'r']과 같이 리스트 형태로 되어 있었다. 
# 그래서 reverse_word와 word가 서로 다른 자료형이기 때문에 비교할 때 False가 나왔던 것이다.

# 하지만 더 간단한 방법이 있었다.
def is_palindrome(word):
    return word == word[::-1]


# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

# word[::-1]은 word의 글자들을 뒤에서부터 하나씩 가져와서 새로운 문자열을 만드는 것이다.
# word[::-1] 이 부분을 실행해보면 racecar, srats, 토마토, kayak, olleh가 나온다.

'''
'구분자'.join(리스트) 설명
join() 메서드는 문자열을 구분자로 하여 리스트의 요소들을 하나의 문자열로 합치는 역할을 한다.
위에서 작성한 코드에서는 빈 문자열 ''을 구분자로 사용하여 reverse_word 리스트의 요소들을 하나의 문자열로 합쳤다.
['r', 'a', 'c', 'e', 'c', 'a', 'r']의 리스트가 'racecar'라는 문자열로 합쳐진 것이다.

실제로 회사를 다녔을 때, join() 메서드를 자주 사용했었다.
그 때는 라벨링한 데이터를 _로 구분하여 하나의 문자열로 합쳐야 하는 경우가 많았었다.

더더욱 해당 메서드를 잊지 말아야 겠다.

----------------------------------------------
[::-1] 설명

기본 구조는 문자열[시작:끝:간격]
따라서 위 구조를 설명하면 시작 생략으로 끝에서부터 시작, 끝 생략으로 처음까지, 간격 -1은 뒤로 한 칸씩 이동으로
"뒤에서부터 앞으로 한 글자씩 가져와라" 이다.

흔히 사용하는 슬라이싱은 문자열[시작:끝] 이다. 예를 들어서 word[0:3]은 word[0:3:1]로 간격 1이 생략된 것이다.
또한 [::1]은 문자열 전체를 간격 1로 가져오라는 의미이다. 따라서 word[::1]은 word와 같은 문자열이 된다.
즉, word[::1] == word 이다.

따라서 간격이 -1, 시작이 생략되어서 끝에서 시작하는 것이었고 앞으로 한 글자씩 가져와서 새로운 문자열을 만든 것이다. 따라서 word[::-1]은 word의 글자들을 뒤에서부터 하나씩 가져와서 새로운 문자열을 만드는 것이다.
'''
