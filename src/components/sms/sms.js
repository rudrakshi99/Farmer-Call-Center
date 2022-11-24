import PreHeader from "../preheader/preheader";
import Header from "../Header/Header";
import Footer from "../Footer/footer";
import React, { useState } from "react";
import axios from "axios";

const SmsService = () => {
  const [number, setNumber] = useState("")
  const [log, setLog] = useState("")
  const [load, setLoad] = useState(true)
  async function onSearchSubmit(term) {
    setLoad(false)
    console.log("Clicked");
    let url = "http://127.0.0.1:5000/find_response/+919756611688/"+log

    let value = await fetch(url, {
      method: "get",
    })

    setLoad(false)
    console.log(value)
  }

  return (
    <>
      <PreHeader />
      <Header />
      <section className="">
        <div className="grid place-items-center my-14  ">
          <div className="container bg-gray-100 p-10 grid place-items-center mt-14  ">
            <p className="text-2xl font-medium text-green-600 my-12">Get your solution via SMS<br /></p>

            <input onChange={
              (e) => {
                setNumber(e.target.value);
              }
            } className="w-3/5 my-2 " type="text" placeholder="Enter number to make request from" />
            <input
              onChange={
                (e) => {
                  setLog(e.target.value);
                }
              }
              className="w-3/5 my-2" type="text" placeholder="Enter log" />

            <div className="grid place-items-center mt-14 ">
              <div className="mt-2">
                <button onClick={
                  () => onSearchSubmit("aaa")
                } type="button"
                        className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Get
                  Get SMS Support
                </button>
              </div>
            </div>

          </div>


        </div>
        <div>
          {load ? <div className="grid place-items-center my-14  ">loading </div> :<div></div> }
        </div>
      </section>
      <Footer />
    </>
  );
};

export default SmsService;