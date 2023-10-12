str = input().strip()  # 입력 문자열에서 앞뒤 공백 제거
if 1 <= len(str) <= 20:
    print(str.swapcase())
else:
    print("입력 문자열의 길이는 1 이상 20 이하이어야 합니다.")