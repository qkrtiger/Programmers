def solution(nums):
    unique_pokemon = set(nums)  # 중복을 제외한 폰켓몬 종류를 구함
    max_pokemon = len(nums) // 2  # 선택할 수 있는 최대 폰켓몬 수
    return min(max_pokemon, len(unique_pokemon))