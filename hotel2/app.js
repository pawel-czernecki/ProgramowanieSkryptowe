import express from 'express';
import morgan from 'morgan';
import bodyParser from 'body-parser';
import db from './db.js'

const app = express();
app.locals.pretty = app.get('env') === 'development';

app.use(bodyParser.urlencoded({ extended: true }));
app.use(morgan('dev'));

app.set('view engine', 'pug');
app.set('views', './views');

const defaultRouter = express.Router()
const clientRouter = express.Router()
const adminRouter = express.Router()

defaultRouter.get('/', (req,res)=>{
    res.send("Witaj na stronie hotelu")
})

// Client Router

clientRouter.get('/', (req,res)=>{
    res.send("Witaj w panelu klienta");
})

clientRouter.get('/add', (req,res)=>{
    res.render('reservationform')
})

clientRouter.post('/add', (req,res)=>{
    res.send('Dodano rezerwacje')
})

// Admin Router

adminRouter.get('/', (req,res)=>{

    const rooms = db.collection('rooms').toArray();
    const reservations = db.collection('reservations').toArray();

    res.render('adminpanel', {
        reservations,
        rooms
    })
})

// App

app.use('/admin', adminRouter)
app.use('/client', clientRouter)
app.use('/', defaultRouter)

app.listen(8000, () => {
    console.log('The server was started on port 8000');
    console.log('To stop the server, press "CTRL + C"');
});

export default app;