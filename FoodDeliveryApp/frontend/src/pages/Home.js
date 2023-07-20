import React from "react";
import Footer from "../components/Footer";
import Card from "../components/Card";
import { useEffect, useState } from "react";

const Home = () => {
  const [search, setSearch] = useState("");
  const [fooditems, setFooditems] = useState(null);
  const [foodcategories, setFoodcategories] = useState(null);
  const getFoodItems = async () => {
    const response = await fetch("http://localhost:5000/api/fooditems");
    const json = await response.json();
    if (response.ok) setFooditems(json);
  };
  const getFoodCatories = async () => {
    const response = await fetch("http://localhost:5000/api/foodcategories");
    const json = await response.json();
    if (response.ok) setFoodcategories(json);
  };
  useEffect(() => {
    getFoodCatories();
    getFoodItems();
  }, []);
  return (
    <div>
      <div
        id="carouselExampleFade"
        className="carousel slide carousel-fade"
        data-bs-ride="carousel"
        style={{ objectFit: "fill" }}
      >
        <div className="carousel-inner" id="carousel">
          <div className="carousel-caption" style={{ zIndex: "10" }}>
            <div className="d-flex justify-content-center">
              <input
                className="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
                value={search}
                onChange={(e) => {
                  setSearch(e.target.value);
                }}
              />
            </div>
          </div>
          <div className="carousel-item active">
            <img
              src="https://source.unsplash.com/random/300×700/?burger"
              className="d-block w-100"
              alt="..."
              style={{
                filter: "brightness(30%)",
                maxHeight: "500px",
                objectFit: "cover",
              }}
            />
          </div>
          <div className="carousel-item">
            <img
              src="https://source.unsplash.com/random/900×700/?pastry"
              className="d-block w-100"
              alt="..."
              style={{
                filter: "brightness(30%)",
                maxHeight: "500px",
                objectFit: "cover",
              }}
            />
          </div>
          <div className="carousel-item">
            <img
              src="https://source.unsplash.com/random/900×700/?barbeque"
              className="d-block w-100"
              alt="..."
              style={{
                filter: "brightness(30%)",
                maxHeight: "500px",
                objectFit: "cover",
              }}
            />
          </div>
        </div>
        <button
          className="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleFade"
          data-bs-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          className="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleFade"
          data-bs-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
      {foodcategories ? (
        foodcategories.map((foodCategory) => {
          return (
            <div className="fs-3 m-3">
              <div style={{ marginTop: "40px" }}>
                {foodCategory.CategoryName}
              </div>
              <div key={foodCategory._id} className="row mb-3">
                {fooditems ? (
                  fooditems
                    .filter(
                      (foodItem) =>
                        foodItem.CategoryName === foodCategory.CategoryName &&
                        foodItem.name.toLowerCase().includes(search.toLowerCase())
                    )
                    .map((filterItem) => {
                      return (
                        <div
                          key={filterItem._id}
                          className="col-12 col-md-6 col-lg-3"
                        >
                          <Card
                            foodItem={filterItem}
                            options={filterItem.options[0]}
                          />
                        </div>
                      );
                    })
                ) : (
                  <div>No Data</div>
                )}
              </div>
            </div>
          );
        })
      ) : (
        <div>No Data</div>
      )}
      <div className="m-3"></div>
      <div>
        <Footer />
      </div>
    </div>
  );
};

export default Home;
