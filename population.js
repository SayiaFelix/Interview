function nbYear(p0, percent, aug, p) {

    let i = 0;
    while (true) {
        if (p0 >= p) { return i; }
        p0 = p0 * (1 + percent / 100) + aug;
        i++;
    }
}
// nbYear(1000, 2, 50, 1200)
console.log(nbYear(1500000, 2.5, 10000, 2000000))