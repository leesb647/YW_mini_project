def error():
	print("\nError:")
	print("다시 입력해 주세요.")

def get_entire_genres(data):
	total = []
	for name in data:
		for movie_genres in data[name][0]:
			if movie_genres not in total:
				total.append(movie_genres)
	return total

def execute():
	data = {"명량": [["사극","액션"]]}
	preference = {'장르': [], '시작점': 0, '종료점': 0, '감독': []}
	entire_genres = get_entire_genres(data)					# 전체 장르 변수.

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
			# 장르별 메뉴 보여주기
			print("")
			print("="*60)
			for i in range(len(entire_genres)):
				if i % 5 == 0: 
					print("")
				string = str((i+1)) + ". " + entire_genres[i]         #ex) 1. 로맨스
				print("{:^10}".format(string), end = '')
			print("{:^10}\n".format("0. 나가기"))

			print("="*60)
			print("")
			print("현재 선택된 장르:")
			for genre in preference['장르']:
				print(genre, end=' ')
			print("\n")

			try:
				idx = int(input("장르를 선택해 주세요: "))
			except:
				error()
				continue

			if idx >= 0 and idx <= len(entire_genres):
				if entire_genres[idx - 1] not in preference['장르']:
					preference['장르'].append(entire_genres[idx - 1])
				else:
					preference['장르'].remove(entire_genres[idx - 1])
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

		# 현재 선택된 옵션 출력
		print("")
		print("="*20 + "{:^20}".format("현재 선택된 옵션") + "="*20)
		for key in preference:
			print(key, " : ", end='')
			if type(preference[key]) != type(list()):
				print("{:^5}".format(preference[key]), end='')
			else:
				for value in preference[key]:
					print("{:^5}".format(value),end='')
			print("")



if __name__ == "__main__":
	execute()





