function solution(my_string) {
  const suffixes = [];

  // 문자열의 모든 접미사를 추출하여 배열에 저장
  for (let i = 0; i < my_string.length; i++) {
    suffixes.push(my_string.substring(i));
  }

  // 접미사 배열을 사전순으로 정렬
  suffixes.sort();

  return suffixes;
}