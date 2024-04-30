def solution(food):
    eat_food = '' #음식 저장 문자열 변수
    
    for idx, i in enumerate(food[1:]):
        # 각 음식을 반으로 나누고, 그 결과를 문자열로 변환하여 eat_food에 추가
        # 이때, 음식의 인덱스는 1부터 시작하므로 idx에 1을 더해줍니다.
        eat_food += str(idx+1) * (i//2)
        
        
    # 왼쪽에서 먹을 음식과 오른쪽에서 먹을 음식 사이에 물(0)을 추가하여 결과 문자열을 생성
    result = eat_food + "0" + eat_food[::-1]
    
    # 결과 문자열을 반환
    return result