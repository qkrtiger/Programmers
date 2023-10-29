function solution(my_strings, parts) {
    let result = [];
    
    //반복문 : my_strings에 입력된 개수만큼
    for(let i=0; i<my_strings.length;i++){
        const[s,e] = parts[i]; //parts요소를 각각 s,e에 할당한다.
        //subString = my_string에서 s~e+1만큼 문자열 자르기
        const subString = my_strings[i].substring(s, e+1);
        result.push(subString);
    }
    return result.join('');
}