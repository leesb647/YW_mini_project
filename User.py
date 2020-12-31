from collections import defaultdict

class User:
	opt_list = []
	def __init__(self, id, pwd, name):
		self.id = id
		self.pwd = pwd
		self.name = name
		self.genres = defaultdict(float)
		self.directors = defaultdict(str)
		self.messages = []

	def evaluate_movie(self):
		pass

	def change_pwd(self):
		pass
