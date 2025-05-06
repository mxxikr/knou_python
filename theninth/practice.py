# ============ 원뿔 계산 함수 정의 (반환 값이 없는 함수) ============ 
def prt_cone_vol(r, h):
    if r > 0 and h > 0:
        # r, h 모두 양수일 때
        vol= 1 / 3 * 3.14 * r ** 2 * h
        print("원뿔의 부피는", vol, "입니다.")
    else:
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

# ============ 원뿔 계산 함수 정의 (함수 호출 및 실행) ============ 
def prt_cone_vol(r, h):
    if r > 0 and h > 0:
        #r,h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        print("원뿔의 부피는", vol, "입니다.")
    else :
        #r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

#반지름 30, 높이 50
rad = 30 
hei = 50 
prt_cone_vol(rad, hei)

# =========== 숫자를 입력 받고 역순으로 출력하는 함수를 사용한 프로그램을 작성하시오. ============
digits = 1234

def reverse_number(num):
    while num != 0:
            digit = num % 10
            num = num // 10
            print(digit, end="") # 개행 문자 대신 한 줄에 이어서 출력
				
reverse_number(digits)

# ============ 원뿔 계산 함수 정의 (반환 값이 있는 함수) ============ 
# 원뿔 계산 함수 정의
def prt_cone_vol(r, h):
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        return vol
    else:
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

# ============ 원뿔 계산 함수 정의 (format 함수 활용) ============ 
def rtn_cone_vol(r, h): # 원뿔의 부피를 출력해주는 함수 정의
    if r > 0 and h > 0 :
	      # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        return vol
    else:
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

# 원뿔 부피 계산 함수 호출
rtn_cone_vol(10, 20)
print(rtn_cone_vol(10, 20), "입니다")
print(format(rtn_cone_vol(10, 20), ">20.3f"), "입니다")
print(format(rtn_cone_vol(10, 20), "<20.3f"), "입니다")

# 원뿔 계산 함수 정의
def prt_cone_vol(r, h) :
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * h
        return vol
    else :
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")
        
#반지름 10, 높이 50
rad = 10
hei = 50
format(prt_cone_vol(rad, hei) , ">10.3f")
print(format(prt_cone_vol(rad, hei) , ">10.3f"))
print(rad, hei)

# ============ 동시 할당 ============
temp = 27
season = "summer"

temp, season = 27, "summer"

# ============ 교환 ============
temp = hei
hei = rad
rad = temp

rad, hei = hei, rad

# ============ 세 개의 사용자 입력을 오름차순으로 정렬하는 함수를 이용하여 정렬된 값을 출력하는 프로그램을 작성하시오. ============
a = int(input("첫번째 숫자를 입력하세요: "))
b = int(input("두번째 숫자를 입력하세요: "))
c = int(input("세번째 숫자를 입력하세요: "))

def sort3(a, b, c):
		if a > b:
				a, b = b, a
		if a > c:
				a, c = c, a
		if b > c:
				b, c = c, b
				
		print(a, b, c)

sort3(a, b, c)
print("출력 이후" , a, b, c) # 함수 내부에는 값만 전달되므로, 변수에는 영향이 가지 않음

# =========== 값의 전달 ============
x = 1
print("x의 값은", x)
# inc(x) # inc 함수 정의 전이기 때문에 오류 발생

def inc(x):
    x = x + 1 
    print("x의 값은", x)

inc(x)
print("x의 값은", x)

# ============ 원뿔 계산 함수 정의(부피와 겉넓이를 모두 반환) ============
def rtn_cone_vol_surf(r, h): # 원뿔의 부피를 출력해주는 함수 정의
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * hei
        surf = 3.14 * r ** 2 + 3.14 * r * h
        return vol, surf # vol과 surf 동시 리턴
    else:
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

print(rtn_cone_vol_surf(50, 100))
vol1, surf1 = rtn_cone_vol_surf(50, 100)
print(vol1, "입니다.")
print(surf1, "입니다.")

# ============ 변수의 스코프 ============ 
x = 1
print("x의 값은", x)

def inc(x):
		x = x + 1
		print("x의 값은", x)
		
inc(x)
print("x의 값은", x)

def rtn_cone_vol(r, h): # 원뿔의 부피를 출력해주는 함수 정의
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * hei
        r, h = 0, 0 # 0으로 초기화
        return vol
    else:
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

radius = 50
height = 100
print(format(rtn_cone_vol(radius, height), ">10.3f"))
print("함수 사용 후 ", radius, height)

# ============ 기본 매개 변수 ============ 
print("Hello", "I am Python")
print("Hello", "I am Python", sep = " ")

def rtn_cone_vol_surf(r = 20, h =30): # 함수 정의 부분에 기본 값 지정
    if r > 0 and h > 0 :
        # r, h 모두 양수일 때
        vol = 1/3 * 3.14 * r ** 2 * hei
        surf = 3.14 * r ** 2 + 3.14 * r * h
        return vol, surf # vol과 surf 동시 리턴
    else:
        # r, h가 음수일 때
        print("반지름과 높이 값에 양수를 입력하세요")

print(rtn_cone_vol_surf(100, 200))
print(rtn_cone_vol_surf())

# ============ 가변 매개 변수 ============ 
x = 10
y = 20
z = 30

print("x는", x, "y는", y, "z는", z)

def var_sum_avg(*numbers):
    sum = 0
    count = 0 # 파라미터의 개수를 알아내기 위한 변수
    for i in numbers: # 시퀀스 내에 있는 값들을 하나씩 가져오기 위해 for문 사용
            sum = sum + i 
            count = count + 1 # 평균을 구하기 위해 파라미터의 개수 구함
            
    return sum, sum/count

print(var_sum_avg(10, 20, 30 , 40))
print(var_sum_avg(20, 25, 10, 85, 100 , 150)) # 입력 값의 개수가 달라져도 정상 동작함