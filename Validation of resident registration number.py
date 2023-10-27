def validate_resident_id(resident_id):
    if len(resident_id) != 13:
        return False  # 주민등록번호는 13자리여야 합니다.

    # 주민등록번호 유효성 검사
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    last_digit = int(resident_id[-1])
    check_sum = 0

    for i in range(12):
        check_sum += int(resident_id[i]) * weights[i]

    remainder = check_sum % 11
    result = 11 - remainder

    # 결과 값이 주민등록번호의 마지막 자리 숫자와 일치하는지 확인
    if result == last_digit:
        return True
    elif result == 10 and last_digit == 0:
        return True
    elif result == 11 and last_digit == 1:
        return True
    else:
        return False

# 주민등록번호 입력 받기
resident_id = input("주민등록번호를 입력하세요 (예: 123456-1234567): ")


resident_id = resident_id.replace("-", "")

if validate_resident_id(resident_id):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
