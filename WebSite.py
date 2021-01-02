import User
import Administrator

class WebSite:
	opt_list = ['나가기', '회원가입', '로그인', '로그아웃']
	def __init__(self):
		self.users = dict()
		self.user = None
		self.movie_data = None
		self.load_data()

	def show_movie_recommendation_by_관객수(self):
		pass

	def show_movie_recommendation_by_genre(self):
		pass

	def show_movie_recommendation_by_directors(self):
		pass

	def sign_up(self):
		while True:
			id = input("아이디를 입력해주세요: ")
			if id in self.users:
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
			self.users[id] = new_user
			print("")
			print("축하합니다 ", id, "님")
			print("회원가입 완료되었습니다.")
			break
		pass

	def sign_in(self):
		pass

	def sign_out(self):
		pass

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
		return isinstance(user, Administrator.Administrator)

	def load_data(self):
		pass