import WebSite
import sys
import os

args = sys.argv[1:]
if args[0] == '-h':
	print("help list")
elif args[0] == '-r':
	f = open("readme.txt", 'r', 'utf-8')
	while True:
		line = f.readline()
		if not line: break
		print(line)
	f.close()

if __name__ == "__main__":
	#argv = sys.argv
	#args_length = len(argv)
	movie_website = WebSite.WebSite()
	while True:
		if movie_website.user is None:
			movie_website.print_menu(WebSite.WebSite.opt_list)
			opt = int(input("메뉴를 선택하세요: "))
			if opt == 1:
				movie_website.sign_up()
			elif opt == 2:
				movie_website.sign_in()
			elif opt == 3:
				movie_website.sign_out()
			elif opt == 0:
				movie_website.save_data()
				break
			else:
				continue
		elif movie_website.isUserAdministrator():
			print("Admin page")
			break
			pass
		else:
			print("User page")
			break
			pass
