import WebSite
import sys

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 1:
		movie_website = WebSite.WebSite()
		movie_website.execute()
	elif args[1] == '-h':	# help 목록 출력
		print("usage: exe.py [option]")
		print("Options:")
		print("-h	: showing help list")
		print("-r	: read and print readme.txt")
		sys.exit()
	elif args[1] == '-r':	# readme.txt 파일 내용을 읽어와서 출력
		print("")
		f = open("readme.txt", 'r', encoding='utf8')
		line = f.read()
		print(line)
		f.close()
		sys.exit()
