import Header from "./components/Header";
import React, { useEffect } from "react";
import { Route,Routes } from "react-router-dom";
import Blogs from './components/Blogs'
import UserBlogs from './components/UserBlogs'
import BlogDetail from './components/BlogDetail'
import AddBlog from './components/AddBlog'
import BlogPage from "./components/BlogPage";
import Auth from './components/Auth'
import { useDispatch, useSelector } from "react-redux";
import { authActions } from "./store";


function App() {
  const isLoggedIn=useSelector(state=>state.isLoggedIn)
  console.log(isLoggedIn)
  const dispatch=useDispatch()
  useEffect(()=>{
    if(localStorage.getItem('userId')){
      dispatch(authActions.login())
    }
  },[dispatch])
  return (
    <React.Fragment>
      <header>
        <Header />
      </header>
      <main>
          <Routes>
          {isLoggedIn?
          (
          <>
          <Route path="/blogs" element={<Blogs />}  />
          <Route path="/blogs/:id" element={<BlogPage />} />
          <Route path="/blogs/add" element={<AddBlog />} />
          <Route path="/myBlogs" element={<UserBlogs />} />
          <Route path="/myBlogs/:id" element={<BlogDetail />} />
          </>
          ):
          (<><Route path="/auth" element={<Auth />} />
             <Route path='/' element={<Blogs />} />
             <Route path="/blogs/:id" element={<BlogPage />} />
              </>
          )}
          </Routes>
      </main>
    </React.Fragment>
  );
}

export default App;
