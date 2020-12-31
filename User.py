from collections import defaultdict

# 참고 url : https://mino-park7.github.io/effective%20python%20study/2018/10/04/betterway22-minhopark/
class User:
    def __init__(self, id, pwd):
        # 사용자 개인정보
        self.id = id
        self.pwd = pwd
        # 영화별, 장르별, 감독별 별점들이 담긴 리스트를 저장할 딕셔너리
        self.movie = {}
        self.genre = {}
        self.director = {}
        # 영화별 별점과 장르별, 감독별 평균 별점을 저장할 딕셔너리
        self.movie_scores = {}
        self.avg_genre_score = {}
        self.avg_director_score = {}

    # 딕셔너리에 없는 새로운 영화, 장르, 감독이 추가될 때 빈리스트 생성
    def add_new_data(self, movie_name, genre_name, director_name):
        if movie_name not in self.movie:
            self.movie[movie_name] = []
        if genre_name not in self.genre:
            self.genre[genre_name] = []
        if director_name not in self.director:
            self.director[director_name] = []

    # 별점을 리스트에 추가. 영화는 동일한 영화인 경우 별점 갱신 처리
    def report_score(self, movie_name, genre_name, director_name, score):
        if movie_name in self.movie:
            self.movie[movie_name] = score
        else:
            self.movie[movie_name].append(score)
        self.genre[genre_name].append(score)
        self.director[director_name].append(score)

    # 영화는 동일한 영화일 경우 별점 갱신 처리하고, 장르와 감독 별점 리스트는 평균값을 구해서 업데이트
    def evaluate_movie(self, movie_name, genre_name, director_name):
        self.movie_scores[movie_name] = self.movie[movie_name]

        genre_scores = self.genre[genre_name]
        self.avg_genre_score[genre_name] = sum(genre_scores) / len(genre_scores)

        director_scores = self.director[director_name]
        self.avg_director_score[director_name] = sum(director_scores) / len(director_scores)

    def change_pwd(self):
        pass

user_list = []
user_list_id = []
id = input("ID를 입력하세요 : ")
pwd = input("비밀번호를 입력하세요 : ")

# for i in range(len(user_list)):
#     if id not in user_list_id:
user = User(id,pwd)
user_list.append(user)
user_list_id.append(id)

for idx in range(len(user_list)):   # 인덱스를 찾아서 해당 인스턴스에 접근
    if user_list[idx].id == id:
        user_list[idx].add_new_data('명량','사극','김한민')
        user_list[idx].report_score('명량','사극','김한민',4)
        user_list[idx].evaluate_movie('명량','사극','김한민')
        print("영화 :", user_list[idx].movie)
        print("장르 :", user_list[idx].genre)
        print("감독 :", user_list[idx].director)
        print("영화 별점 :", user_list[idx].movie_scores)
        print("장르 평균 별점 :", user_list[idx].avg_genre_score)
        print("감독 평균 별점 :", user_list[idx].avg_director_score)

for idx in range(len(user_list)):   # 인덱스를 찾아서 해당 인스턴스에 접근
    if user_list[idx].id == id:
        user_list[idx].add_new_data('명량','사극','김한민')
        user_list[idx].report_score('명량','사극','김한민',2)
        user_list[idx].evaluate_movie('명량','사극','김한민')
        print("영화 :", user_list[idx].movie)
        print("장르 :", user_list[idx].genre)
        print("감독 :", user_list[idx].director)
        print("영화 별점 :", user_list[idx].movie_scores)
        print("장르 평균 별점 :", user_list[idx].avg_genre_score)
        print("감독 평균 별점 :", user_list[idx].avg_director_score)

for idx in range(len(user_list)):   # 인덱스를 찾아서 해당 인스턴스에 접근
    if user_list[idx].id == id:
        user_list[idx].add_new_data('신세계','범죄','박훈정')
        user_list[idx].report_score('신세계','범죄','박훈정',5)
        user_list[idx].evaluate_movie('신세계','범죄','박훈정')
        print("영화 :", user_list[idx].movie)
        print("장르 :", user_list[idx].genre)
        print("감독 :", user_list[idx].director)
        print("영화 별점 :", user_list[idx].movie_scores)
        print("장르 평균 별점 :", user_list[idx].avg_genre_score)
        print("감독 평균 별점 :", user_list[idx].avg_director_score)