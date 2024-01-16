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

app.use((req, res, next) => {
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Content-Security-Policy', 'default-src \'self\'');
  next();
});

const mongoDBUrl = 'mongodb://admin:admin@localhost:27017';
const dbName = 'hotel';
async function connectToDB() {
    try {
        const client = new MongoClient(mongoDBUrl);
        await client.connect();
        console.log('Połączono z MongoDB');
        return client.db(dbName);
    } catch (error) {
        console.error('Błąd podczas łączenia z MongoDB:', error);
        process.exit(1);
    }
}

const defaultRouter = express.Router()
const clientRouter = express.Router()
const adminRouter = express.Router()

defaultRouter.get('/', (req,res)=>{
    res.send("Witaj na stronie hotelu")
})

// Client Router

clientRouter.get('/', (req,res)=>{
    res.send("Witaj w panelu klienta <br> <a href='/client/reservation'>Zarezerwuj pokój</a>")
})

clientRouter.get('/reservation', async (req,res)=>{
    const db = await connectToDB();
    if(db === undefined) return res.send('Błąd połączenia z bazą danych');

    const rooms = await db.collection('rooms').find().toArray();

    res.render('reservationform', {
        rooms
    })
});
clientRouter.post('/add-reservation', async (req,res)=>{
    const db = await connectToDB();
    if(db === undefined) return res.send('Błąd połączenia z bazą danych');

    const {client, room} = req.body;

    const reservation = {
        client: client,
        room: room
    }

    await db.collection('reservations').insertOne(reservation);

    res.send('Rezerwacja została dodana');
})

// Admin Router

adminRouter.get('/', async (req,res)=>{
    const db = await connectToDB();
    if(db === undefined) return res.send('Błąd połączenia z bazą danych');

    const rooms = await db.collection('rooms').find().toArray();
    const reservations = await db.collection('reservations').find().toArray();

    res.render('adminpanel', {
        reservations,
        rooms
    })
})

adminRouter.post('/add-room', async (req,res)=>{
    const db = await connectToDB();
    if(db === undefined) return res.send('Błąd połączenia z bazą danych');

    const {id} = req.body;

    const room = {
        id: parseInt(id),
    }

    await db.collection('rooms').insertOne(room);

    res.redirect('/admin');
});

// App

app.use('/admin', adminRouter)
app.use('/client', clientRouter)
app.use('/', defaultRouter)

app.listen(8000, () => {
    console.log('The server was started on port 8000');
    console.log('To stop the server, press "CTRL + C"');
});

export default app;