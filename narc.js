function narcissistic(value) {
    let digits = (value + '').split('').map(Number);
    let narc = digits.reduce((b, d) => b + (d ** digits.length), 0)
    return narc === value;
}

console.log(narcissistic(4012))
console.log(narcissistic(153))
console.log(narcissistic(371))