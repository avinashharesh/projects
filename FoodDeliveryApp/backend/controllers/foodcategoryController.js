const FoodCategory=require('../models/foodcategoryModel')
const mongoose=require('mongoose')

//get all food categories
const getFoodCategories=async(req,res)=>{
    const foodcategories=await FoodCategory.find({}).sort({createdAt:-1})
    res.status(200).json(foodcategories)
}

module.exports={getFoodCategories}