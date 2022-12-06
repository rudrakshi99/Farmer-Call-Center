import PreHeader from "../../components/preheader/preheader";
import React, { useEffect, useState } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/footer";
import alanBtn from "@alan-ai/alan-sdk-web";
// let alanKey = "67254c6d750a036c9a01ac6ae831c3202e956eca572e1d8b807a3e2338fdd0dc/stage
let alanKey =
  "2929637674a720da423ab91d9237489a2e956eca572e1d8b807a3e2338fdd0dc/stage";

const Voice = () => {
  const [load, setLoad] = useState(false);
  const [log, setLog] = useState("");

  const [organic1, setOrganic1] = useState("");
  const [organic1Link, setOrganic1Link] = useState("");
  const [organic1Title, setOrganic1Title] = useState("");

  const [organic2, setOrganic2] = useState("");
  const [organic2Link, setOrganic2Link] = useState("");
  const [organic2Title, setOrganic2Title] = useState("");

  // const [organic3, setOrganic3] = useState("");
  // const [organic3Link, setOrganic3Link] = useState("");
  // const [organic3Title, setOrganic3Title] = useState("");
  //
  // const [organic4, setOrganic4] = useState("");
  // const [organic4Link, setOrganic4Link] = useState("");
  // const [organic4Title, setOrganic4Title] = useState("");
  //
  // const [organic5, setOrganic5] = useState("");
  // const [organic5Link, setOrganic5Link] = useState("");
  // const [organic5Title, setOrganic5Title] = useState("");

  const [lang, setLang] = useState("en");
  function onSearchSubmit(term) {
    setLoad(true);
    console.log("Clicked");
    let url = "http://127.0.0.1:5000/farmers-log";
    let body = JSON.stringify({
      log: log,
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
          setOrganic1(main_data["organic_result_1"]["response"]);
          setOrganic1Link(main_data["organic_result_1"]["link"]);
          setOrganic1Title(main_data["organic_result_1"]["title"]);

          setOrganic2(main_data["organic_result_2"]["response"]);
          setOrganic2Link(main_data["organic_result_2"]["link"]);
          setOrganic2Title(main_data["organic_result_2"]["title"]);

          // setOrganic3(main_data["organic_result_3"]["response"]);
          // setOrganic3Link(main_data["organic_result_3"]["link"]);
          // setOrganic3Title(main_data["organic_result_3"]["title"]);
          //
          // setOrganic4(main_data["organic_result_4"]["response"]);
          // setOrganic4Link(main_data["organic_result_4"]["link"]);
          // setOrganic4Title(main_data["organic_result_4"]["title"]);
          //
          // setOrganic5(main_data["organic_result_5"]["response"]);
          // setOrganic5Link(main_data["organic_result_5"]["link"]);
          // setOrganic5Title(main_data["organic_result_5"]["title"]);

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

  useEffect(() => {
    alanBtn({
      key: alanKey,
      onCommand: ({ command }) => {
        if (command.includes("showweather")) {
          console.log("testCommand");
          alert("This is a Alan AI demo");
        }
      }
    });
  }, []);

  return (
    <>
      <PreHeader />
      <Header />
      <section className="">
        <div className="grid place-items-center my-14  ">
          <div className="container bg-gray-100 p-10  mt-14 text-center">
            <p className="text-2xl font-medium text-green-600 my-12">
              Ask your queries here
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
            <div className="bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10  w-full flex flex-row ">
              <input
                onChange={(e) => {
                  setLog(e.target.value);
                }}
                className="w-4/5 pr-4"
                type="text"
                placeholder="Search"
              />
              <div className="ml-16 mt-2">
                <button
                  onClick={() => onSearchSubmit()}
                  type="button"
                  className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                >
                  Search Now
                </button>
              </div>
            </div>

            <p className="my-10">SEARCH RESULT</p>

            <div className="my-10 p-6 bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10">
              <p className="text-2xl font-medium text-green-600">
                {organic1Title}
                <br />
              </p>
              {/*<p className="text-lg font-medium">{organic1.toString()}<br /></p>*/}
              {organic1}
              <div className="flex flex-row place-content-end">
                <p className="text-xs font-medium text-green-600">
                  <a href={organic1Link}>Read More</a>
                </p>
              </div>
            </div>

            <div className="my-10 p-6 bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10">
              <p className="text-2xl font-medium text-green-600">
                {organic2Title}
                <br />
              </p>
              {/*<p className="text-lg font-medium">{organic1.toString()}<br /></p>*/}
              {organic2}
              <div className="flex flex-row place-content-end">
                <p className="text-xs font-medium text-green-600">
                  <a href={organic2Link}>Read More</a>
                </p>
              </div>
            </div>

            {/*<div className="my-10 p-6 bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10"*/}
            {/*>*/}

            {/*  <p className="text-2xl font-medium text-green-600">{organic3Title}<br /></p>*/}
            {/*  /!*<p className="text-lg font-medium">{organic1.toString()}<br /></p>*!/*/}
            {/*  {organic3.toString()}*/}
            {/*  <div className="flex flex-row place-content-end">*/}
            {/*    <p className="text-xs font-medium text-green-600"><a href={organic3Link}>Read More</a></p>*/}
            {/*  </div>*/}

            {/*</div>*/}

            {/*<div className="my-10 p-6 bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10"*/}
            {/*>*/}

            {/*  <p className="text-2xl font-medium text-green-600">{organic4Title}<br /></p>*/}
            {/*  /!*<p className="text-lg font-medium">{organic1.toString()}<br /></p>*!/*/}
            {/*  {organic4.toString()}*/}
            {/*  <div className="flex flex-row place-content-end">*/}
            {/*    <p className="text-xs font-medium text-green-600"><a href={organic4Link}>Read More</a></p>*/}
            {/*  </div>*/}

            {/*</div>*/}

            {/*<div className="my-10 p-6 bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10"*/}
            {/*>*/}

            {/*  <p className="text-2xl font-medium text-green-600">{organic5Title}<br /></p>*/}
            {/*  /!*<p className="text-lg font-medium">{organic1.toString()}<br /></p>*!/*/}
            {/*  {organic5.toString()}*/}
            {/*  <div className="flex flex-row place-content-end">*/}
            {/*    <p className="text-xs font-medium text-green-600"><a href={organic5Link}>Read More</a></p>*/}
            {/*  </div>*/}

            {/*</div>*/}

            <div className="flex justify-between ">
              <div className="mt-2">
                <button
                  type="button"
                  className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
                >
                  Not Satisfied? Raise a ticket
                </button>
              </div>
              <div>{/*Alan Api here */}</div>
            </div>
          </div>
        </div>
        <div>
          {load ? (
            <div className="grid place-items-center my-14  ">loading </div>
          ) : (
            <div></div>
          )}
        </div>
      </section>
      <Footer />
    </>
  );
};

export default Voice;
