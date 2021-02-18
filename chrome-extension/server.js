const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");

const app = express()
const port = 8081

app.get("/", (req, res) => {
  res.send("Hello Wolrd!");
})

app.post("/test", async (req, res) => {
  console.log("made it here");
  fs.writeFile("inputedStuff.txt", req.body);
  return res.status(200);
})

app.listen(port, ()=>{
  console.log("Listening");
})