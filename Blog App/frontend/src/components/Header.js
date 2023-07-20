import React, { useState } from 'react'
import {AppBar, Toolbar, Typography,Box,Button, Tabs,Tab} from '@mui/material'
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import { authActions } from '../store';
const Header = () => {
  const dispatch=useDispatch()
  const [value,setValue]=useState()
  const isLoggedIn=useSelector((state)=>state.isLoggedIn)
  return (
    <AppBar position="sticky" sx={{background:"linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(1,1,111,1) 35%, rgba(0,212,255,1) 100%)"}}>
      <Toolbar>
        <Typography LinkComponent={Link} to='/' variant="h4">BlogApp</Typography>
       { isLoggedIn && <Box display="flex" marginLeft="auto" marginRight="auto" >
          <Tabs textColor="inherit" value={value} onChange={(e,val)=>setValue(val)}>
            <Tab LinkComponent={Link} to="/blogs" label="All Blogs" />
            <Tab LinkComponent={Link} to="/myBlogs" label="My Blogs" />
            <Tab LinkComponent={Link} to="/blogs/add" label="Add Blog" />
          </Tabs>
        </Box>}
        <Box display="flex" marginLeft='auto'>
        { !isLoggedIn && <> <Button LinkComponent={Link} to="/" variant='contained' sx={{margin:1,borderRadius:10}} color="warning">Home</Button>
          <Button LinkComponent={Link} to="/auth" variant='contained' sx={{margin:1,borderRadius:10}} color="warning">Login/Signup</Button> </>}
          {isLoggedIn && 
          <Button LinkComponent={Link} to="/auth" variant='contained' sx={{margin:1,borderRadius:10}} color="warning" onClick={()=>dispatch(authActions.logout())}>Logout</Button>
          }
        </Box>
      </Toolbar>
    </AppBar>
  )
}

export default Header