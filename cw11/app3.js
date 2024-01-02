import express from 'express';
import morgan from 'morgan';
import bodyParser from 'body-parser';
import { MongoClient } from 'mongodb';

const app = express();
app.locals.pretty = app.get('env') === 'development';
app.use(bodyParser.urlencoded({ extended: true }));
app.use(morgan('dev'));

app.set('view engine', 'pug');
app.set('views', './views');

app.use('/static', express.static('static'))

const url = 'mongodb://admin:admin@localhost:27017';
const dbName = 'AGH';
const collectionName = 'students';

/* ------------- */
/* Route 'GET /' */
/* ------------- */

app.get('/:department?', async (req, res) => {
    const { department } = req.params;

    const imagePath = '/static/images/400.jpg';

    try {
        const client = new MongoClient(url);
        await client.connect();
        const db = client.db(dbName);
        const collection = db.collection(collectionName);
        const query = department ? { department: department } : {};
        const students = await collection.find(query).toArray();
        res.render('index', { students, imagePath });
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

/* ------------- */
/* Route 'GET /submit' */
/* ------------- */

app.get('/submit', (request, response) => {
    // Processing the form content, if the relative URL is '/submit', and the GET method was used to send data to the server'
    /* ************************************************** */
    // Setting an answer header — we inform the browser that the returned data is plain text
    response.set('Content-Type', 'text/plain')
    /* ************************************************** */
    // Place given data (here: 'Hello <name>') in the body of the answer
    response.send(`Hello ${request.query.name}`); // Send a response to the browser
});


app.post('/', (request, response) => {
    // Processing the form content, if the relative URL is '/submit', and the GET method was used to send data to the server'
    /* ************************************************** */
    // Setting an answer header — we inform the browser that the returned data is plain text
    response.set('Content-Type', 'text/plain')
    /* ************************************************** */
    // Place given data (here: 'Hello <name>') in the body of the answer
    response.send(`Hello ${request.body.name}`); // Send a response to the browser
});



/* ************************************************ */

app.listen(8000, () => {
    console.log('The server was started on port 8000');
    console.log('To stop the server, press "CTRL + C"');
});


export default app;