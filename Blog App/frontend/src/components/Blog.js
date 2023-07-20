import React from 'react'
import {Avatar,CardContent,CardMedia,Typography,CardHeader,Card, Box, IconButton} from '@mui/material'
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import OpenInNewIcon from '@mui/icons-material/OpenInNew';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import formatDistanceToNow from 'date-fns/formatDistanceToNow'

const Blog = ({id,isUser,title,description,imageURL,userName,date}) => {
  const navigate=useNavigate()
  const handleEdit=()=>{
    navigate(`/myBlogs/${id}`)
  }

  const deleteRequest=async()=>{
    const res=await axios.delete(`http://localhost:5000/api/blogs/delete/${id}`).catch(err=>console.log(err))
    const data=await res.data
    return data

  }
  const handleDelete=()=>{
    deleteRequest().then(()=>navigate('/')).then(()=>navigate('/blogs')).then((data)=>console.log(data))
  }
  const openView=()=>{
    navigate(`/blogs/${id}`)
  }
  return (
    <div>
    
    <Card sx={{ width: '40%',margin:'auto',mt:2,padding:2,boxShadow:'5px 5px 10px #ccc',':hover:':{
        boxShadow:'10px 10px 20px #ccc'
    } }}>
      {isUser ? (
        <Box display='flex'>
          <IconButton onClick={openView}><OpenInNewIcon /></IconButton>
          <IconButton sx={{marginLeft:'auto'}} onClick={handleEdit} color='warning'><EditIcon /></IconButton>
          <IconButton onClick={handleDelete} color='error'><DeleteIcon /></IconButton> 
        </Box>
      ):(
        <Box display='flex'>
          <IconButton onClick={openView}><OpenInNewIcon /></IconButton>
        </Box>
      )}
      <CardHeader
        avatar={
          <Avatar sx={{ bgcolor: 'red' }} aria-label="recipe">
            {userName.charAt(0)}
          </Avatar>
        }
       
        title={title}
        subheader={formatDistanceToNow(new Date(date),{addSuffix: true})}
      />
      <CardMedia
        component="img"
        height="194"
        image={imageURL}
        alt="Paella dish"
      />
      <CardContent>
        <hr />
        <br />
        <Typography variant="body2" color="text.secondary">
          <b>{userName}</b>{':'}{description}
        </Typography>
      </CardContent>

    </Card>
    </div>
  )
}

export default Blog