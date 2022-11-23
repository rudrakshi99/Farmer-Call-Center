import { useNavigate } from "react-router-dom";
import "../../index.css";
import { Component } from "react";

class CardBar extends Component {
  render() {
    return <section className="body__section my-10">
      <div className="grid place-items-center mt-5">
        <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">HOW KRASHAK HELPS</p>
        <p className="text-sm font-medium text-center text-gray-500 ">Being a part of Krashak.ai, these are our
          mainstays</p>
      </div>
      <div className="inline-flex flex-col space-y-16 items-start justify-start px-32 pt-12 pb-1.5">

        <div className="inline-flex space-x-36 items-center justify-end">
          <div className="w-1/4 h-full">
            <div
              className="inline-flex flex-col space-y-6 items-center justify-end flex-1 h-full pl-9 pr-8 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
              <img className="w-1/5 h-12 rounded-lg" src="https://via.placeholder.com/46x46" />
              <p className="w-56 h-7 text-lg font-semibold text-gray-900">24*7 calls and help desk</p>
              <p className="opacity-70 w-56 h-1/5 text-base text-center">Providing solutions through calls</p>
            </div>
          </div>
          <div className="w-1/4 h-full">
            <div
              className="inline-flex flex-col space-y-5 items-center justify-end flex-1 h-full pl-12 pr-5 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
              <img className="w-14 h-14 rounded-lg" src="https://via.placeholder.com/54x54" />
              <p className="w-full h-7 text-lg font-semibold text-gray-900">SMS services for contact</p>
              <p className="opacity-70 w-52 h-1/5 text-base text-center">Send your queries through SMS</p>
            </div>
          </div>
          <div className="w-1/4 h-full">
            <div
              className="inline-flex flex-col space-y-5 items-end justify-end flex-1 h-full pl-16 pr-10 pt-8 pb-12 bg-white border rounded border-black border-opacity-10">
              <img className="w-14 h-14 rounded-full" src="https://via.placeholder.com/56x56" />
              <p className="w-44 h-7 text-lg font-semibold text-gray-900">Voice assistent</p>
              <p className="opacity-70 w-44 h-1/5 text-base text-center">Get voice assisted solution</p>
            </div>
          </div>
        </div>
      </div>
    </section>;
  }
}

class HelpCard extends Component {
  render() {
    return <section className="bg-gray-100 py-10">
      <div className="grid place-items-center mt-14 ">
        <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">NEED HELP?</p>
        <p className="text-sm font-medium text-center text-gray-500 max-w-md">We open the door to thousands of farmers
          worldwide. Ask your queries and get the best solution instantly. There are two ways to get the solutions.
        </p>
      </div>
      <div className="grid place-items-center mt-14 mb-20">
        <div className="flex space-x-20">
          <div className="flex flex-row m-2">
            <img className="rounded-lg mr-3" src="https://via.placeholder.com/46x46" />

            <div className="flex flex-column flex-wrap w-40">
              <p className=""
              >Give krashak a call </p>
              <p className=""
              >9876644566</p>
            </div>
          </div>
          <div className="flex flex-row m-2">
            <img className="rounded-lg mr-3" src="https://via.placeholder.com/46x46" />

            <div className="flex flex-column flex-wrap w-40">
              <p className=""
              >Give krashak a call </p>
              <p className=""
              >9876644566</p>
            </div>
          </div>
          <div className="flex flex-row m-2">
            <img className="rounded-lg mr-3" src="https://via.placeholder.com/46x46" />

            <div className="flex flex-column flex-wrap w-40">
              <p className=""
              >Give krashak a call </p>
              <p className=""
              >9876644566</p>
            </div>
          </div>
        </div>
      </div>
    </section>;
  }
}

const Body = () => {
  const navigate = useNavigate();
  return (
    <div className="body">

      <CardBar />
      <HelpCard />
      <section className="flex flex-col mr-5">
        <div className="grid place-items-center my-14 ">
          <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">FEATURES EXPLORED</p>
          <p className="text-sm font-medium text-center text-gray-500 max-w-md"> Take a look at our features
          </p>
        </div>
        <img src="home_image.jpeg"></img>
      </section>
    </div>
  );
};

export default Body;