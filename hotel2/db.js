import { MongoClient } from 'mongodb';

const url = 'mongodb://admin:admin@localhost:27017';
const dbName = 'hotel';

export default async function(){
    const client = new MongoClient(url);
    await client.connect();
    const db = client.db(dbName);
    return db
};