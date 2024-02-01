def solution(order):
    # 메뉴별 가격을 딕셔너리로 저장
    menu = {
        'iceamericano': 4500, 'americanoice': 4500,
        'hotamericano': 4500, 'americanohot': 4500,
        'americano': 4500,
        'icecafelatte': 5000, 'cafelatteice': 5000,
        'hotcafelatte': 5000, 'cafelattehot': 5000,
        'cafelatte': 5000,
        'anything': 4500  # "아무거나"를 주문한 경우는 차가운 아메리카노로 처리
    }

    # 결제 금액 초기화
    total = 0

    # 주문을 순회하면서 가격을 더함
    for item in order:
        total += menu[item]

    return total