from collections import defaultdict

# 참고 url : https://mino-park7.github.io/effective%20python%20study/2018/10/04/betterway22-minhopark/
class User:
	opt_list=["로그아웃", "비밀번호 변경하기", "영화추천 보기", "별점 주기"]
	def __init__(self, id, pwd, name):
		# 사용자 개인정보
		self.id = id
		self.pwd = pwd
		self.name = name
		# 영화별, 장르별, 감독별 별점들이 담긴 리스트를 저장할 딕셔너리
		self.movie = defaultdict(float)
		self.genre = defaultdict(float)
		self.director = defaultdict(float)
		# 영화별 별점과 장르별, 감독별 평균 별점을 저장할 딕셔너리
		#self.movie_scores = {}
		#self.avg_genre_score = {}
		#self.avg_director_score = {}
	'''
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
	'''
	def change_pwd(self):
		current_pwd = input("현재 비밀번호를 입력해주세요: ")
		if current_pwd != self.pwd:
			print("비밀번호가 틀렸습니다.")
		else:
			new_pwd = input("새로운 비밀번호를 입력해주세요: ")
			self.pwd = new_pwd
