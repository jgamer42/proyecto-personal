const router = require("express").Router();
const titulares = require("../models/titulares");

router.get("/all",async (req,res)=>{
    const a = await titulares.find();
    console.log(a);
    res.status(200).json(a);
    return;
});
    
module.exports= router;