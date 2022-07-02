import express, { json, Request, Response } from 'express';
import morgan from 'morgan';
import { PORT, SERVER_URL } from './config';
import { addNameAge, clear, editNameAge, getNamesAges, getStats, removeNameAge } from './names.ages';

const app = express();

app.use(json());
// For debugging purposes - logs http requests
app.use(morgan('dev'));

app.post('/addnameage', (req: Request, res: Response) => {
  const { name, age } = req.body;
  res.json(addNameAge(name, age));
});

app.get('/getnamesages', (req: Request, res: Response) => {
  const minAge = req.query.minAge as string;
  res.json(getNamesAges(minAge ? parseInt(minAge) : undefined));
});

app.put('/editnameage', (req: Request, res: Response) => {
  const { name, age } = req.body;
  res.json(editNameAge(name, age));
});

app.delete('/removenameage', (req: Request, res: Response) => {
  res.json(removeNameAge(req.query.name as string));
});

app.get('/getstats', (req: Request, res: Response) => {
  res.json(getStats());
});

app.delete('/clear', (req: Request, res: Response) => {
  res.json(clear());
});

app.listen(PORT, () => {
  console.log(`Starting Express Server at the URL: '${SERVER_URL}'`);
});
