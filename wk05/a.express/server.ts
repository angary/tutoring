import express, { json, Request, Response } from 'express';
import morgan from 'morgan';
import { PORT, SERVER_URL } from './config';

const app = express();

app.use(json());
// For debugging purposes - logs http requests
app.use(morgan('dev'));

app.post('/addnameage', (req: Request, res: Response) => {
  // TODO
});

// TODO

app.listen(PORT, () => {
  console.log(`Starting Express Server at the URL: '${SERVER_URL}'`);
});
