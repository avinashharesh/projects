import React from "react";
import { useState, useEffect } from "react";


const MyOrder = () => {
  const [orderData, setOrderData] = useState(null);
  const getOrders = async () => {
    const userId = localStorage.getItem("userId");
    const response = await fetch(
      `http://localhost:5000/api/users/orders/${userId}`
    );
    const json = await response.json();
    if (response.ok) {
      setOrderData(json);
      console.log(json);
    }
  };
  useEffect(() => {
    getOrders();
  }, []);
  if (!orderData || orderData.length===0)
    return (
      <div>
        <div className="m-5 w-100 text-center fs-3">The Cart is Empty!</div>
      </div>
    );
  return (
    <div className="container m-auto mt-5 table-responsive  table-responsive-sm table-responsive-md">
      <table className="table table-hover ">
        <thead className=" text-success fs-4">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Quantity</th>
            <th scope="col">Option</th>
            <th scope="col">Amount</th>
            <th scope="col">Date</th>
          </tr>
        </thead>
        <tbody>
            {orderData.map((order)=>{
                let orderDetails=order.order_data
                return(
                    orderDetails.map((data,index)=>(
                        <tr>
                        <th scope="row">{index + 1}</th>
                        <td>{data.name}</td>
                        <td>{data.qty}</td>
                        <td>{data.size}</td>
                        <td>{data.price}</td>
                        <td>{order.createdAt}</td>
                        </tr>
                        
                    ))
                )
            })}
        </tbody>
      </table>
    </div>
  );
};

export default MyOrder;
