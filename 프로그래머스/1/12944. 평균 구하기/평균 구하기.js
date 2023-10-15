function solution(arr) {
  const sum = arr.reduce((acc, num) => acc + num, 0);
  const average = sum / arr.length;
  
  return average;
}

// 다른 방법
function average(array){
  return array.reduce((a,b) => a+b) / array.length;
}
