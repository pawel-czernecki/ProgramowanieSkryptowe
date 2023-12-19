const fs = require('fs');

const filePath = 'counter.txt';

function readCounterSync() {
    try {
        const data = fs.readFileSync(filePath, 'utf8');
        return parseInt(data, 10) || 0;
    } catch (error) {
        return 0;
    }
}

function writeCounterSync(count) {
    fs.writeFileSync(filePath, count.toString(), 'utf8');
}

function readCounterAsync(callback) {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return callback(null, 0);
        }
        const count = parseInt(data, 10) || 0;
        callback(null, count);
    });
}

function writeCounterAsync(count, callback) {
    fs.writeFile(filePath, count.toString(), 'utf8', (err) => {
        if (err) {
            return callback(err);
        }
        callback(null);
    });
}

function executeCommands() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
        terminal: false
    });

    console.log('Wprowadź komendy — naciśnięcie Ctrl+D kończy wprowadzanie danych');

    rl.on('line', (input) => {
        const command = input.trim();
        if (command.toLowerCase() === 'exit') {
            rl.close();
        } else {
            const exec = require('child_process').exec;
            exec(command, (error, stdout, stderr) => {
                if (stdout) {
                    console.log(stdout);
                }
                if (stderr) {
                    console.error(stderr);
                }
                if (error !== null) {
                    console.error(`Error: ${error}`);
                }
            });
        }
    });

    rl.on('close', () => {
        console.log('Koniec wprowadzania danych');
    });
}

function main() {
    const option = process.argv[2];

    if (option === '--sync' || option === '--async') {
        let count;

        if (option === '--sync') {
            count = readCounterSync();
            console.log(`Liczba uruchomień: ${count + 1}`);
            writeCounterSync(count + 1);
        } else if (option === '--async') {
            readCounterAsync((err, data) => {
                if (err) {
                    console.error('Błąd odczytu licznika:', err);
                } else {
                    count = data;
                    console.log(`Liczba uruchomień: ${count + 1}`);
                    writeCounterAsync(count + 1, (err) => {
                        if (err) {
                            console.error('Błąd zapisu licznika:', err);
                        }
                    });
                }
            });
        }
    } else {
        executeCommands();
    }
}

main();