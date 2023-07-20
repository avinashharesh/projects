const FoodItem=require('../models/fooditemModel')
const mongoose=require('mongoose')

//get all fooditems
const getFoodItems=async(req,res)=>{
    const fooditems=await FoodItem.find({}).sort({createdAt:-1})
    res.status(200).json(fooditems)
}

module.exports={getFoodItems}