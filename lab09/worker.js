addEventListener('message', function(event) {
    var primes = calculatePrimes(event.data);
    postMessage(primes);
    close();
});

function calculatePrimes(iterations) {
    var primes = [];
    for (var i = 0; i < iterations; i++) {
        var candidate = i * (1000000000 * Math.random());
        var isPrime = true;
        for (var c = 2; c <= Math.sqrt(candidate); ++c) {
            if (candidate % c === 0) {
                isPrime = false;
                break;
            }
        } 
        if (isPrime) {
            primes.push(candidate);
        }
    }
    return primes;
}