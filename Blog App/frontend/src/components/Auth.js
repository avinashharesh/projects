import { TextField, Typography,Box,Button,Alert,Stack } from '@mui/material'
import React, { useState } from 'react'
import {useDispatch} from 'react-redux'
import { authActions } from '../store'
import { useNavigate } from 'react-router-dom'

const Auth = () => {
  const dispatch=useDispatch()
  const navigate=useNavigate()
  const [inputs,setInputs]=useState({name:"",email:"",password:""})
  const [isSignup,setIsSignup]=useState(false)
  const [error,setError]=useState(null)
  const [emptyFields,setEmptyFields]=useState([])
  const handleChange=(e)=>{
    setInputs((prevState)=>({
      ...prevState,
      [e.target.name]:e.target.value
    }))
  }
  const handleSubmit=(e)=>{
    e.preventDefault()
    console.log(inputs)
    if(isSignup){
      signupRequest()
    }
    else
    {
      loginRequest()
      
    }
  }

  const signupRequest=async()=>{
    const user={name:inputs.name,email:inputs.email,password:inputs.password}
    const response=await fetch('http://localhost:5000/api/users/signup',{
      method:'POST',
      body:JSON.stringify(user),
      headers:{
        'Content-Type':'application/json'
      }
    })
    const json=await response.json()
    if(!response.ok)
    {
      setError(json.error)
      setEmptyFields(json.emptyFields)

    }
    if(response.ok)
    {
      localStorage.setItem('userId',json.user._id)
      dispatch(authActions.login())
      navigate('/blogs')
      console.log(json)
    }
  }

  const loginRequest=async()=>{
    const user={email:inputs.email,password:inputs.password}
    const response=await fetch('http://localhost:5000/api/users/login',{
      method:'POST',
      body:JSON.stringify(user),
      headers:{
        'Content-Type':'application/json'
      }
    })
    const json=await response.json()
    if(!response.ok)
    {
      setError(json.error)
      setEmptyFields(json.emptyFields)
    }
    if(response.ok)
    {
      localStorage.setItem('userId',json.user._id)
      dispatch(authActions.login())
      navigate('/blogs')
      console.log(json)
    }

  }
  return (
    <div>
        <form onSubmit={handleSubmit}>
            <Box maxWidth={400} display='flex' flexDirection={'column'} alignItems='center' justifyContent={'center'} boxShadow='10px 10px 20px #ccc' padding={3} margin='auto' marginTop={5} borderRadius={5}>
                <Typography variant='h2' padding={3} textAlign='center'>{!isSignup ? 'Login':'Signup'}</Typography>
                {isSignup && <TextField error={emptyFields.includes('Name')?true:false} helperText={emptyFields.includes('Name')?'Required':false} name='name' value={inputs.name} onChange={handleChange} placeholder='Name' margin='normal' />}
                <TextField error={emptyFields.includes('Email')?true:false} helperText={emptyFields.includes('Email')?'Required':false} name='email' value={inputs.email} onChange={handleChange} type='email' placeholder='Email' margin='normal' />
                <TextField error={emptyFields.includes('Password')?true:false} helperText={emptyFields.includes('Password')?'Required':false} name='password' value={inputs.password} onChange={handleChange} type='password' placeholder='Password' margin='normal' />
                <Button type='submit' variant='contained' sx={{borderRadius:3,marginTop:3}} color='lightBlue'>{!isSignup ? "Login": "Signup"}</Button>
                <Button onClick={()=>setIsSignup(!isSignup)} sx={{borderRadius:3,marginTop:3}}>Change To {!isSignup ? "Signup": "Login"}</Button>
            </Box>
            {error && <Stack sx={{paddingTop:5,width:'100%'}} spacing={2}>
              <Alert severity='error'>{error}</Alert>
              </Stack>}
        </form>
    </div>
  )
}

export default Auth