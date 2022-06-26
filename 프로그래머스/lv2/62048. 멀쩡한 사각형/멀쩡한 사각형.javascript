const gcd = (w, h) => {
  let c;

  while(h !== 0) {
    c = w % h;
    w = h;
    h = c;
  }
  return w; 
}

function solution(w, h) {
  var answer = 1;

  // 못쓰는 사각형개수 = (w/최대공약수 + h/최대공약수 -1) * 최대공약수
  const maxGongYaksu = gcd(w, h);
  divideW = w / maxGongYaksu;
  divideH = h / maxGongYaksu;
  answer = w*h - ((divideW + divideH - 1) * maxGongYaksu);

  return answer;
}