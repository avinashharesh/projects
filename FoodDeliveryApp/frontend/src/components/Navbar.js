import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { useSelector } from 'react-redux';
import { authActions } from "../store";
import { useNavigate } from "react-router-dom";
import { useCart } from "./ContextReducer";
import Badge from 'react-bootstrap/Badge'
import Modal from "../Modal";
import Cart from "../pages/Cart";
const Navbar = () => {
  let data=useCart()
  const [cartView,setCartView]=useState(false)
  const navigate=useNavigate()
  const dispatch = useDispatch();
  const isLoggedIn = useSelector((state) => state.isLoggedIn);
  const handleLogout = () => {
    dispatch(authActions.logout())
    localStorage.removeItem('userId')
    navigate("/")
  };
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-success">
        <div className="container-fluid">
          <Link className="navbar-brand fs-1 fst-italic fw-bold" to="/">
            GoFood
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav me-auto mb-2">
              <li className="nav-item">
                <Link className="nav-link" aria-current="page" to="/">
                  Home
                </Link>
              </li>
              {isLoggedIn && (
                <li className="nav-item">
                  <Link className="nav-link" aria-current="page" to="/myorders">
                    My Orders
                  </Link>
                </li>
              )}
            </ul>
            {isLoggedIn ? (
              <div className="d-flex">
                <Link className="btn bg-white text-success mx-2"  onClick={()=>{setCartView(true)}}>
                  My Cart {" "}
                  <Badge pill bg="danger"> {data.length} </Badge>
                </Link>
                {cartView && <Modal onClose={()=>setCartView(false)}><Cart /></Modal>}
                <Link
                  className="btn bg-white text-danger mx-2"
                  onClick={handleLogout}
                  to="/login"
                >
                  Logout
                </Link>
              </div>
            ) : (
              <div className="d-flex">
                <Link className="btn bg-white text-success mx-1" to="/login">
                  Login
                </Link>
                <Link className="btn bg-white text-success mx-1" to="/signup">
                  Signup
                </Link>
              </div>
            )}
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
