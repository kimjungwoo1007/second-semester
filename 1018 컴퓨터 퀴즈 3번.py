import random

# 도박꾼 클래스
class Gambler:
    def __init__(self, name, balance, addiction_level=0):
        self.name = name
        self.balance = balance
        self.addiction_level = addiction_level  # 중독 레벨
        self.time_spent = 0  # 도박에 사용한 시간

    def gamble(self, amount):
        if self.balance < amount:
            print(f"{self.name}님, 잔액이 부족합니다!")
            return
        self.balance -= amount
        self.time_spent += 1
        result = random.choice([True, False])  # 승리(True) 또는 패배(False)
        if result:
            winnings = amount * 2
            self.balance += winnings
            print(f"{self.name}님이 {winnings}만큼 승리하였습니다!")
        else:
            print(f"{self.name}님이 {amount}만큼 잃었습니다.")
        self.addiction_level += 1  # 도박할 때마다 중독 레벨 증가

    def check_balance(self):
        print(f"{self.name}님의 현재 잔액: {self.balance}")

    def reset_addiction(self):
        print(f"{self.name}님의 중독 레벨을 초기화합니다.")
        self.addiction_level = 0

# 카지노 클래스
class Casino:
    def __init__(self, name):
        self.name = name
        self.total_winnings = 0  # 카지노가 얻은 이익

    def host_game(self, gambler, amount):
        print(f"{self.name}에서 {gambler.name}님이 {amount}만큼 베팅합니다.")
        gambler.gamble(amount)
        self.total_winnings += amount if gambler.balance < amount else 0

    def report(self):
        print(f"{self.name}의 총 이익: {self.total_winnings}")

# 중독 관리 시스템 클래스
class AddictionSystem:
    def __init__(self, max_addiction_level=10):
        self.max_addiction_level = max_addiction_level

    def monitor(self, gambler):
        if gambler.addiction_level >= self.max_addiction_level:
            print(f"{gambler.name}님이 위험 수준의 중독 상태에 도달했습니다. 도박을 중지하세요.")
            gambler.reset_addiction()

# 사용 예시
gambler = Gambler(name="홍길동", balance=1000)
casino = Casino(name="Lucky Casino")
addiction_system = AddictionSystem()

# 도박 과정
casino.host_game(gambler, 200)
casino.host_game(gambler, 150)
gambler.check_balance()

# 중독 상태 모니터링
addiction_system.monitor(gambler)