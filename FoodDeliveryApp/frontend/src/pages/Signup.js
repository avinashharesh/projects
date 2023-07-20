import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { authActions } from "../store";
import { useDispatch } from "react-redux";

const Signup = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [inputs, setInputs] = useState({
    name: "",
    email: "",
    password: "",
    location: "",
  });
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
      name: inputs.name,
      email: inputs.email,
      password: inputs.password,
      location: inputs.location,
    };
    const response = await fetch("http://localhost:5000/api/users/signup", {
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
            <label for="name" className="form-label">
              Name
            </label>
            <input
              type="text"
              name="name"
              className={
                emptyFields.includes("name")
                  ? "form-control is-invalid"
                  : "form-control"
              }
              value={inputs.name}
              onChange={handleChange}
            />
          </div>
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
            <div id="emailHelp" className="form-text">
              We'll never share your email with anyone else.
            </div>
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
          <div className="mb-3">
            <label for="location" className="form-label">
              Address
            </label>
            <input
              type="text"
              className={
                emptyFields.includes("location")
                  ? "form-control is-invalid"
                  : "form-control"
              }
              name="location"
              value={inputs.location}
              onChange={handleChange}
            />
          </div>
          <button type="submit" className="btn btn-success">
            Signup
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

export default Signup;
