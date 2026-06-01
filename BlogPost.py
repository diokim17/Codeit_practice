# BlogUser 클래스를 정의해 보세요.

# 인스턴스 변수(타입)

# name(문자열): 블로그 사용자의 이름
# posts(리스트): 블로그 게시글들을 담을 리스트
# 메소드

# __init__: 인스턴스 변수가 설정되는 메소드
# add_post: 블로그 사용자의 블로그 게시글 리스트에 새로운 게시글 인스턴스를 추가하는 메소드
# show_all_posts: 블로그 사용자가 올린 모든 게시글을 출력하는 메소드
# __str__: 블로그 사용자의 간단한 인사와 이름을 문자열로 리턴하는 메소드

class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return f"작성 날짜: {self.date}\n내용: {self.content}"
    
    
class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        self.posts.extend([date, content])

    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        self.Post(posts)

    def __str__(self):
        # 간단한 인사와 이름을 문자열로 리턴
        return f"안녕하세요 {self.name}입니다.\n"
    
    

# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이었다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()

# 피드백
# add_post 메소드에서 self.posts.extend([date, content]) 이렇게 하면, posts 리스트에 날짜와 내용이 각각 원소로 들어가게 된다.
# 실제로는 Post 인스턴스(게시글)를 만들어야 한다. 즉, Post(date, content)로 만든 객체를 리스트에 추가해야 한다.
# show_all_posts 메소드에서 self.Post(posts)는 올바른 사용법이 아니다. Post는 별도의 클래스이고, posts는 현재 클래스의 리스트이기 때문에 이렇게 호출하면 에러가 난다.
# 모든 게시글을 출력하려면, posts 리스트를 반복문으로 순회하면서 각 게시글(Post 인스턴스)를 출력해야 한다.


# 모범답안
class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return f"작성 날짜: {self.date}\n내용: {self.content}"
    
    
class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        for i in self.posts:
            print(i)

    def __str__(self):
        # 간단한 인사와 이름을 문자열로 리턴
        return f"안녕하세요 {self.name}입니다.\n"
    
    

# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이었다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()


# 알게 된 점
# 클래스 내에서 메소드를 사용할 때는 self.메소드() 식으로 쓰는 것
# self.Post() → BlogUser 클래스 내에 별도의 Post 메소드나 속성이 없어서 에러가 난다.
# 클래스는 코드 어디서든 사용할 수 있다.
# 즉, 클래스를 정의하면 같은 파일 내에 어디서든 사용가능하다.
# 클래스(...)로 새 객체를 만들면, 자동으로 클래스의 __init__ 메소드가 호출된다.
# 즉, 클래스 이름 뒤에 ()를 쓰면 __init__ 메소드가 자동으로 실행된다.