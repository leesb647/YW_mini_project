import WebSite
import sys

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 1:
		movie_website = WebSite.WebSite()
		movie_website.execute()
	elif args[1] == '-h':	# help 목록 출력
		print("usage: exe.py [option] ... [-c cmd | -m mod | file | -] [arg] ...")
		print("Options and arguments (and corresponding environment variables):")
		print("-h	: showing help list")
		print("-r	: read and print readme.txt")
		sys.exit()
	elif args[1] == '-r':	# readme.txt 파일 내용을 읽어와서 출력
		print("readme.txt : \n")
		f = open("readme.txt", 'r', encoding='utf8')
		while True:
			line = f.readline()
			if not line: break
			print(line)
		f.close()
		sys.exit()
