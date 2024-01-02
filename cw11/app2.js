import express from 'express';
import morgan from 'morgan';
import bodyParser from 'body-parser';

/* *************************** */
/* Configuring the application */
/* *************************** */
const app = express();

//app.locals.pretty = app.get('env') === 'development'; // The resulting HTML code will be indented in the development environment
app.use(bodyParser.urlencoded({ extended: true }));

/* ************************************************ */

app.use(morgan('dev')); 

app.set('view engine', 'pug')
app.set('views', './views')

app.use('/static', express.static('static'))

/* ******** */
/* "Routes" */
/* ******** */

/* ------------- */
/* Route 'GET /' */
/* ------------- */
app.get('/', (request, response) => {

    const students = [
        {
            fname: 'Jan',
            lname: 'Kowalski'
        },
        {
            fname: 'Anna',
            lname: 'Nowak'
        },
    ];

    const imagePath = '/static/images/400.jpg';

    response.render('index', {
        students,
        imagePath
    }); // Render the 'index' view
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