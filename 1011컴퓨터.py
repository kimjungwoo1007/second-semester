class User:

 def __init__(self, name, age, phone):
    self.name = name
    self.age = age
    self.phone = phone

 def info(self):
    print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.phone}입니다.")


user1 = User("000", 000, "010-0000-0000")
user1.info()