import math
import sys

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
