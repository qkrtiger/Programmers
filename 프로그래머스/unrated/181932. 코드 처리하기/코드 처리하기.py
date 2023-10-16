def solution(code):
    ret = ""  # 결과 문자열을 저장하는 변수
    mode = 0  # 시작 모드는 0
    idx = 0  # code 문자열을 읽는 인덱스

    # code 문자열을 끝까지 읽을 때까지 반복
    while idx < len(code):
        # 현재 모드에 따라 다른 동작 수행
        if mode == 0:
            # mode가 0일 때
            if code[idx] != "1":
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                mode = 1
        else:
            # mode가 1일 때
            if code[idx] != "1":
                if idx % 2 != 0:
                    ret += code[idx]
            else:
                mode = 0

        # 다음 문자로 이동
        idx += 1

    # 만약 ret이 빈 문자열이라면 "EMPTY" 반환
    if ret == "":
        return "EMPTY"
    else:
        return ret