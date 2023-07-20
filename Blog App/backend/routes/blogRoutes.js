const express=require('express')
const {getblogs,addblog,updateblog,getblog,deleteblog,getByUserId}=require('../controllers/blogController')

const router=express.Router()

//GET all blogs
router.get('/',getblogs)

//CREATE a blog
router.post('/add',addblog)

//UPDATE a blog
router.patch('/update/:id',updateblog)

//GET a blog
router.get('/:id',getblog)

//DELETE a blog
router.delete('/delete/:id',deleteblog)

//GET all blogs by userid
router.get('/user/:id',getByUserId)


module.exports=router