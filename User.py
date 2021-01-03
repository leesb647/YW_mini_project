from collections import defaultdict
from msvcrt import getch	# 키보드 입력 받는 getch() 함수를 사용하기 위해 import
import time		# time.sleep(시간) 함수로 버퍼링 효과
import random
# 참고 url : https://mino-park7.github.io/effective%20python%20study/2018/10/04/betterway22-minhopark/
class User:
	opt_list=["로그아웃", "비밀번호 변경하기", "영화추천 보기", "별점 주기"]
	def __init__(self, id, pwd, name):
		# 사용자 개인정보
		self.id = id
		self.pwd = pwd
		self.name = name
		# 영화별, 장르별, 감독별 별점들이 담긴 리스트를 저장할 딕셔너리
		self.movie = defaultdict(list)
		self.genre = defaultdict(list)
		self.director = defaultdict(list)
		# 영화별 별점과 장르별, 감독별 평균 별점을 저장할 딕셔너리
		#self.movie_scores = defaultdict(float)
		self.avg_genre_score = defaultdict(float)
		self.avg_director_score = defaultdict(float)
	
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

	def rate_selected_movie(self, movie_data, movie_index_dict):
		while True:
			movie = input("영화 이름을 입력하세요 : ")  # 영화명으로 영화를 선택
			idx = movie_index_dict[movie]
			selected_movie_data = movie_data.loc[idx]
			if movie == '0':
				break
			return self.rate_movie(selected_movie_data, movie), selected_movie_data
			print("영화 추천 데이터에 존재하지 않는 영화입니다. 다시 입력하거나 나가시려면 0번을 입력하세요.")

	def rate_random_movie(self, movie_data, movie_index_dict):
		movie = random.choice(movie_data.영화명)	# 랜덤으로 영화를 결정
		idx = movie_index_dict[movie]
		selected_movie_data = movie_data.loc[idx]
		return self.rate_movie(selected_movie_data, movie), selected_movie_data

	def rate_movie(self, movie_data, movie):	# 영화에 별점을 부여하는 함수
		print("="*150)
		print("{:^30}{:^20}{:^10}{:^10}{:^20}{:^10}{:^20}".format("영화명", "개봉일", "관객수", "제작국가", "장르", "제작상태", "감독"))
		print("="*150)
		# 랜덤으로 정해진 영화의 정보를 출력
		print("{:^30}{:^23}{:^13}{:^12}{:^19}{:^13}{:^20}".format(movie_data.영화명, str(movie_data.개봉일.date()), str(movie_data.관객수), movie_data.제작국가, movie_data.장르, movie_data.제작상태, movie_data.감독))
		print("="*150)
		print("")
		print("{:^100}".format("영화 별점(좌우(← →) 방향키로 변경, 입력하려면 enter, 나가려면 0번이나 esc를 입력하세요)"))
		n = 3
		while True:
			print("\t\t\t\t\t\t\t\t", end='')
			print('{}{}'.format('★' * n, '☆' * (5 - n)), end='\r')
			time.sleep(0.5)
			key = str(ord(getch()))  # getch 함수로 방향키 및 엔터키를 입력받음
			if key == '75' or key == '80':  # 75(left), 80(down)
				if n != 1:
					n -= 1
			elif key == '77' or key == '72':  # 77(right), 72(up)
				if n != 5:
					n += 1
			elif key == '13':  # 13(enter)
				print("\t\t\t\t\t\t\t\t", end='')
				print('{}{}'.format('★' * n, '☆' * (5 - n)), end='\n\n')
				return n  # 영화의 별점 값(n)을 리턴
			elif key == '27' or key == '48':  # 27(esc), 48(0)
				break
