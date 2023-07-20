const express=require('express')
const {getOrders,postOrder}=require('../controllers/orderController')

const router=express()

//GET all orders
router.get('/',getOrders)

//POST a order
router.post('/createOrder',postOrder)

module.exports=router