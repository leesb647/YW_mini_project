import User
import Administrator
import pandas as pd
import math
import xlrd
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
'''

class WebSite:
	opt_list = ['나가기', '회원가입', '로그인']
	
	def __init__(self):
		admin = Administrator.Administrator('YW', '1234', '영우')
		self.users = {admin.id: admin}
		self.user = None
		self.movie_data = self.load_movie_data()
		self.load_data()

	def execute(self):
		self.show_start_page()

	def show_start_page(self):
		while True:
			if self.user is None:
				print("{:^80}".format("START PAGE"))
				self.print_menu(self.opt_list)
				opt = self.select_option()
				if opt == -1:
					continue
				elif opt == 1:
					self.sign_up()
				elif opt == 2:
					self.sign_in()
				elif opt == 3:
					self.sign_out()
				elif opt == 0:
					self.save_data()
					break
				else:
					self.out_of_range_error()
					continue
			elif isinstance(self.user, Administrator.Administrator):
				self.show_administrator_page()
			else:
				self.show_user_page()

	def show_administrator_page(self):
		while True:
			print("{:^80}".format("ADMINISTRATOR PAGE"))
			self.print_menu(Administrator.Administrator.opt_list)
			opt = self.select_option()
			if opt == -1:
				continue
			elif opt == 1:
				pass
			elif opt == 2:
				self.show_all_users_info_page()
			elif opt == 3:
				pass
			elif opt == 0:
				self.sign_out()
				break
			else:
				self.out_of_range_error()
				continue

	def show_user_page(self):
		while True:
			print("{:^80}".format("USER PAGE"))
			self.print_menu(User.User.opt_list)
			opt = self.user.select_option()
			if opt == -1:
				continue
			elif opt == 1:
				self.change_pwd_page()
			elif opt == 2:
				self.show_movie_recommendation_page()
			elif opt == 3:
				pass
			elif opt == 0:
				self.sign_out()
				break
			else:
				self.out_of_range_error()
				continue

	def show_movie_recommendation_page(self):
		while True:
			print("{:^80}".format("RECOMMENDATION PAGE"))
			menu = ["나가기", "관객수", "장르", "감독"]
			self.print_menu(menu)
			opt = self.user.select_option()
			if opt == -1:
				continue
			elif opt == 1:
				self.show_movie_recommendation_by_attendance()
			elif opt == 2:
				self.show_movie_recommendation_by_genre()
			elif opt == 3:
				self.show_movie_recommendation_by_attendance()
			elif opt == 0:
				break
			else:
				self.out_of_range_error()
				continue

	def show_movie_recommendation_by_attendance(self):
		current_page = 1
		end_page = (len(self.movie_data)//10) + 1
		while True:
			self.show_movie_table(current_page, end_page)
			if current_page == 1:
				menu = ["나가기", "다음", "소개"]
				self.print_menu(menu)
				if end_page == 1:
					menu = ["나가기", "소개"]
					self.print_menu(menu)
			elif current_page == end_page:
				menu = ["나가기", "이전", "소개"]
				self.print_menu(menu)
			else:
				menu = ["나가기", "이전", "다음", "소개"]
				self.print_menu(menu)
			opt = self.user.select_option()
			if opt == -1:
				continue
			elif opt < 0 or opt >= len(menu):
				self.out_of_range_error()
				continue

			if menu[opt] == "나가기":
				break
			elif menu[opt] == "다음":
				current_page += 1
			elif menu[opt] == "이전":
				current_page -= 1
			elif menu[opt] == "소개":
				menu2 = ["나가기"]
				if current_page == end_page:
					menu2 += [self.movie_data.영화명[i] for i in range((current_page - 1) * 10, len(self.movie_data))]
				else:
					menu2 += [self.movie_data.영화명[i] for i in range((current_page - 1) * 10, current_page * 10)]
				
				while True:
					self.print_menu(menu2)
					opt2 = self.user.select_option()
					if opt2 == -1:
						continue
					elif opt2 == 0:
						break
					elif opt2 > 0 and opt2 < len(menu2):
						self.show_movie_introduction(current_page, end_page, opt2)
					else:
						continue
			else:
				self.out_of_range_error()
				continue

	def show_movie_recommendation_by_genre(self):
		pass

	def show_movie_recommendation_by_directors(self):
		pass

	def sign_up(self):
		while True:
			id = input("아이디를 입력해주세요(특수문자 X): ")
			if not id.isalnum():
				print("error: 특수문자가 들어있습니다.")
				continue
			if id.upper() in self.users:
				print("error: 동일한 아이디가 있습니다.")
				continue
			pwd = input("비밀번호를 입력해주세요(\\사용불가): ")
			if '\\' in pwd:
				print("error: \\ 문자가 들어있습니다.")
				continue
			name = input("이름을 입력해주세요: ")
			if not name.isalpha():
				print("error: 문자가 아닙니다.")
			
			menu = ["나가기", "완료", "다시하기"]
			self.print_menu(menu)
			while True:
				opt = self.select_option()
				if opt == -1:
					continue
				elif opt < 0 and opt >= len(menu):
					self.out_of_range_error()
					continue
				else:
					break
			if opt == 0:
				break
			elif opt == 2:
				continue

			new_user = User.User(id, pwd, name)
			self.users[id.upper()] = new_user
			print("")
			print("축하합니다 ", id, "님")
			print("회원가입 완료되었습니다.")
			break

	def sign_in(self):
		while True:
			id = input("아이디를 입력해주세요: ")
			pwd = input("비밀번호를 입력해주세요: ")
			if id.upper() not in self.users:
				print("없는 아이디 입니다.")
			else:
				if self.users[id.upper()].pwd != pwd:
					print("비밀번호가 틀립니다")
				else:
					print("로그인에 성공하였습니다.")
					self.user = self.users[id.upper()]
					break
			menu = ["나가기", "다시하기"]
			self.print_menu(menu)
			while True:
				opt = self.select_option()
				if opt == -1:
					continue
				elif opt < 0 and opt >= len(menu):
					self.out_of_range_error()
					continue
				else:
					break
			if opt == 0:
				break
		
	def sign_out(self):
		self.user = None
		print("로그아웃 되었습니다.")

	def print_menu(self, opt):
		print("")
		print("="*150)
		for i in range(1, len(opt)):
			if i % 5 == 1:
				print("")
			menu_str = str(i) + ". " + opt[i]
			print("{:^15}".format(menu_str), end='')
		menu_str = "0. " + opt[0]
		print("{:^15}".format(menu_str))
		print("")
		print("="*150)
		print("")
		pass

	def load_data(self):
		with open("data/user_data.txt", 'r') as f:
			line = f.readline()
			while line:
				line = line.split('\\')
				id = line[0]
				new_user = User.User(line[0], line[1], line[2])
				self.load_dictionary_data(line[3], new_user.movie)
				self.load_dictionary_data(line[4], new_user.genre)
				self.load_dictionary_data(line[5], new_user.director)
				self.users[id.upper()] = new_user
				line = f.readline()

	def load_dictionary_data(self, line, dict):
		if not line.startswith("N/A"):
			line = line.split(',')
			for i in range(len(line) - 1):
				key_value = line[i].split(':')
				key = key_value[0]
				value = float(key_value[1])
				dict[key] = value

	def save_data(self):
		with open("data/user_data.txt", 'w') as f:
			for id in self.users:
				if isinstance(self.users[id], User.User):
					f.write("{}\\{}\\{}\\".format(self.users[id].id, self.users[id].pwd, self.users[id].name))
					self.save_dictionary_data(f, self.users[id].movie)
					self.save_dictionary_data(f, self.users[id].genre)
					self.save_dictionary_data(f, self.users[id].director)
					f.write("\n")

	def save_dictionary_data(self, file, dict):
		if len(dict) == 0:
			file.write("N/A\\")
		else:
			for key, value in dict.items():
				file.write("{}:{}".format(key, value),end=',')
			file.write("\\")
	
	def select_option(self):
		try:
			opt = int(input("메뉴를 선택해주세요: "))
			return opt
		except:
			print("error: 숫자가 아닙니다.")
			print("다시 선택해주세요.")
			return -1

	def out_of_range_error(self):
		print("error: 범위를 벗어났습니다.")
		print("다시 선택해주세요.")
		print("")

	def load_movie_data(self):
		df = pd.read_excel("data/movie_data.xlsx", engine = "openpyxl", sheet_name = 'movie_data')
		return df 

	def show_movie_table(self, current_page, end_page):
		start_idx = (current_page - 1) * 10
		if current_page == end_page:
			end_idx = len(self.movie_data)
		else:
			end_idx = current_page * 10
		print("="*150)
		print("{:^30}{:^20}{:^10}{:^10}{:^20}{:^10}{:^20}".format("영화명", "개봉일", "관객수", "제작국가", "장르", "제작상태", "감독"))
		print("="*150)
		for i in range(start_idx, end_idx):
			print("{:^30}{:^23}{:^13}{:^12}{:^19}{:^13}{:^20}".format(self.movie_data.영화명[i], str(self.movie_data.개봉일[i].date()), str(self.movie_data.관객수[i]), self.movie_data.제작국가[i], self.movie_data.장르[i], self.movie_data.제작상태[i], self.movie_data.감독[i]))
		print("="*150)
		page_number = str(current_page) + ' / ' + str(end_page)
		print("{:^150}".format(page_number))
		print("")

	def show_all_users_info_page(self):
		current_page = 1
		end_page = (len(self.users)//10) + 1
		while True:
			self.show_all_users_info_table(current_page, end_page)
			if current_page == 1:
				if end_page == 1:
					menu = ["나가기"]
					self.print_menu(menu)
				else:
					menu = ["나가기", "다음"]
					self.print_menu(menu)
				
			elif current_page == end_page:
				menu = ["나가기", "이전"]
				self.print_menu(menu)
			else:
				menu = ["나가기", "이전", "다음"]
				self.print_menu(menu)

			opt = self.user.select_option()
			if opt == -1:
				continue
			elif opt < 0 or opt >= len(menu):
				self.out_of_range_error()
				continue

			if menu[opt] == "나가기":
				break
			elif menu[opt] == "다음":
				current_page += 1
			elif menu[opt] == "이전":
				current_page -= 1
			else:
				self.out_of_range_error()
				continue

	def show_change_pwd_page(self):
		self.user.change_pwd()

	def show_all_users_info_table(self, current_page, end_page):
		start_idx = (current_page - 1) * 10
		if current_page == end_page:
			end_idx = len(self.users)
		else:
			end_idx = current_page * 10
		info = list(self.users.values())
		print(start_idx)
		print(end_idx)
		print("="*150)
		print("{:^20}{:^20}".format("ID", "이름"))
		print("="*150)
		for i in range(start_idx, end_idx):
			print("{:^20}{:^20}".format(info[i].id, info[i].name))
		print("="*150)
		page_number = str(current_page) + ' / ' + str(end_page)
		print("{:^150}".format(page_number))
		print("")

	'''
	def show_movie_introduction(self, current_page, end_page, opt):
		index = (current_page - 1) * 10 + (opt - 1)
		movie_name = "영화 " + self.movie_data.영화명[index] + " 정보"
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		options.add_argument('window-size=1920x1080')
		options.add_argument("disable-gpu")
		wd = webdriver.Chrome(chrome_options=options)
		wd.get("http://www.naver.com")
		elem = wd.find_element_by_name('query')
		elem.send_keys(movie_name)
		elem.send_keys(Keys.RETURN)
		soup = BeautifulSoup(wd.page_source, 'html.parser')
		print("="*150)
		print("{:^150}".format("소개"))
		print("")
		print(soup.select("p.text._content_text")[0].text)
		print("")
		print("="*150)
		time.sleep(1)
	'''
