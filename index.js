const express = require('express')

const app = express()
const port = 3000

const {
    spawn
} = require('child_process');
const python = spawn('python3', ['python.py']);
python.stdout.on('data', function (data) {
    dataToSend = data.toString();

});


app.get('/', (req, res) => {

    res.sendFile(__dirname + '/index.html');
})

app.listen(port, () => console.log(`live on http://localhost:${port}`))