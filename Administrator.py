import math
import WebSite

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
