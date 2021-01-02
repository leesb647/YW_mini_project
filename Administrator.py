import math
import WebSite

class Administrator:
	def __init__(self, id, pwd, name):
		self.id = id
		self.pwd = pwd
		self.name = name

	def manage_data(self):
		pass

	def send_message(self):
		pass

	def show_all_users(self, user_list):
		# user_list = {'1': '영희', '2': '철수', '3': 'ㄱ', '4': 'ㄴ', '5': 'ㄷ'
		# 	, '6': 'ㄹ', '7': 'ㅁ', '8': 'ㅂ'}
		user_keys = list(user_list.keys())
		page = 1
		end_page = math.ceil(len(user_list) / 5)

		while True:
			print("=" * 80)
			print("")
			if page == end_page:
				for i in range(5 * (end_page - 1), len(user_list)):
					print("\t\t", user_keys[i], user_list[user_keys[i]], end="")
			else:
				for i in range(5 * (page - 1), 5 * page):
					print("\t\t", user_keys[i], user_list[user_keys[i]], end="")
			print("\n")
			print("=" * 80)
			select = int(input("메뉴를 선택하세요( 0.나가기 / 1.이전 / 2.다음 )  : "))
			if select == 0:
				break
			elif select == 1:
				if page == 1:
					pass
				else:
					page -= 1
			elif select == 2:
				if page == end_page:
					pass
				else:
					page += 1
