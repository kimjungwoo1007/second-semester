#문제 1번
import random

def generate_lotto_numbers():
    result = []
    while len(result) < 6:
        number = random.randint(1, 45)
        if number not in result:
            result.append(number)
    return result

# 함수 사용 예시
lotto_numbers = generate_lotto_numbers()
print(lotto_numbers)

#문제 2번
class Gugudan:
    def __init__(self, num):
        self.num = num

    def output(self):
        for i in range(1, 10):
            result = self.num * i
            print(f"{self.num} X {i} = {result}")

# 사용 예시
num = int(input("구구단을 출력할 숫자를 입력하세요: "))
gugudan = Gugudan(num)
gugudan.output() 