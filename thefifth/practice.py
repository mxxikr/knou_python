# 삼각형 모양으로 *을 출력하는 프로그램을 작성하시오.
print("   *")
print("  ***")
print(" *****")
print("*******")

# input 함수
rad = input()
rad = input("반지름을 입력하세요:") # 입력 대기 후 입력값 반환

# 원뿔 계산 프로그램 개선

# 반지름 사용자 입력
rad = input("반지름을 입력하세요:")
rad = int(rad) # 정수 변환

# 높이 사용자 입력
hei = input("높이를 입력하세요:")
hei = int(hei) # 정수 변환


# 부피 계산 (TypeError 발생: 문자열 연산 불가)
# vol = 1/3 * 3.14 * rad ** 2 * hei
# print(vol)

# 부피 & 겉넓이 계산
vol = 1/3 * 3.14 * rad ** 2 * hei
suf = 3.14 * rad ** 2 + 3.14 * rad * hei

# 결과 출력
print(vol)
print(suf)

print("원뿔의 부피는 ", vol, "입니다.", sep="")