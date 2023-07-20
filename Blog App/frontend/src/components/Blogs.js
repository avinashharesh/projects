import React,{useEffect, useState} from 'react'
import axios from 'axios'
import Blog from './Blog'
import { Typography } from '@mui/material'

const Blogs = () => {
  
  const [blogs,setBlogs]=useState()
  const sendRequest=async()=>{
    const res=await axios.get('http://localhost:5000/api/blogs').catch(err=>console.log(err))
    const data=await res.data
    return data
  }
  useEffect(()=>{
    sendRequest().then((data)=>{
      setBlogs(data)
    })
  },[])
  console.log(blogs)
  return (
    <div>
      {blogs && blogs.map((blog,index)=>(
        <Blog key={index} id={blog._id} isUser={localStorage.getItem('userId')===blog.user._id} title={blog.title} description={blog.description} imageURL={blog.image} userName={blog.user.name} date={blog.createdAt}/>
      ))}
      {!blogs && setInterval(()=>(<Typography className='noBlogs' variant='h2'>No Blogs</Typography>),3000)}
    </div>
  )
}

export default Blogs