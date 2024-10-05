# Quiz 1
def add(a, b, c, d):
    return a + b + c + d


def multiply(a, b, c, d):
    return a * b * c * d


print(add(1, 2, 3, 4))  # 출력: 10
print(multiply(1, 2, 3, 4))  # 출력: 24


# Quiz 2
def odd_or_even(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"


print(odd_or_even(5))  # 출력: 홀수
print(odd_or_even(8))  # 출력: 짝수


# Quiz 3
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(calculate_average([1, 2, 3, 4, 5]))


# Quiz 4
class GameCharacter:
    def __init__(self, id, gender, job):
        self.id = id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")


character = GameCharacter("player1", "남성", "전사")
character.attack()


# Quiz 5
class RealEstate:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def display_info(self):
        print(f"위치: {self.location}")
        print(f"평수: {self.size}")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price}")
        print(f"건축 연도: {self.year_built}")


estate = RealEstate("서울", 85, "아파트", 500000000, 2010)
estate.display_info()