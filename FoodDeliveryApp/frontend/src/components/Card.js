import React, { useRef, useState } from "react";
import { useDispatchCart, useCart } from "./ContextReducer";
import { useEffect } from "react";

const Card = ({ foodItem, options }) => {
  let priceOptions = Object.keys(options);
  let dispatch = useDispatchCart();
  let data = useCart();
  const priceRef = useRef();
  const [qty, setQty] = useState(1);
  const [size, setSize] = useState("");
  const name = foodItem.name;
  const description = foodItem.description;
  const image = foodItem.img;
  const handleAddToCart = async () => {
    let food = [];
    for (const item of data) {
      if (item.id === foodItem._id) {
        food = item;
        break;
      }
    }
    if (food !== []) {
      if (food.size === size) {
        await dispatch({
          type: "UPDATE",
          id: foodItem._id,
          price: finalPrice,
          qty: qty,
        });
        return;
      } else if(food.size!==size) {
        await dispatch({
          type: "ADD",
          id: foodItem._id,
          name: foodItem.name,
          price: finalPrice,
          qty: qty,
          size: size,
        });
        return
      }
      return
    }
    await dispatch({
      type: "ADD",
      id: foodItem._id,
      name: foodItem.name,
      price: finalPrice,
      qty: qty,
      size: size,
    });
    console.log(data);
  };
  let finalPrice = qty * parseInt(options[size]);
  useEffect(() => {
    setSize(priceRef.current.value);
  }, []);
  return (
    <div className="card mt-3" style={{ width: "18rem" }}>
      <img
        style={{ height: "200px", width: "285px", objectFit: "fill" }}
        src={image}
        className="card-img-top"
        alt="..."
      />
      <div className="card-body">
        <h5 className="card-title">{name}</h5>
        <p className="card-text">{description}</p>
        <div className="container w-100">
          <select
            className="m-2 h-100 bg-success rounded"
            onChange={(e) => setQty(e.target.value)}
          >
            {Array.from(Array(6), (e, i) => {
              return (
                <option key={i + 1} value={i + 1}>
                  {i + 1}
                </option>
              );
            })}
          </select>
          <select
            className="m-2 h-100 bg-success rounded"
            ref={priceRef}
            onChange={(e) => setSize(e.target.value)}
          >
            {priceOptions.map((option) => {
              return (
                <option key={option} value={option}>
                  {option}
                </option>
              );
            })}
          </select>
          <hr></hr>
          <div className="h-100 fs-5">${finalPrice}</div>
          <hr></hr>
          <button
            className={"btn btn-success justify-center ms-2"}
            onClick={handleAddToCart}
          >
            Add To Cart
          </button>
        </div>
      </div>
    </div>
  );
};

export default Card;
