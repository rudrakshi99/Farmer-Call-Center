import PreHeader from "../../components/preheader/preheader";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/footer";
import React, { useState } from "react";

const Crop = () => {
  const [load, setLoad] = useState(false);
  const [nitrogen, setNitrogen] = useState("");
  const [phosphorus, setPhosphorus] = useState("");
  const [potassium, setPotassium] = useState("");
  const [ph, setPh] = useState("");
  const [rain, setRain] = useState("");
  const [city, setCity] = useState("");
  const [prediction, setPrediction] = useState("");
  const [lang, setLang] = useState("en");

  function onSearchSubmit(term) {
    setLoad(true);
    console.log("Clicked");
    let url = "http://127.0.0.1:5000/crop-recommedation";
    let body = JSON.stringify({
      nitrogen: parseFloat(nitrogen),
      phosphorous: parseFloat(phosphorus),
      pottasium: parseFloat(potassium),
      ph: parseFloat(ph),
      rainfall: parseFloat(rain),
      city: city,
      lang: lang
    });
    console.log("body", body);
    try {
      fetch(url, {
        method: "post",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          "Access-Control-Allow-Origin": "*"
        },
        body: body
      })
        .then((response) => response.json())
        .then((data) => {
          let main_data = data["data"];
          setPrediction(main_data["prediction"]);
          console.log("res", data); // gives SyntaxError: Unexpected end of input
        })
        .catch((error) => {
          console.log(error);
        });
    } catch (e) {
      console.log(e);
    }

    setLoad(false);
  }

  return (
    <>
      <PreHeader />
      <Header />
      <section className="">
        <div className="grid place-items-center my-14  ">
          <div className="container bg-gray-100 p-10 grid place-items-center mt-14  ">
            <p className="text-2xl font-medium text-green-600 my-12">
              Predict the best crop to plant
              <br />
            </p>
            <div className="flex flex-row space-x-3 my-10">
              <div>Please select a Language, default language is English</div>
              <div className="ml-16 ">
                <button
                  onClick={() => setLang("en")}
                  type="button"
                  className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                >
                  English
                </button>
              </div>
              <div className="ml-16">
                <button
                  onClick={() => setLang("hi")}
                  type="button"
                  className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                >
                  Hindi
                </button>
              </div>
              <div className="ml-16 ">
                <button
                  onClick={() => setLang("es")}
                  type="button"
                  className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                >
                  Spanish
                </button>
              </div>
            </div>
            <input
              onChange={(e) => {
                setNitrogen(e.target.value);
              }}
              className="w-3/5 my-2 required"
              type="text"
              placeholder="Enter the value of nitrogen"
            />
            <input
              onChange={(e) => {
                setPhosphorus(e.target.value);
              }}
              className="w-3/5 my-2 required"
              type="text"
              placeholder="Enter the value of Phosphorus"
            />
            <input
              onChange={(e) => {
                setPotassium(e.target.value);
              }}
              className="w-3/5 my-2 required"
              type="text"
              placeholder="Enter the value of Potassium"
            />
            <input
              onChange={(e) => {
                setPh(e.target.value);
              }}
              className="w-3/5 my-2 required"
              type="text"
              placeholder="Enter the soil ph value (0-14)"
            />
            <input
              onChange={(e) => {
                setRain(e.target.value);
              }}
              className="w-3/5 my-2 required"
              type="text"
              placeholder="Enter the rainfall gauge (in mm)"
            />
            <input
              onChange={(e) => {
                setCity(e.target.value);
              }}
              className="w-3/5 my-2 required"
              type="text"
              placeholder="Enter your city"
            />

            <div className="grid place-items-center mt-14 ">
              <div className="mt-2">
                <button
                  onClick={() => {
                    onSearchSubmit();
                  }}
                  type="button"
                  className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                >
                  Get Crop Recommendation
                </button>
              </div>
            </div>
          </div>
        </div>

        <div>
          {load ? (
            <div className="grid place-items-center my-14  ">loading </div>
          ) : (
            <div></div>
          )}
          {prediction !== "" ? (
            <div className="grid place-items-center my-14 text-center ">
              <p className="font-bold my-3">Crop Predicted: </p>
              {prediction}
            </div>
          ) : (
            <div></div>
          )}
        </div>
      </section>
      <Footer />
    </>
  );
};

export default Crop;
