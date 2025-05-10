# ============ 파일 읽기 ============
h_fp = open("Hamlet_by_Shakespeare_read.txt", "r", encoding="utf-8") # 경로가 없는 걸로 보아 같은 폴더 내에 있다는 뜻, 읽기 모드 사용
title = h_fp.read(6) # 입력 받은 바이트 수 만큼 파일 포인터를 읽으면서 데이터를 반환 함
author = h_fp.readline() # 다음에 있는 개행 포인터가 보일 때까지 쭉 읽어들이는 함수
h_fp.close()

# ============ 파일 쓰기 ============
p_fp = open("python.txt", "w", encoding="utf-8")
p_fp.write("KNOU\n")
p_fp.write("python programming\n")
p_fp.close( )

# ============ 데이터 추가 ============
a_fp = open("python.txt", "a", encoding="utf-8")
a_fp.write("\nby CS\n")
a_fp.close()

# ============ 파일 읽고 쓰고 수정하는 프로그램 ============
# 'Khan.txt' 파일을 읽고 처리하는 프로그램을 작성하시오.
# 모든 내용을 출력하시오.
# 마지막에 '-칭기스 칸-'을 삽입하시오.

# 파일 생성
khan_fp = open("Khan.txt", "r", encoding="utf-8")
print(khan_fp.read(10)) # 10글자를 읽고 출력
print(khan_fp.readline()) # 개행 문자가 있는 곳까지 읽고 출력

khan_fp.close()

# 텍스트 한줄 씩 읽고 출력하기
khan_fp = open("Khan.txt", "r", encoding="utf-8")

# \n으로 한줄 띄우고 print로 한줄 띄워지면서 새로운 줄이 생김
for motto in khan_fp.readlines(): # 텍스트 파일에 있는 모든 라인을 읽음(한줄 씩을 리스트로 읽어내는 명령)
	print(motto)

# 문자열에 있는 개행 문자 삭제
for motto in khan_fp.readlines(): # 텍스트 파일에 있는 모든 라인을 읽음(한줄 씩을 리스트로 읽어내는 명령)
	print(motto.strip()) # 특정 문자를 제거

khan_fp.close()

# 텍스트 파일 맨 뒤에 새로운 텍스트 삽입
khan_fp = open("Khan.txt", "a", encoding="utf-8")

khan_fp.write("\n")
khan_fp.write(format("-칭기스 칸-", ">50s")) # 파일 포인터가 이미 맨 뒤에 위치해 있으므로, write 함수를 사용
# 문자열을 50폭, 오른쪽으로 정렬해서 추가
khan_fp.close()

# ============ "Hamlet_by_Shakespeare.txt" 파일에 포함된 단어가 출현한 횟수를 출력하는 프로그램을 작성하시오. ============
# 텍스트 파일을 열어 데이터 분석(딕셔너리 사용)

h_fp = open("Hamlet_by_Shakespeare.txt", "r", encoding="utf-8")
word_dict = dict() # 빈 딕셔너리 생성

# 각각의 라인을 읽어 내어 word 별로 저장
for line in h_fp.readlines(): # 텍스트를 줄 단위로 읽어냄
	# 한 줄에 있는 여러 단어들을 하나 하나씩 끊어 주어야 함
	for word in line.strip().split(): # 불 필요한 개행 문자 제거(strip) -> 결과물을 하나씩 분할(split)
		word = word.strip(" .,;?[]\"\':=!").lower() # 제거할 문자들을 전부 입력 후 소문자로 변환
		
		if word_dict.get(word) is not None: # 정돈 된 word를 word_dict의 key로 가져온 것이 있다면
			count = word_dict[word] # 기존 단어의 출현 횟수(value)를 count로 가져오는 작업
		else:
			count = 0
		
		word_dict[word] = count + 1

# 딕셔너리 순회
for key in word_dict:
	print("[" + key + "]", str(word_dict[key]) + "회") # key 값(단어들)과 카운트한 횟수(word_dict[key]) 출력하는 작업
	
h_fp.close() # 파일 사용하고 난 후에는 꼭 close() 처리해 줄 것

# ============ 'Hamlet_by_Shakespeare.txt' 파일에 출현 횟수가 100 이상되는 단어와 출력 횟수를 정렬하여 출력하는 프로그램을 작성하시오. ============
# 딕셔너리 정렬한 후 출력하기
h_fp = open("Hamlet_by_Shakespeare.txt", "r")
word_dict = dict() # 빈 딕셔너리 생성

# 각각의 라인을 읽어 내어 word 별로 저장
for line in h_fp.readlines(): # 텍스트를 줄 단위로 읽어냄
	# 한 줄에 있는 여러 단어들을 하나 하나씩 끊어 주어야 함
	for word in line.strip().split(): # 불 필요한 개행 문자 제거(strip) -> 결과물을 하나씩 분할(split)
		word = word.strip(" .,;?[]\"\':=!").lower() # 제거할 문자들을 전부 입력 후 소문자로 변환
		
		if word_dict.get(word) is not None: # 정돈 된 word를 word_dict의 key로 가져온 것이 있다면
			count = word_dict[word] # 기존 단어의 출현 횟수(value)를 count로 가져오는 작업
		else:
			count = 0
		
		word_dict[word] = count + 1

# key와 value를 바꾸어 줄 새로운 딕셔너리 생성
word_r_dict = {v:k for (k, v) in word_dict.items()} # word_dict에서 리스트로 가져온 것들의 key와 value를 뒤바꾸어 새로운 word_r_dict에 넣기

word_dict = {k:v for (v, k) in sorted(word_r_dict.items(), reverse=True)} # word_r_dict에서 가져온 것들을 정렬 후 다시 딕셔너리로 구성

for key in word_dict:
	if word_dict[key] >= 100: # 100회 이상 등장하는 단어만 출력
		print("[" + key + "]", str(word_dict[key]) + "회") # key 값(단어들)과 카운트한 횟수(word_dict[key]) 출력하는 작업
	
h_fp.close() # 파일 사용하고 난 후에는 꼭 close() 처리해 줄 것