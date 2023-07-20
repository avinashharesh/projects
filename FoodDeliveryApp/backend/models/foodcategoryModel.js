const mongoose=require('mongoose')

const Schema=mongoose.Schema
const foodcategorySchema=new Schema(
    {
        CategoryName:{
            type:String,
            required:true
        }
    },{timestamps:true}

)

module.exports=mongoose.model('FoodCategory',foodcategorySchema)