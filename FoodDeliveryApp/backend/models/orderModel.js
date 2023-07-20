const mongoose=require('mongoose')

const Schema=mongoose.Schema

const orderSchema=new Schema({
    user:{
        type:mongoose.Types.ObjectId,
        ref:'User',
        required:true
    },
    order_data:{
        type:Array,
        required:true
    }
},{timestamps:true})

module.exports=mongoose.model('Order',orderSchema)