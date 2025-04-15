#  ============ '저는 파이썬을 잘 다룰 수 있습니다'를 5번 출력하는 프로그램을 작성하시오. (while문 미사용) ============ 
# 메시지 저장
msg = "저는 파이썬을 잘 다룰 수 있습니다."

# 5번 반복 출력 (개선 전)
print(msg)
print(msg)
print(msg)
print(msg)
print(msg)

#  ============ '저는 파이썬을 잘 다룰 수 있습니다'를 5번 출력하는 프로그램을 작성하시오. (while문 사용) ============ 
# 메시지 저장
msg = "저는 파이썬을 잘 다룰 수 있습니다."

# 5번 반복 출력 (while 사용)
count = 1
while count <= 5:
    print(msg)
    count = count + 1 # 추가하지않으면 무한 반복함

#  ============ n까지 합 계산 프로그램 (반복 구조 설계 전략 적용) ============ 
# 초기값 설정
sum_value = 0
i = 1

# 사용자 입력 받기
last = int(input("어디까지 더할까요?: ")) # 입력값을 정수로 변환

# 합 계산 (while 사용)
while i <= last: # 종결 조건
    sum_value = sum_value + i
    i = i + 1

# 결과 출력
print(f"1부터 {last}까지의 합은 {sum_value}입니다.")

#  ============ 구구단 출력 프로그램 ============ 
# 단 입력 받기
base = int(input("출력할 단을 입력하세요: "))

# 구구단 출력 (while 사용)
i = 1
while i <= 9: # 종결 조건 작성
    print(base, "X", i, "=", base * i)
    i = i + 1

#  ============ 리스트의 생성 ============ 
hei_list = [1, 4, 14, 26, 31]
# 다양한 자료형을 포함하는 리스트 생성
body = [181, 78, "dark brown", "black"]
print(hei_list[2])  # 출력: 14
hei_list[4] = 45
print(hei_list)     # 출력: [1, 5, 14, 26, 45]

#  ============ 계수 제어 반복의 사용 ============ 
# 리스트 생성
hei_list = [1, 4, 14, 26, 31]

# 리스트의 각 요소를 순회하며 출력
for hei in hei_list:
    print(hei)

# ============ 원뿔 계산 프로그램 개선 (반지름은 10이고 높이가 1, 5, 14, 26, 31인 원뿔의 부피와 겉넓이를 각각 출력하시오.) ============ 
rad = 10
hei_list = [1, 4, 14, 26, 31]

# 리스트의 각 요소를 순회하며 출력
for hei in hei_list:
    # 부피 & 겉넓이 계산
    vol = 1 / 3 * 3.14 * rad ** 2 + 3.14 * rad * hei
    surf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("반지름", rad, "높이", hei, "원뿔")
    print("원뿔의 부피는", vol, "입니다.")
    print("원뿔의 겉넓이는", surf, "입니다.")

# ============ 원뿔 계산 프로그램 개선 (반지름과 높이가 (10, 1), (20, 5), (30, 14)인 원뿔의 부피와 겉넓이를 각각 출력하시오.) ============ 
rad_list = range(10, 31, 10)
hei_list = [1, 5, 14]

for rad, hei in zip(rad_list, hei_list):
    vol = 1 / 3 * 3.14 * rad ** 2 + 3.14 * rad * hei
    surf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("반지름", rad, "높이", hei, "원뿔")
    print("원뿔의 부피는", vol, "입니다.")
    print("원뿔의 겉넓이는", surf, "입니다.")

# ============ 반복 출력 프로그램 개선 (for 와 range 사용) ============ 
# 메시지 저장
msg = "저는 파이썬을 잘 다룰 수 있습니다."

# 5번 반복 출력
for count in range(1, 6): # 1부터 5까지 반복
    print(msg)

# ============ 구구단 출력 프로그램 개선 (중첩 반복 및 format 사용) ============ 
# 구구단표 헤더 출력
print(format("구구단표", ">20s")) # 제목 가운데 정렬 느낌으로

# 표 머리 출력
print("|", end="")
for j in range(1, 10):
    print("  ", j, end = "") # 각 숫자 헤더 4칸 오른쪽 정렬
# 새로운 행 삽입
print()
print("-" * 40) # 구분선

# 구구단표 본문 출력
for i in range(1, 10): # 단 (1단 ~ 9단)
    print(i, "|", end = "") # 단 표시
    for j in range(1, 10): # 곱하는 수 (1 ~ 9)
        print(format(i * j, ">4d"), end="") # 결과값 4칸 오른쪽 정렬
    print() # 다음 단으로 넘어갈 때 줄바꿈