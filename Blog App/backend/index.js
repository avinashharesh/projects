require('dotenv').config()


const express=require("express")
const userRoutes=require('./routes/userRoutes')
const blogRoutes=require('./routes/blogRoutes')
const mongoose=require("mongoose")
const cors=require('cors')

//express app
const app=express()
app.use(cors())
//middleware
app.use(express.json())
app.use((req,res,next)=>{
    console.log(req.path,req.method)
    next()
})

//routes
app.use('/api/users',userRoutes)
app.use('/api/blogs',blogRoutes)

//connection to mongodb
mongoose.connect(process.env.MONG_URI).then(()=>{
    app.listen(process.env.PORT,()=>{
        console.log('Connected to DB and listening to PORT: '+process.env.PORT)
    })
})


