const express=require('express')
const {getUsers,signup,login}=require('../controllers/userController')

const router=express.Router()

//GET all users
router.get('/',getUsers)

//CREATE a user
router.post('/signup',signup)

//LOGIN a user
router.post('/login',login)


module.exports=router