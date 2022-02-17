const express = require('express')
const app = express()
const port = 3000

const {
    spawn
} = require("child_process");

const py = spawn("python3", ['script.py', '%232GPUV2Y0', '%232L0YRYUQR', '%23C9PR9PJ02', '%23CQLGCCJ', '%232VUQ9YJ']);
py.stdout.on("data", data => {
    console.log(`stdout: ${data}`);
});

app.get('/', (req, res) => {


    res.sendFile(__dirname + '/index.html');
})

app.listen(port, () => console.log(`live on http://localhost:${port}`))