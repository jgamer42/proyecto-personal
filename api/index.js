const express = require("express");
const mongoose = require("mongoose");
const db_uri = process.env.DB_URI
//const db_uri = "mongodb://localhost:27017"
const app = express();
mongoose.connect(db_uri, {
    useUnifiedTopology: true,
    useNewUrlParser: true,
    useCreateIndex: true,
});
const conexion = mongoose.connection;
conexion.once("open",()=>{
    console.log("se conecto",db_uri)
});

const titularesRouter = require("./routes/titulares");
app.use("/titulares",titularesRouter);

app.listen(5000,()=>{
    console.log("servidor en el puerto 5000");
});