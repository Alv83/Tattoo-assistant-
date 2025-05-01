const express = require('express');
const app = express();
app.use(express.json());

app.post('/webhook', (req, res) => {
  console.log('Mensaje recibido:', req.body);
  res.send('Mensaje recibido');
});

const listener = app.listen(process.env.PORT, () => {
  console.log('Servidor escuchando en el puerto ' + listener.address().port);
});
