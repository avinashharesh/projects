const express=require('express')
const {getFoodItems}=require('../controllers/fooditemController')

const router=express.Router()

//GET all food items
router.get('/',getFoodItems)

module.exports=router