import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { authActions } from "../store";
import { useDispatch } from "react-redux";

const Login = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [inputs, setInputs] = useState({ email: "", password: "" });
  const [error, setError] = useState(null);
  const [emptyFields, setEmptyFields] = useState([]);
  const handleChange = (e) => {
    setInputs((prevState) => ({
      ...prevState,
      [e.target.name]: e.target.value,
    }));
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    const user = {
      email: inputs.email,
      password: inputs.password,
    };
    const response = await fetch("http://localhost:5000/api/users/login", {
      method: "POST",
      body: JSON.stringify(user),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const json = await response.json();
    if (!response.ok) {
      setError(json.error);
      setEmptyFields(json.emptyFields);
    }
    if (response.ok) {
      console.log(json);
      dispatch(authActions.login());
      localStorage.setItem('userId',json.user._id)
      navigate("/");
    }
  };
  return (
    <>
      <form onSubmit={handleSubmit}>
        <div className="container" style={{ marginTop: "10px" }}>
          <div className="mb-3">
            <label for="exampleInputEmail1" className="form-label">
              Email address
            </label>
            <input
              type="email"
              className={
                emptyFields.includes("email")
                  ? "form-control is-invalid"
                  : "form-control"
              }
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              name="email"
              value={inputs.email}
              onChange={handleChange}
            />
          </div>
          <div className="mb-3">
            <label for="exampleInputPassword1" className="form-label">
              Password
            </label>
            <input
              type="password"
              className={
                emptyFields.includes("password")
                  ? "form-control is-invalid"
                  : "form-control"
              }
              id="exampleInputPassword1"
              name="password"
              value={inputs.password}
              onChange={handleChange}
            />
          </div>
          <button type="submit" className="btn btn-success">
            Login
          </button>
          {error && (
            <div className="alert alert-danger" role="alert" id="errorTag">
              {error}
            </div>
          )}
        </div>
      </form>
    </>
  );
};

export default Login;
