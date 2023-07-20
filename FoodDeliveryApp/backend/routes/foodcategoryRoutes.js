const express=require('express')
const {getFoodCategories}=require('../controllers/foodcategoryController')

const router=express.Router()

//GET all food categories
router.get('/',getFoodCategories)

module.exports=router