import http from 'http';
import { promises as fsPromises } from 'fs';
import path from 'path';
import { parse } from 'querystring';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const server = http.createServer(async (req, res) => {
    const urlParsed = new URL(req.url, `http://${req.headers.host}`);

    if (urlParsed.pathname === '/' && req.method === 'GET') {
        // Obsługa żądania GET dla głównej strony
        res.writeHead(200, { 'Content-Type': 'text/html' });
        const guestBookEntries = await getGuestBookEntries();
        res.end(generateGuestBookPage(guestBookEntries));
    } else if (urlParsed.pathname === '/' && req.method === 'POST') {
        // Obsługa żądania POST z formularza
        let body = '';
        req.on('data', (chunk) => {
            body += chunk.toString();
        });

        req.on('end', async () => {
            const formData = parse(body);
            const guestBookEntry = {
                name: formData.name,
                message: formData.message,
            };

            await saveGuestBookEntry(guestBookEntry);
            res.writeHead(302, { 'Location': '/' });
            res.end();
        });
    } else {
        // Obsługa innych ścieżek URL
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

const PORT = 8000;

server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});

/**
 * Funkcja do odczytu wpisów z księgi gości
 * @returns {Promise<Array>} Promise z tablicą obiektów zawierających wpisy z księgi gości
 * @async
 * */

async function getGuestBookEntries() {
    const filePath = path.join(__dirname, 'guestbook.txt');
    try {
        const data = await fsPromises.readFile(filePath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        return [];
    }
}


/**
 * Funkcja do zapisu wpisu do księgi gości
 * @param entry
 * @returns {Promise<void>}
 */
async function saveGuestBookEntry(entry) {
    const filePath = path.join(__dirname, 'guestbook.txt');
    const entries = await getGuestBookEntries();
    entries.push(entry);
    await fsPromises.writeFile(filePath, JSON.stringify(entries), 'utf8');
}

/**
 * Funkcja do generowania strony z księgą gości
 * @param entries
 * @returns {string}
 */
function generateGuestBookPage(entries) {
    const header = '<h1>Ksiega gosci</h1>';
    const form = `
        <h2>Formularz</h2>
        <form method="post" action="/">
            <label for="name">Imie i nazwisko:</label>
            <input type="text" id="name" name="name" required><br>
            <label for="message">Tresc wpisu:</label>
            <textarea id="message" name="message" required></textarea><br>
            <button type="submit">Dodaj wpis</button>
        </form>
    `;

    const guestBookList = entries.map(entry =>
        `<p><strong>${entry.name}</strong>: <br>${entry.message}</p>`
    ).join('');

    return `${header}${guestBookList}${form}`;
}
