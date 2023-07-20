import { Box, InputLabel, TextField, Typography, Button } from '@mui/material'
import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const labelStyles={mb:1,mt:2,fontSize:'24px',fontWeight:'bold'}
const AddBlog = () => {
  const navigate=useNavigate()
  const [inputs,setInputs]=useState({
    title:"",
    description:"",
    imageURL:"",
    text:""
  })

  const handleChange=(e)=>{
    setInputs((prevState)=>({
      ...prevState,
      [e.target.name]:e.target.value
    }))
  }

  const sendRequest=async()=>{
    const res=await axios.post('http://localhost:5000/api/blogs/add',{
      title:inputs.title,
      description:inputs.description,
      image:inputs.imageURL,
      user:localStorage.getItem('userId'),
      text:inputs.text
    }).catch(err=>console.log(err))
    const data=await res.data
    return data

  }
  
  const handleSubmit=(e)=>{
    e.preventDefault()
    console.log(inputs)
    sendRequest().then(()=>navigate('/blogs')).then((data)=>console.log(data))
  }
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <Box border={3} borderColor='linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(1,1,111,1) 35%, rgba(0,212,255,1) 100%)' borderRadius={10} boxShadow='10px 10px 20px #ccc' padding={3} margin={'auto'} marginTop={3} display='flex' flexDirection={'column'} width={'80%'}>
          <Typography fontWeight={'bold'} padding={3} color='grey' variant='h2' textAlign={'center'}>Post Your Blog</Typography>
          <TextField name='title' label='Title' value={inputs.title} onChange={handleChange} margin='normal' variant='outlined' />
          <TextField name='description' label='Description' value={inputs.description} onChange={handleChange} margin='normal' variant='outlined' />
          <TextField name='imageURL' label='ImageURL' value={inputs.imageURL} onChange={handleChange} margin='normal' variant='outlined' />
          <TextField name='text' label='You Can Type Here' multiline rows={10} value={inputs.text} onChange={handleChange} variant="standard"/>
          <Button type='submit' sx={{mt:2,borderRadius:4}} variant='contained' color='warning'>Submit</Button>
        </Box>
      </form>
    </div>
  )
}

export default AddBlog