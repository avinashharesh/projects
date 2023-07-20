import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Blog from './Blog'
import { Typography } from '@mui/material'
const UserBlogs = () => {
  const [blogs,setBlogs]=useState()
  const [user,setUser]=useState()
  const id=localStorage.getItem('userId')
  const sendRequest=async()=>{
    const res=await axios.get(`http://localhost:5000/api/blogs/user/${id}`).catch(err=>console.log(err))
    const data=await res.data 
    return data
  }
  useEffect(()=>{
    sendRequest().then((data)=>{
      setBlogs(data.blogs)
      setUser(data.user)
    })
  },[])
  console.log(blogs)
  console.log(user)
  return (
    <div>
      {blogs && blogs.map((blog,index)=>(
        <Blog key={index} id={blog._id} isUser={true} title={blog.title} description={blog.description} imageURL={blog.image} userName={user.name} date={blog.createdAt}/>
      ))}
      {!blogs && setInterval(()=>(<Typography className='noBlogs' variant='h2'>No Blogs</Typography>),3000)}
    </div>
  )
}

export default UserBlogs