import React from 'react'
import { Box, Typography} from '@mui/material'
import { useEffect,useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

const BlogPage = () => {
  const id=useParams().id
  const [blog,setBlog]=useState()
  const [inputs,setInputs]=useState({title:'',imageURL:'',text:''})
  const fetchDetails=async()=>{
    const res=await axios.get(`http://localhost:5000/api/blogs/${id}`).catch(err=>console.log(err))
    const data=await res.data
    return data
  }
  useEffect(()=>{
    fetchDetails().then(data=>{
      setBlog(data)
      setInputs({title:data.title,imageURL:data.image,text:data.text})
    })
  },[id])
  console.log(blog)
  return (
    <div>
      <Box border={3} borderColor='linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(1,1,111,1) 35%, rgba(0,212,255,1) 100%)' borderRadius={10} boxShadow='10px 10px 20px #ccc' padding={3} margin={'auto'} marginTop={3} display='flex' flexDirection={'column'} width={'80%'}>
          <Typography fontWeight={'bold'} padding={3} color='grey' variant='h2' textAlign={'center'}>{inputs.title}</Typography>
          <img className='blogImage' src={inputs.imageURL} alt='Paella dish' />
          <p className='blogPage'>{inputs.text}</p>
      </Box>
    </div>
  )
}

export default BlogPage