# ============ 원 뿔 계산 클래스 (객체 지향 개념 적용) ============
# 원뿔 클래스 정의(지역 변수)
class Cone:
    def __init__(self, radius=20, height=30): # 초기자 지정
		# 변수 r과 h의 스코프는 __init__ 메소드 내부
		# 지역 변수
        r = radius 
        h = height

    def get_vol(self):
        # 원뿔 부피 계산: 1/3 * pi * r^2 * h
        return 1/3 * 3.14 * self.r ** 2 * self.h

    def get_surf(self):
        # 원뿔 겉넓이 계산: pi * r^2 + pi * r * h
        return 3.14 * self.r ** 2 + 3.14 * self.r * self.h # 데이터 필드의 r과 h라는 것을 알려주기 위해 꼭 self.를 앞에 표시해주어야 함
    
# 원뿔 클래스 정의(전역 변수)
class Cone:
    def __init__(self, radius=20, height=30): # 초기자 지정
        # self.r, self.h의 스코프는 클래스 전역
        # self.r, self.h는 인스턴스 변수 (클래스 내 다른 메소드에서도 접근 가능)
        self.r = radius
        self.h = height

    def get_vol(self):
        # 원뿔 부피 계산: 1/3 * pi * r^2 * h
        return 1/3 * 3.14 * self.r ** 2 * self.h

    def get_surf(self):
        # 원뿔 겉넓이 계산: pi * r^2 + pi * r * h
        return 3.14 * self.r ** 2 + 3.14 * self.r * self.h
    
Cone(20, 30)
unit_cone = Cone() # 객체 참조 변수 = 클래스명(초기자 파라미터), 별도로 정의해주지 않으면 위에서 정의한 기본 값이 적용
big_cone = Cone(50, 100)

# 멤버에 접근하기 위해서는 연산자 .을 사용
unit_cone.get_vol() # 부피 구하는 메소드 호출
unit_cone.get_surf() # 겉넓이 구하는 메소드 호출

print("단위 원뿔의 겉넓이와 부피는", unit_cone.get_surf(), unit_cone.get_vol(), "입니다.")
print("큰 원뿔의 겉넓이와 부피는", big_cone.get_surf(), big_cone.get_vol(), "입니다.")

# ============ BMI 계산 프로그램 ============
class BMI:
	def __init__(self, name, age, weight, height): # 초기자 지정
		self.name = name # 입력 파라미터에 들어온 값들을 데이터 필드에 넣어주는 작업
		self.age = age
		self.weight = weight
		self.height = height
		
	def get_BMI(self):
		return self.weight / (self.height) / 100 ** 2
	
	def get_status(self): # 위에서 반환 된 BMI 값을 가지고 판정하는 부분
		BMI = self.get_BMI()
		
		if BMI  >= 25:            
			return "비만"
		elif BMI  >= 23 and BMI  < 25:
			return "과체중"
		elif BMI  >= 18.5 and BMI  < 23:
			return "정상"
		else:
			return "저체중"

person1 = BMI("홍길동", 40, 78, 182) # 객체 참조 변수를 만들고 BMI 객체를 호출함

print(person1.name + "님(" + str(person1.age) + "세)의 BMI 수치는", person1.get_BMI(), "결과는", person1.get_status(), "입니다.")

# ============ 데이터 타입과 객체 ============
"Korea National Open University".lower() # 소문자로 변형 되어서 문자열 출력
number = 20
print(type(number))  # <class 'int'>
print(id(number))    # 1403902********28

symbol = "파이썬"
print(type(symbol))  # <class 'str'>
print(id(symbol))    # 1403892********08

# ============ str 메소드 ============
"I love python".upper() # "I LOVE PYTHON"
"I love python".replace("o", "i") # "I live pythin"
isymbol = "I love python".replace("o", "i")
# dir(str) # str 객체가 가진 모든 메소드와 속성 확인

# ============ 원뿔 클래스 개선 (데이터 은닉) ============
class pCone:
    def __init__(self, radius = 20, height = 30): # 초기자 지정
        if radius > 0 and height > 0:
            self.__r = radius # private 선언 -> 객체 외부에서는 접근이 불가능한 반지름과 높이 값
            self.__h = height

    def get_vol(self):
        vol = 1 / 3 * 3.14 * self.__r ** 2 * self.__h #데이터 필드의 r과 h라는 것을 알려주기 위해 꼭 self.를 앞에 표시해주어야 함
        return vol
    
    def get_surf(self):
        suf = 3.14 * self.__r ** 2 + 3.14 * self.__r * self.__h
        return suf
    
    def get_radius(self): # 접근자 통한 데이터 필드 반환
        return self.__r

    def set_radius(self, radius): # 변경자 통한 데이터 필드 설정
        if radius > 0:# 음수 값이 입력되지 않도록 if문으로 제어
            self.__r = radius
            
perfect_cone = pCone(100, 200)

perfect_cone.get_vol() # 기존에 보였던 데이터 필드 r, h가 보이지 않음

perfect_cone.r = -50

print(perfect_cone.get_surf())

# ============ BMI 계산 프로그램 (데이터 은닉닉) ============
class BMI:
	def __init__(self, name, age, weight, height): # 초기자 지정
		self.__name = name # 입력 파라미터에 들어온 값들을 데이터 필드에 넣어주는 작업
		self.__age = age
		self.__weight = weight
		self.__height = height
		
	def get_BMI(self):
		return self.__weight / (self.__height) / 100 ** 2
	
	def get_status(self): # 위에서 반환 된 BMI 값을 가지고 판정하는 부분
		BMI = self.get_BMI()
		
		if BMI  >= 25:            
			return "비만"
		elif BMI  >= 23 and BMI  < 25:
			return "과체중"
		elif BMI  >= 18.5 and BMI  < 23:
			return "정상"
		else:
			return "저체중"