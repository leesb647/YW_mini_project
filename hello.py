def error():
	print("\nError:")
	print("다시 입력해 주세요.")

def execute():
	data = {}
	favor_genre = []
	while True:
		print("")
		print("="*60)
		print("{:^10}{:^10}{:^10}{:^10}{:^10}".format("1. 장르", "2. 기간", "3. 감독", "4. 영화추천", "0. 종료"))
		print("="*60)
		print("")

		try:
			opt = int(input("원하는 메뉴를 선택해 주세요: "))
		except:
			error()
			continue

		if opt == 0:
			break
		elif opt == 1:
			# 장르 메뉴를 보여주기 위한 리스트 만들기 
			genres = []
			for name in data:
				genre = data[name][0]
				if genre not in genres:
					genres.append(genre)
			
			# 장르별 메뉴 보여주기
			print("")
			print("="*60)
			for i in range(1, len(genres) + 1):
				if i % 5 == 0: 
					print("")
				string = (i+1) + ". " + genres         #ex) 1. 로맨스
				print("{:^10}".format(string), end = '')
			print("{:^10}".format("0. 나가기"))
			print("="*60)
			print("")

			try:
				idx = int(input("장르를 선택해 주세요: "))
			except:
				error()
				continue

			if idx >= 0 and idx <= len(genres):
				if genres[idx - 1] not in favor_genre:
					favor_genre.append(genres[idx - 1])
				else:
					favor_genre.remove(genres[idx - 1])
			else:
				error()
				continue

			# 장르 함수
			pass
		elif opt == 2:
			# 기간 함수
			pass
		elif opt == 3:
			# 감독 함수
			pass
		elif opt == 4:
			# 배우 함수
			pass
		else:
			error()
			continue



if __name__ == "__main__":
	execute()





