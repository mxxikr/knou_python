# ============ 불리언 타입 ============
3 > 6 # False
light_on = 3 > 6 # False

suf = 1
vol = 2
suf == vol # False

isStop = suf == vol # False

# ============원뿔 계산 프로그램(음수 처리 없음) ============
# 반지름 사용자 입력
rad = int(input("반지름을 입력하세요: "))

# 높이 사용자 입력
hei = int(input("높이를 입력하세요: "))

# 부피 & 겉넓이 계산
vol = 1/3 * 3.14 * rad ** 2 * hei
suf = 3.14 * rad ** 2 + 3.14 * rad * hei
print("원뿔의 부피는", vol, "입니다.")
print("원뿔의 겉넓이는", suf, "입니다.")

# ============ 논리 연산자 and ============
temp = 20
fruit = "apple"
temp >= 27 and fruit == "apple" # False

rad = 10
hei = 20
rad > 0 and hei > 0 # True

# ============ 논리 연산자 or ============
temp >= 27 or fruit == "apple" # True

rad > 0 or hei > 0 # True

# ============ 논리 연산자 not ============
not temp >= 21 # True

# ============ 단락 평가 ============
temp = 25
season = "summer"
temp >= 27 and season == "summer" # False
temp >= 27 or season == "summer" # True

# ============ 원뿔 계산 프로그램 개선 (음수 처리) ============
# 반지름 사용자 입력
rad = int(input("반지름을 입력하세요: "))

# 높이 사용자 입력
hei = int(input("높이를 입력하세요: "))

if (rad > 0):
		# 부피 & 겉넓이 계산
		vol = 1/3 * 3.14 * rad ** 2 * hei
		suf = 3.14 * rad ** 2 + 3.14 * rad * hei
		print("원뿔의 부피는", vol, "입니다.")
		print("원뿔의 겉넓이는", suf, "입니다.")

# ============ 원뿔 계산 프로그램 개선 (음수 처리 확장) ============
# 사용자가 반지름과 높이 값에 양수를 입력할 경우 부피 겉넓이 출력
# 반지름 사용자 입력
rad = int(input("반지름을 입력하세요: "))

# 높이 사용자 입력
hei = int(input("높이를 입력하세요: "))

if (rad > 0 and hei > 0):
		# 부피 & 겉넓이 계산
		vol = 1/3 * 3.14 * rad ** 2 * hei
		suf = 3.14 * rad ** 2 + 3.14 * rad * hei
		print("원뿔의 부피는", vol, "입니다.")
		print("원뿔의 겉넓이는", suf, "입니다.")

# ============ 원뿔 계산 프로그램 개선 (이분 선택 구조) ============
# 반지름 사용자 입력
rad = int(input("반지름을 입력하세요: "))

# 높이 사용자 입력
hei = int(input("높이를 입력하세요: "))

if (rad > 0 and hei > 0):
		# 부피 & 겉넓이 계산
		vol = 1/3 * 3.14 * rad ** 2 * hei
		suf = 3.14 * rad ** 2 + 3.14 * rad * hei
		print("원뿔의 부피는", vol, "입니다.")
		print("원뿔의 겉넓이는", suf, "입니다.")
else:
		print("반지름과 높이에 양수를 입력해주세요")
		
# ============ 가장 큰 수 찾는 프로그램 (내장 함수 사용) ============
# A, B, C 사용자 입력
A = int(input("A 입력: "))
B = int(input("B 입력: "))
C = int(input("C 입력: "))

# A, B, C 중 가장 큰 수 출력
max(A, B, C)

# ============ 가장 큰 수 찾는 프로그램 (if문 사용) ============
# A, B, C 사용자 입력
A = int(input("A 입력: "))
B = int(input("B 입력: "))
C = int(input("C 입력: "))

# A, B, C 중 가장 큰 수 출력
if A > B: # 바깥쪽 if문 진입 -> True
		if A > C: # 안쪽 if문 블록 진입 -> 조건 판별
				print(A)
		else:
				print(C)
else: # # 바깥쪽 if문 진입 -> Flase
		if B > C: # 여기서 판별
				print(B)
		else:
				print(C)

# ============ 연습 문제 2 ============
temp = int(input("온도를 입력하세요: "))
if temp <= 0:
        print("겨울입니다.")

# ============ 연습 문제 3 ============
guess = int(input("숫자를 입력하세요: "))

if guess % 3 == 0 and guess % 5 == 0:
        print("3과 5의 공배수입니다.")
else:
        print("3과 5의 공배수가 아닙니다.")