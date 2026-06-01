#  두 플레이리스트를 + 연산자를 통해서 더할 수 있게 하고 싶은데요.

# us_pop_2010s이 2010년대 미국 팝 플레이리스트, 
# k_pop_2010s가 2010년대 한국 대중 음악 플레이리스트 인스턴스일 때, 
# 아래 코드로 두 플레이리스트에 있는 모든 노래가 들어있는 새로운 플레이리스트를 리턴되게 하고 싶습니다.

# 실행 결과
# 플레이리스트 안 노래들:

# Rolling in the Deep - Adele (2011)
# Call Me Maybe - Carly Rae Jepsen (2012)
# Get Lucky - Daft Punk (2013)
# Uptown Funk - Mark Ronson (2015)
# Pallete(팔레트) - 아이유 (2017)
# 피 땀 눈물 - 방탄소년단 (2016)
# TT - 트와이스 (2016)


class Song:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.year})"


class PlayList:
    def __init__(self, songs):
        self.songs = songs

    def __str__(self):
        result = f"플레이리스트 안 노래들:\n\n"
        for song in self.songs:
            result += f"{song}\n"
        return result

    # 여기 코드를 쓰세요
    def __add__(self, other_playlist):
        new_playlist = self.songs + other_playlist.songs
        return PlayList(new_playlist)


# 실행 코드
rolling_in_the_deep = Song("Rolling in the Deep", "Adele", 2011)
call_me_maybe = Song("Call Me Maybe", "Carly Rae Jepsen", 2012)
get_lucky = Song("Get Lucky", "Daft Punk", 2013)
uptown_funk = Song("Uptown Funk", "Mark Ronson", 2015)

palette = Song("Pallete(팔레트)", "아이유", 2017)
blood_sweat_and_tears = Song("피 땀 눈물", "방탄소년단", 2016)
tt = Song("TT", "트와이스", 2016) # 송 인잇은 끝

us_pop_2010s = PlayList([rolling_in_the_deep, call_me_maybe, get_lucky, uptown_funk])
k_pop_2010s = PlayList([palette, blood_sweat_and_tears, tt])

pop_2010s = us_pop_2010s + k_pop_2010s
print(pop_2010s)
