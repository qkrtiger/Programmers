function solution(a, b) {
  const ab = parseInt(a.toString() + b.toString());
  const ba = parseInt(b.toString() + a.toString());

  return ab >= ba ? ab : ba;
}