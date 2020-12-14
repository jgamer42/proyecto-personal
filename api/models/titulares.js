const { Schema, model } = require('mongoose');

const titularSchema =new Schema({
    date:String,
    news_paper:String,
    title:String,
    link:String, 
    _id:String,
    sumary:String
    },
    {collection:"titulares"}
);

module.exports= model('titular',titularSchema)