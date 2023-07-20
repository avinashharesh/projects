const User=require('../models/userModel')
const mongoose=require('mongoose')
const bcrypt=require('bcryptjs')


//get all users
const getUsers=async(req,res)=>{
    const users=await User.find({}).sort({createdAt:-1})
    res.status(200).json(users)
}

//create a user
const signup=async(req,res)=>{
    const {name,email,password,location}=req.body
    let emptyFields=[]
    if(!name)
        emptyFields.push('name')
    if(!email)
        emptyFields.push('email')
    if(!password)
        emptyFields.push('password')
    if(!location)
        emptyFields.push('location')
    if(emptyFields.length>0)
        return res.status(400).json({error:"Please fill in the required fields",emptyFields})
    let existingUser
    try{
        existingUser=await User.findOne({email})
    }
    catch(error)
    {
        res.status(400).json({error:error.message,emptyFields})
    }

    if(existingUser)
        return res.status(400).json({error:'User already exists',emptyFields})
    hashedPassword=bcrypt.hashSync(password)
    const user=new User({name,email,password:hashedPassword,location,orders:[]})
    try{
        await user.save()
        res.status(201).json({user:user})
    }catch(error){
        res.status(400).json({error:error.message,emptyFields})
    }
}

//login a user
const login=async(req,res)=>{
    const {email,password}=req.body
    let emptyFields=[]
    if(!email)
        emptyFields.push('email')
    if(!password)
        emptyFields.push('password')
    if(emptyFields.length>0)
        return res.status(400).json({error:'Please fill in the required fields',emptyFields})
    let existingUser
    try{
        existingUser=await User.findOne({email})
    }
    catch(error){
        return res.status(400).json({error:error.message,emptyFields})
    }
    if(!existingUser)
        return res.status(400).json({error:'User does not exists',emptyFields})
    const isPasswordCorrect=bcrypt.compareSync(password,existingUser.password)
    if(!isPasswordCorrect)
        return res.status(400).json({error:'Incorrect Password',emptyFields})
    res.status(200).json({user:existingUser})
}

//get orders
const getOrders=async(req,res)=>{
    const {id}=req.params
    if(!mongoose.Types.ObjectId.isValid(id))
        return res.status(404).json({error:'User Not Found'})
    const user=await User.findById(id).populate('orders')
    if(!user)
         return res.status(404).json({error:'User Not Found'})
    res.status(200).json(user.orders)
}

module.exports={getUsers,signup,login,getOrders}