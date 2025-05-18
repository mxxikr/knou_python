#  ============ 2차원 리스트 동적 생성 ============ 
import random as rd

# 행의 개수 nRows, 열의 개수 nColumns
nRows, nColumns = 3, 4
distance = []

for i in range(nRows): # 행의 개수만큼 반복
    row = [] # 행을 저장할 리스트
    for j in range(nColumns): # 열의 개수만큼 반복
        row.append(rd.randint(0, 99)) # 0~99 사이의 난수 생성
    distance.append(row) # 2차원 리스트에 행 추가

print(distance)

#  ============ 2차원 리스트 순회 ============ 
# 출발 도시(departure) 순회
for dep in distance: # dep 출발 도시 변수
    # 도착 도시(destination) 순회
    for des in dep: # des 도착 도시 변수
        print(des, end = " ") # 각 도시 간 거리를 출력
    print() # 한 행의 출력이 끝나면 줄 바꿈

#  ============ 틱택토 게임 구현 ============ 
import random

class Tic_Tac_Toe: 
    # 게임판 생성
    def __init__(self):
        self.board = [] # 클래스 전역에서 사용하기 위해 self 붙임

    # 게임판 초기화
    def create_board(self): 
        for i in range(3):
            row = [] # 하나의 행 생성
            for j in range(3):
                row.append('*') # *로 채운 3개의 칸 만들기
            self.board.append(row) # self.board 판에 row 넣음
				
    # 첫 플레이어 선택
    def select_first_player(self):
        if random.randint(0, 1) == 0: # 0, 1 포함해 값 랜덤하게 뽑고 0이 나오면
            return 'X' # 컴퓨터(X)가 플레이어
        else:
            return 'O' # 사용자(O)가 플레이어

    # 기호 표시
    def mark_spot(self, row, col, player):
        self.board[row][col] = player

    # 승리 상태 확인
    def is_win(self, player):
        n = len(self.board) # board가 가리키는 리스트의 원소의 개수 추출
        
        # 행 확인
        for i in range(n):
            win = True # 승리 상황이라 일단 가정하고 반복할 때마다 각 행에 대해서 다른게 있는지 체크
            for j in range(n):
                if self.board[i][j] != player: # 세칸이 모두 player의 말과 다르다는 것은 승리 상황이 아니라는 의미
                    win = False
                    break # 반복 중단
        if win == True:
            return win # 승리 상황일 경우 True를 반환

        # 열 확인
        for i in range(n):
            win = True # 승리 상황이라 일단 가정하고 반복할 때마다 각 행에 대해서 다른게 있는지 체크
            for j in range(n):
                if self.board[j][i] != player: # 열부터 확인할 때에는 i와 j의 위치 바꿈
                    win = False
                    break # 반복 중단
        if win == True: # 할당 연산자 =와 비교 연산자 == 사용에 유의
            return win # 승리 상황일 경우 True를 반환

        # 오른쪽 대각선 확인
        win = True # 승리 상황이라 일단 가정하고 반복할 때마다 각 행에 대해서 다른게 있는지 체크
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win == True:
            return win

        # 왼쪽 대각선 확인
        win = True # 승리 상황이라 일단 가정하고 반복할 때마다 각 행에 대해서 다른게 있는지 체크
        for i in range(n):
            if self.board[i][n - i - 1] != player:
                win = False
                break
        if win == True:
            return win

        return False # 행, 열, 대각선 확인 후에도 승리 상황이 아닌 경우는 False 반환

    # 잔여 빈칸 여부 확인
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if item == '*':
                    return False
        return True

    # 플레이어 변경
    def next_player(self, player):
        if player == 'O':
            return 'X'
        else:
            return 'O'
        # return 'X' if player == 'O' else 'O'

    # 현재 게임판 상태 출력
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end = " ") # 출력할 때 줄바꿈 되지 않게
            print()

    # 게임 시작
    def start(self):
        # 새 게임 판 생성
        self.create_board()
        self.show_board()

        # 첫 플레이어 선택
        player = self.select_first_player()

        # 게임 루프 시작(이벤트가 발생할 때까지 기다림 반복)
        while True:
            # 다음 플레이어 안내	    
            if player == 'X':
                print("컴퓨터 차례입니다.")
            else:
                print("사용자 차례입니다.")

            # 현재 게임 판 상태 출력
            self.show_board()

            # 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
            if player == 'X':
                while True:
                    row, col = random.randint(1, 3), random.randint(1, 3) # 사용자와 동일한 입력 상황을 맞추기 위해 (1, 3)으로 표기
                    if self.board[row - 1][col - 1] == '*': # 무작위로 입력 받은 게임판의 좌표 값이 빈칸('*')이면 반복을 중단
                        break
                print("컴퓨터가 행 " + str(row) + ", 열" + str(col) + "을/를 선택했습니다.") 
                print()
            else:
                row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요: ").split())) # 공백 기준으로 문자 분리
                print("사용자가 행 " + str(row) + ", 열" + str(col) + "을/를 선택했습니다.") 
                print()

            # row, col 입력 값이 0, 0인 경우 게임 종료
            if row == 0 and col ==0:
                print("게임을 종료합니다.")
                break

            # 입력 된 위치 표시
            self.mark_spot(row - 1, col - 1, player)
            self.show_board()

            # 현재 플레이어가 이겼는지 확인 
            if self.is_win(player) == True: # 승리 상황 메소드 값이 True인지 확인하고
                if player == 'X': # 승리자에 맞는 메시지 출
                    print("컴퓨터가 이겼습니다. 다시 도전하세요")
                else:
                    print("사용자가 이겼습니다. 축하합니다.")
                break # 상황 종료
                
            # 게임판 가득참 확인, 빈칸 여부 확인
            if self.is_board_full() == True:
                print("무승부 입니다. 다시 도전하세요.")
                break

            # 플레이어 변경 확인
            player = self.next_player(player)

			# 최종 게임판 출력
            print()
            self.show_board()

# 게임 생성
TTT = Tic_Tac_Toe()

#게임 시작
TTT.start()