function solution(arr) {
  const sum = arr.reduce((acc, num) => acc + num, 0);
  const average = sum / arr.length;
  
  return average;
}