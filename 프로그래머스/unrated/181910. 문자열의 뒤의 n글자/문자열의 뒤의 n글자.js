function solution(my_string, n) {
    if(n >= 0 <= my_string.length){
        return my_string.slice(-n);
    }else {
        return '';
    }
}