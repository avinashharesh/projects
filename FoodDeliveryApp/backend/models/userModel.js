const mongoose=require('mongoose')

const Schema=mongoose.Schema

const userSchema=new Schema({
    name:{
        type:String,
        required:true
    },
    location:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true,
        unique: true
    },
    password:{
        type:String,
        required:true
    },
    orders:[{type:mongoose.Types.ObjectId,ref:'Order',required:true}]
},{timestamps:true})

module.exports=mongoose.model('User',userSchema)