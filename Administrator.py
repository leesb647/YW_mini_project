import math
import sys
from datetime import datetime

class Administrator:
	opt_list = ["로그아웃", "데이터 관리하기", "유저목록", "공지사항 보내기"]
	def __init__(self, id, pwd, name):
		self.id = id
		self.pwd = pwd
		self.name = name

	def select_option(self):
		try:
			opt = int(input("메뉴를 선택해주세요: "))
			return opt
		except:
			print("error: 숫자가 아닙니다.")
			print("다시 선택해주세요.")
			return -1

	def write_notice(self):
		while True:
			print("user에게 보낼 공지사항을 입력하세요.", "입력을 마치려면 Ctrl  + z")
			notice_input = [line.rstrip() for line in sys.stdin.readlines()]
			print()
			print("user에게 공지될 내용은 다음과 같습니다.")
			print()
			for i in notice_input:
				print(i)
			print()
			print(notice_input)
			return notice_input

	def manage_data(self, movie_data):
	# 영화 제목에 근거해서 데이터프레임 인덱스에 접근. 영화 제목, 감독, 장르 등 데이터 수정 가능하도록 변경
		pass

	def add_movie_data(self, data):
	# 데이터프레임 영화데이터 추가
		sel = {1:'개봉일', 2:'관객수', 3:'스크린수', 4:'제작국가', 5:'유형', 6:'장르', 7:'제작상태', 8:'감독'}
		name = input('추가할 영화명을 입력하세요: ')
		data = data.append({'영화명': name}, ignore_index=True)
		data.at[data.index[-1],'장르'] = []		# Pandas에서 df.loc으로 list가 입력값으로 삽입되지 않을때, df.at을 사용한다
		data = data.fillna('No data')	# NaN을 모두 0으로 변경
		data.loc[data.index[-1],'개봉일'] = datetime(1, 1, 1)	# 개봉일 NaN값을 datetime 타입으로 만들기 위함
		while True:
			code = int(input('추가할 영화 정보를 입력하세요\n(0:종료, 1:개봉일, 2:관객수, 3:스크린수, 4:제작국가, 5:유형, 6:장르, 7:제작상태, 8:감독) \n:'))
			if code == 0:
				break
			elif code == 6:
				while True:
					value = input('%s을(를) 입력하세요(0:종료): ' %sel[code])
					if value == '0':
						break
					data.loc[data.index[-1], '장르'].append(str(value))	# 장르의 경우 리스트에 str타입으로 추가
			else:
				value = input('%s을(를) 입력하세요: ' %sel[code])
				data.loc[data.index[-1], sel[code]] = value
			print('\n', data.iloc[data.index[-1]], '\n')
		print(data.tail)
		return data

	def delete_movie_data():
	# .drop 영화데이터 삭제
		pass