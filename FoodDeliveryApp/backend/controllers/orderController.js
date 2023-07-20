const Order=require('../models/orderModel')
const User=require('../models/userModel')
const mongoose=require('mongoose')

//get all orders
const getOrders=async(req,res)=>{
    const orders=await Order.find({}).sort({createdAt:-1})
    res.status(200).json(orders)
}

//post a order
const postOrder=async(req,res)=>{
    const {user,order_data}=req.body
    let existingUser
    existingUser=await User.findById(user)
    if(!existingUser)
        return res.status(404).json({error:'User not found'})
    const order=new Order({user,order_data})
    try{
        const session=await mongoose.startSession()
        session.startTransaction()
        await order.save({session})
        existingUser.orders.push(order)
        await existingUser.save({session})
        await session.commitTransaction()
    }catch(error){
        res.status(400).json({error:error.message})
    }

    res.status(200).json(order)
}

module.exports={getOrders,postOrder}