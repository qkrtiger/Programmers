def solution(k, m, score):
    score.sort(reverse=True)  # 사과 점수를 내림차순으로 정렬합니다.
    profit = 0  # 최대 이익을 저장할 변수를 초기화합니다.

    boxes = len(score) // m  # 만들 수 있는 상자의 개수를 계산합니다.
    for i in range(boxes):
        min_score = score[i * m + m - 1]  # 현재 상자의 최저 사과 점수를 가져옵니다.
        profit += min_score * m  # 현재 상자의 이익을 누적합니다.

    return profit