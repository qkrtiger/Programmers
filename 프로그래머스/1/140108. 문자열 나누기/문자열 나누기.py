def solution(s):
    def count_letters(sub_s, x):
        count_x = sub_s.count(x)
        count_other = len(sub_s) - count_x
        return count_x, count_other

    def split_string(sub_s, x):
        for i in range(1, len(sub_s)):
            count_x, count_other = count_letters(sub_s[:i], x)
            if count_x == count_other:
                return sub_s[:i], sub_s[i:]
        return sub_s, ""

    def decompose(s):
        result = []
        while s:
            x = s[0]
            sub_s, s = split_string(s, x)
            result.append(sub_s)
        return len(result)

    return decompose(s)