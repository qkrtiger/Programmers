def solution(n, k):
    # k의 배수를 저장할 빈 리스트 생성
    multiples_of_k = []

    # 1부터 n까지의 정수 중에서 k의 배수를 찾아서 리스트에 추가
    for i in range(1, n + 1):
        if i % k == 0:
            multiples_of_k.append(i)

    return multiples_of_k