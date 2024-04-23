def solution(board, h, w):
    
    count = 0
    color = board[h][w]
    
    # 상, 하, 좌, 우
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    # directions 순회 (상 -> 하 -> 좌 -> 우)
    for dir_h, dir_w in directions:

        # 이동할 인덱스 생성
        mov_h = h + dir_h 
        mov_w = w + dir_w

        # 이동한 인덱스가 유효할 시
        if (0 <= mov_h <= len(board)-1) and (0 <= mov_w <= len(board[0])-1):

            # 이동한 칸의 색과 board[h][w]의 색이 같을 시 count += 1
            count += int(color == board[mov_h][mov_w])

    return count