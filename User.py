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
		self.movie_scores = {}
		self.avg_genre_score = {}
		self.avg_director_score = {}
	
	def select_option(self):
		try:
			opt = int(input("메뉴를 선택해주세요: "))
			return opt
		except:
			print("error: 숫자가 아닙니다.")
			print("다시 선택해주세요.")
			return -1

	def change_pwd(self):
		current_pwd = input("현재 비밀번호를 입력해주세요: ")
		if current_pwd != self.pwd:
			print("비밀번호가 틀렸습니다.")
		else:
			new_pwd = input("새로운 비밀번호를 입력해주세요: ")
			self.pwd = new_pwd
