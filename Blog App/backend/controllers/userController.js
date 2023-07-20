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
    const {name,email,password}=req.body
    let emptyFields=[]
    if(!name)
        emptyFields.push('Name')
    if(!email)
        emptyFields.push('Email')
    if(!password)
        emptyFields.push('Password')
    if(emptyFields.length>0)
        return res.status(400).json({error:"Please fill in the required fields",emptyFields})
    let existingUser

    try{
        existingUser=await User.findOne({email})
    } 

    catch(error)
    {
        res.status(400).json({error: error.message})
    }

    if(existingUser)
        {
            emptyFields.push('User Already Exists')
            return res.status(400).json({error:"User Already Exists! Login Instead",emptyFields})
        }

    hashedPassword=bcrypt.hashSync(password)
    const user=new User({name,email,password:hashedPassword,blogs:[]})
    
    try{
        await user.save()
        res.status(201).json({user:user})
    } catch(error){
        res.status(400).json({error: error.message})
    }
}

//login a user
const login=async(req,res)=>{
    const {email,password}=req.body
    let emptyFields=[]
    if(!email)
        emptyFields.push('Email')
    if(!password)
        emptyFields.push('Passsword')
    if(emptyFields.length>0)
        return res.status(400).json({error:"Please fill in the required fields",emptyFields})
    let existingUser
    try{
        existingUser=await User.findOne({email})

    }catch(error){
        return res.status(400).json({error:error.message})
    }
    if(!existingUser)
    {
        emptyFields.push('User with this ID not found')
        return res.status(404).json({error:'User with this ID not found',emptyFields})
    }
    const isPasswordCorrect=bcrypt.compareSync(password,existingUser.password)
    if(!isPasswordCorrect)
        {
            emptyFields.push('Incorrect Password')
            return res.status(400).json({error:'Password Incorrect',emptyFields})
        }
    res.status(200).json({message:"Login Successful",user:existingUser})
}

module.exports={getUsers,signup,login}