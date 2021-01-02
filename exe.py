import WebSite
import sys
import os

args = sys.argv[1:]
if args[0] == '-h':	# help 목록 출력
	print("usage: exe.py [option] ... [-c cmd | -m mod | file | -] [arg] ...")
	print("Options and arguments (and corresponding environment variables):")
	print("-h	: showing help list")
	print("-r	: read and print readme.txt")
	sys.exit()
elif args[0] == '-r':	# readme.txt 파일 내용을 읽어와서 출력
	print("readme.txt : \n")
	f = open("readme.txt", 'r', encoding='utf8')
	while True:
		line = f.readline()
		if not line: break
		print(line)
	f.close()
	sys.exit()

if __name__ == "__main__":
	#argv = sys.argv
	#args_length = len(argv)
	movie_website = WebSite.WebSite()
	movie_website.execute()