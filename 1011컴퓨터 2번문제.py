def check_length_of_message(message):
    if len(message) <= 20:
        return 50
    else:
        return 100

message = input("문자 메시지를 입력하세요: ")

fee = check_length_of_message(message)
print(f"문자 메시지 요금은 {fee}원입니다.")