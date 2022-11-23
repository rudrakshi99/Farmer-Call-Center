import PreHeader from "../preheader/preheader";
import React from "react";
import Header from "../Header/Header";
import Body from "../body/body";
import Footer from "../Footer/footer";

const Voice = () => {
  return (
    <>
      <PreHeader />
      <Header />
      <section className="">
        <div className="grid place-items-center my-14  ">
          <div className="container bg-gray-100 p-10 ">
            <div className="bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10  w-full flex flex-row "
            >
              <input className="w-4/5" type="text" placeholder="Search" />
              <div className="ml-16 mt-2">
                <button type="button"
                        className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Button
                </button>
              </div>
            </div>

            <p className="my-10">SEARCH RESULT</p>


            <div className="my-10 p-6 bg-gray-300 bg-opacity-30 border border-gray-900 border-opacity-10"
                 >

              <p className="text-2xl font-medium text-green-600">Transportation Problem and Assignment problem<br /></p>
              <p className="text-lg font-medium">Transportation problem is a special kind of Linear
                Programming Problem (LPP) in which goods are transported from a set of sources to a set of destinations
                ...<br /></p>
              <div className="flex flex-row place-content-end">
                <p className="text-xs font-medium text-green-600">View more</p>
              </div>

            </div>


            <div className="flex justify-between ">
              <div className="mt-2">
                <button type="button"
                        className="inline-block px-6 py-2.5 bg-green-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Not Satisfied? Raise a ticket
                </button>
              </div>
              <div>
                {/*Alan Api here */}
                aa
              </div>
            </div>

          </div>


        </div>
      </section>
      <Footer />
    </>
  );
};

export default Voice;