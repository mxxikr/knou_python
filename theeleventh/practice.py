#  ============ 모듈 등록 확인 ============ 
import math
from math import sin

dir() # 어떤 모듈들이 등록(import) 되어 있는지 확인할 수 있는 dir 함수
dir(math) # math 모듈에 어떤 멤버들이 있는지 확인
help(math.gamma) # 등록 된 함수의 사용 방법을 알고자 할 때 사용
help("python".upper)

#  ============ 원뿔 계산 프로그램 개선 ============
# 원뿔 클래스 정의
class Cone :
    def __init__(self, radius = 20, height = 30):
        self.r = radius
        self.h = height

    def get_vol(self) :
        return 1/3 * 3.14 * self.r ** 2 * self.h

    def get_surf(self) :
        return 3.14 * self.r ** 2 + 3.14 * self.r * self.h


print(math.pi)
# 원뿔 클래스 정의
class Cone :
    def __init__(self, radius = 20, height = 30):
        self.r = radius
        self.h = height

    def get_vol(self) :
        return 1/3 * math.pi * self.r ** 2 * self.h # 3.14 보다 정확한 파이 값 사용

    def get_surf(self) :
        return math.pi * self.r ** 2 + math.pi * self.r * self.h

#  ============ 삼각형 넓이 계산 프로그램 ============
# 두 변의 길이 a, b와 끼인 각 α인 삼각형의 넓이를 구하는 프로그램을 작성하시오.
a, b = 10, 20

# area = 1 / 2 * a * b * math.sin(60) # 결과 값이 음수가 나옴 파이 값으로 매개 변수 추가해야 함

# 60도를 호도법으로 바꾸어야 함
area = 1 / 2 * a * b * math.sin(math.radians(60)) # 60도를 호도법으로 바꾼 값의 sin 값 산출

print(area) 

#  ============ 삼각형 넓이 계산 프로그램(특정 함수 부분 호출) ============
a, b = 10, 20

# area = 1 / 2 * a * b * math.sin(60) # 결과 값이 음수가 나옴 파이 값으로 매개 변수 추가해야 함

# 60도를 호도법으로 바꾸어야 함
area = 1 / 2 * a * b * sin(math.radians(60)) # 60도를 호도법으로 바꾼 값의 sin 값 산출

print(area) 

# ============ 가위-바위-보 게임 ============
import random # random 모듈 import

options = ["가위", "바위", "보"]
user = input("가위,바위,보를 입력: ")
com = random.choice(options) # option 리스트를 랜덤하게 반환

if user == com:
    print("비겼다!")
elif user == "바위" and com == "가위":
		print("이겼다!")
elif user == "보" and com == "바위":
		print("이겼다!")
elif user == "가위" and com == "보":
		print("이겼다!")
else:
		print("졌다!")

# ============ 로또 추첨 프로그램 ============
# 1 ~ 45 숫자 6개를 입력 받아 당첨 숫자와 비교하는 프로그램을 작성하시오.

import random # random 모듈 import

# 사용자의 입력 값 그대로 사용할 수 없음 -> input을 통해 들어온 긴 문자열을 콤마 기준으로 분리
guess_str = input("1 ~ 45 번호 6개를 쉼표로 분리하여 입력하세요 : ").split(", ")
guess_list = list()

# 숫자로 된 문자열을 하나씩 읽어 int형으로 받은 뒤 guess_list 에 저장
for i in guess_str:
	guess_list.append(int(i)) # guess_str의 값들을 하나하나 정수로 변환하여 guess_list에 하나씩 추가
	
lotto_list = random.sample(range(1, 46, 1), 6) # 1부터 45까지의 값 중 6개의 값을 랜덤으로 추출

print("예상 번호는", guess_list, "입니다.")
print("추첨 번호는", lotto_list, "입니다.")

hit_count = 0

for guess in guess_list:
		if guess in lotto_list: # 비교 연산자 in
			hit_count = hit_count + 1

print("축하합니다 " + str(hit_count) + "개 맞혔습니다.")

# ============ 스무 고개 프로그램 ============
# 20번의 기회 안에 1 ~ 1000 사이의 숫자를 맞히는 스무 고개 프로그램을 작성하시오.
import random

hit_number = random.randint(1, 1001) # 정수를 무작위로 추출

guess_count_list = range(1, 21, 1) # 1 ~ 20 까지 들어있는 리스트 생성하여 현재 몇 번째 시도인지를 출력

passfail = False # 실패했다고 가정

for guess_count in guess_count_list: # 20번 반복하는 for문
	guess = int(input("숫자를 맞혀 보세요(" + str(guess_count)+"번째 시도): "))
	# 반복할 때마다 몇번 째 시도인지 알려줘야 함
	if hit_number == guess:
		passfail = True # 숫자를 20회 내에 맞힌 경우에는 반복할 필요 없음
		break # 반복 중단할 때 사용
	elif hit_number > guess:
		print(str(guess) + "보다 큽니다.", end = "")
	else:
		print(str(guess) + "보다 작습니다.", end = "")

if passfail == True:
	print("맞혔습니다. 축하합니다.")
else:
	print("모든 기회를 다 사용하셨습니다. 다음에 다시 도전하세요")

# ============ 소수 찾기 프로그램 ============
# 1 ~ 5000 사이에 소수(prime number)를 찾고 실행 시간을 출력하는 프로그램을 작성하시오.
import time

start_time = time.time() # 1970.1.1 이후로 경과 된 시점을 초 단위로 환산

# 소수인지 판별하는 함수(소수는 자신과 1을 제외한 다른 수로 나누어떨어지지 않는 1보다 큰 정수)
def is_prime(x):
    for i in range(2, x): # 2부터 x-1까지 반복
        if x % i == 0:
            return False # i로 나누었을 때 나누어 떨어지면(나머지가 0이면) 소수가 아니므로 False 반환
    return True

prime_count = 0

for i in range(1, 5001): # 1부터 5000까지 확인
    if is_prime(i):
        prime_count = prime_count + 1
        print(i, end = ", ")

end_time = time.time()
print("\n", end_time - start_time, "초 실행했습니다.")