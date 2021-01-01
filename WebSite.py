import User
import Administrator

class WebSite:
	opt_list = ['나가기', '회원가입', '로그인']
	
	def __init__(self):
		admin = Administrator.Administrator('YW', '1234', '영우')
		self.users = {admin.id: admin}
		self.user = None
		self.movie_data = None
		self.load_data()
		print(len(self.users))

	def show_movie_recommendation_by_관객수(self):
		pass

	def show_movie_recommendation_by_genre(self):
		pass

	def show_movie_recommendation_by_directors(self):
		pass

	def sign_up(self):
		while True:
			id = input("아이디를 입력해주세요: ")
			if id.upper() in self.users:
				print("동일한 아이디가 있습니다.")
				continue
			pwd = input("비밀번호를 입력해주세요: ")
			name = input("이름을 선택해주세요: ")
			self.print_menu(["나가기", "완료", "다시하기"])
			opt = int(input("선택해주세요: "))
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
					print("로그인에 성긍하였습니다.")
					self.user = self.users[id.upper()]

					break
			self.print_menu(["나가기", "다시하기"])
			opt = int(input("선택해주세요: "))
			if opt == 0:
				break
		
	def sign_out(self):
		self.user = None
		print("로그아웃 되었습니다.")

	def print_menu(self, opt):
		print("")
		print("="*80)
		for i in range(1, len(opt)):
			if i % 5 == 1:
				print("")
			menu_str = str(i) + ". " + opt[i]
			print("{:^15}".format(menu_str), end='')
		print("{:^15}".format("0. 나가기"))
		print("")
		print("="*80)
		print("")
		pass

	def isUserAdministrator(self):
		return isinstance(self.user, Administrator.Administrator)

	def load_data(self):
		with open("data/user_data.txt", 'r') as f:
			line = f.readline()
			while line:
				line = line.split(',')
				id = line[0]
				new_user = User.User(line[0], line[1], line[2])
				line = f.readline()									# 영화 딕셔너리 데이터
				self.load_dictionary_data(line, new_user.movie)
				line = f.readline()									# 장르 딕셔너리 데이터
				self.load_dictionary_data(line, new_user.genre)
				line = f.readline()									# 감독 딕셔너리 데이터
				self.load_dictionary_data(line, new_user.director)
				line = f.readline()									# 다음 정보
				self.users[id.upper()] = new_user

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
					f.write("{},{},{}".format(self.users[id].id, self.users[id].pwd, self.users[id].name))
					f.write("\n")
					self.write_dictionary_data(f, self.users[id].movie)
					self.write_dictionary_data(f, self.users[id].genre)
					self.write_dictionary_data(f, self.users[id].director)

	def write_dictionary_data(self, file, dict):
		if len(dict) == 0:
			file.write("N/A\n")
		else:
			for key, value in dict.items():
				file.write("{}:{}".format(key, value),end=',')
			file.write("\n")


		
