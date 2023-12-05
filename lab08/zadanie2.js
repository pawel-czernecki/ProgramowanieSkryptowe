'use strict';

function sum(x,y) {
    return x+y;
}

function sum_strings(arr) {
    return arr.reduce((sum, str) => {
        const num = parseInt(str, 10);
        if (!isNaN(num)) {
            return sum + num;
        }
        return sum;
    }, 0);
}

function digits(s) {
    const oddSum = s.split('').filter(char => /[13579]/.test(char)).reduce((sum, digit) => sum + parseInt(digit, 10), 0);
    const evenSum = s.split('').filter(char => /[02468]/.test(char)).reduce((sum, digit) => sum + parseInt(digit, 10), 0);
    return [oddSum, evenSum];
}

function letters(s) {
    const lowercaseCount = s.split('').filter(char => /[a-z]/.test(char)).length;
    const uppercaseCount = s.split('').filter(char => /[A-Z]/.test(char)).length;
    return [lowercaseCount, uppercaseCount];
}