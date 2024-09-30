# Quiz 1.
user_input1 = input("인사를 해주세요: ")

if user_input1 == "안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요.")

# Quiz 2.
user_input2 = input("숫자를 입력하세요: ")

calculated_value = int(user_input2) + 100

if calculated_value >= 150:
    print(f"계산 결과: {calculated_value}")
else:
    print("값이 부족합니다.")

# Quiz 3.
numbers1 = [100, 200, 300]

result = []

for price in numbers1:
    tax_price = price * 1.1
    result.append(int(tax_price))

print(result)

# Quiz 4.
numbers2 = [3, 100, 23, 33, 72, 94]

result = []

for num in numbers2:
    if num % 3 == 0:
        result.append(num)

print(result)

# Quiz 5.
waiting_number = 1

while waiting_number <= 1000:
    print(f"대기번호: {waiting_number}")
    waiting_number = waiting_number + 1

# Quiz 6.
number = 1
odd_sum = 0

while number <= 100:
    if number % 2 != 0:
        odd_sum = odd_sum + number
    number = number + 1

print(f"1부터 100까지 존재하는 홀수의 합: {odd_sum}")