class Administrator:
	opt_list = ['나가기', '데이터 관리', '공지 보내기', '유저 상황', '로그아웃']
	def __init__(self, id, pwd, name):
		self.id = id
		self.pwd = pwd
		self.name = name

	def manage_data(self):
		pass

	def send_message(self):
		pass

	def show_all_users(self):
		pass
