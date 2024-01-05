import re

def solution(myStr):
    # "a", "b", "c"를 구분자로 사용해 문자열을 분할합니다.
    split_list = re.split('[abc]', myStr)
    
    # 빈 문자열을 제거합니다.
    split_list = [s for s in split_list if s]
    
    # 리스트가 비어있는 경우 ["EMPTY"]를 반환합니다.
    if not split_list:
        return ["EMPTY"]
    
    return split_list