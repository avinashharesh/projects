const Blog=require('../models/blogModel')
const mongoose=require('mongoose')
const User=require('../models/userModel')

//get all blogs
const getblogs=async(req,res)=>{
    const blogs=await Blog.find({}).sort({createdAt:-1}).populate('user')
    res.status(200).json(blogs)

}

//create a blog
const addblog=async(req,res)=>{
    const {title,description,image,user,text}=req.body
    let existingUser
    existingUser=await User.findById(user)
    if(!existingUser)
        return res.status(404).json({error:"User not found"})
  
    const blog=new Blog({title,description,image,user,text})

    try{
        const session=await mongoose.startSession()
        session.startTransaction()
        await blog.save({session})
        existingUser.blogs.push(blog)
        await existingUser.save({session})
        await session.commitTransaction()
    }catch(error){
        res.status(400).json({error:error.message})
    }

    res.status(200).json(blog)
}

//update a blog
const updateblog=async(req,res)=>{
    const {id} =req.params
    if(!mongoose.Types.ObjectId.isValid(id))
        return res.status(404).json({error:"Blog Not Found"})
    const blog=await Blog.findByIdAndUpdate({_id:id},{...req.body})
    if(!blog)
        return res.status(404).json({error:"Blog Not Found"})
    res.status(200).json(blog)

}

//get blog by id
const getblog=async(req,res)=>{
    const {id}=req.params
    if(!mongoose.Types.ObjectId.isValid(id))
        return res.status(404).json({error:'Blog Not Found'})
    const blog=await Blog.findById(id)
    if(!blog)
        return res.status(404).json({error:'Blog Not Found'})
    res.status(200).json(blog)
}

//delete a blog
const deleteblog=async(req,res)=>{
    const {id}=req.params
    if(!mongoose.Types.ObjectId.isValid(id))
        return res.status(404).json({error:'Blog Not Found'})
    const blog=await Blog.findByIdAndDelete({_id:id}).populate('user')
    await blog.user.blogs.pull(blog)
    await blog.user.save()
    if(!blog)
        return res.status(404).json({error:'Blog Not Found'})
    res.status(200).json(blog)
}

//get blogs by userid
const getByUserId=async(req,res)=>{
    const {id}=req.params
    if(!mongoose.Types.ObjectId.isValid(id))
        return res.status(404).json({error:'User Not Found'})
    const user=await User.findById(id)
    const userBlogs=await User.findById(id).populate('blogs')
    if(!userBlogs)
        return res.status(404).json({error:"No Blogs Found"})
    res.status(200).json({blogs:userBlogs.blogs,user:user})

}

module.exports={getblogs,addblog,updateblog,getblog,deleteblog,getByUserId}