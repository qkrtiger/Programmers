def solution(picture, k):
    # picture 배열의 크기를 구합니다.
    rows = len(picture)
    cols = len(picture[0])
    
    # 새로운 그림 파일을 담을 배열을 생성합니다.
    new_picture = []
    
    # picture 배열을 탐색하면서 가로, 세로로 k배 늘린 그림 파일을 생성합니다.
    for row in picture:
        # 행을 k번 반복해서 새로운 행을 생성합니다.
        new_row = ""
        for pixel in row:
            new_row += pixel * k
        for i in range(k):
            new_picture.append(new_row)
    
    # 새로운 그림 파일을 반환합니다.
    return new_picture
