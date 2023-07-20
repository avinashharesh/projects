const express=require('express')
const {getUsers,signup,login,getOrders}=require('../controllers/userController')

const router=express.Router()

//GET all users
router.get('/',getUsers)

//POST a user
router.post('/signup',signup)

//LOGIN a user
router.post('/login',login)

//GET orders
router.get('/orders/:id',getOrders)

module.exports=router