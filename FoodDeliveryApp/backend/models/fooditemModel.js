const mongoose=require('mongoose')

const Schema=mongoose.Schema

const fooditemSchema=new Schema({
    name:{
        type:String,
        required:true
    },
    CategoryName:{
        type:String,
        required:true
    },
    img:{
        type:String,
        required:true
    },
    options:{
        type:Array,
        required:true
    },
    description:{
        type:String,
        required:true
    }
},{timestamps:true})

module.exports=mongoose.model('FoodItem',fooditemSchema)