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
	movie_website.execute()