function solution(a, b) {
  const ab = parseInt(a.toString() + b.toString());
  const ba = parseInt(b.toString() + a.toString());

  return ab >= ba ? ab : ba;
}

// 다른 방법
function solution(a, b) {
    return Math.max(Number(`${a}${b}`), Number(`${b}${a}`))
}
