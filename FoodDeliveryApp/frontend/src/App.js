import './App.css';
import React from 'react';
import Home from './pages/Home';
import Login from './pages/Login';
import Signup from './pages/Signup';
import {Routes,Route} from 'react-router-dom'
import Navbar from './components/Navbar';
import { CartProvider } from './components/ContextReducer';
import MyOrder from './pages/MyOrder';
import { useSelector } from 'react-redux';

function App() {
  const isLoggedIn = useSelector((state) => state.isLoggedIn);
  return (
  <CartProvider>
  <React.Fragment>
    <header>
      <Navbar />
    </header>
    <main>
      <Routes>
        <Route exact path='/' element={<Home />} />
        <Route exact path='/login' element={<Login />} />
        <Route exact path='/signup' element={<Signup />} />
        {isLoggedIn && <Route exact path='/myorders' element={<MyOrder />} />}
      </Routes>
    </main>
  </React.Fragment>
  </CartProvider>
  );
}

export default App;
