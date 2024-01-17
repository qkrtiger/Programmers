def solution(rank, attendance):
    # 출석한 학생과 그들의 등수를 함께 저장하기 위한 리스트
    attended_students = [(i, r) for i, (r, a) in enumerate(zip(rank, attendance)) if a]
    
    # 출석한 학생들의 등수에 따라 정렬 (등수가 낮을수록 좋으므로 오름차순 정렬)
    attended_students.sort(key=lambda x: x[1])
    
    # 상위 3명의 학생 번호 추출
    a, b, c = [student[0] for student in attended_students[:3]]
    
    # 문제에서 요구하는 계산 수행
    return 10000 * a + 100 * b + c