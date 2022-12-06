import { useNavigate } from "react-router-dom";
import "../../index.css";
import { Component } from "react";
import "./body.css";
import Image from "./voice-message.png";
import SMS from "./sms.png";
import Help from "./help-desk.png";
import Call from "./phone-call.png";

class CardBar extends Component {
  render() {
    return (
      <section className="body__section py-10">
        <div className="grid place-items-center mt-5">
          <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">
            HOW KRASHAK HELPS
          </p>
          <p className="text-xl font-medium text-center text-gray-500 ">
            Being a part of Krashak.AI, these are our mainstays
          </p>
        </div>
        <div className="grid place-items-center mt-14 mb-20">
          <div className="inline-flex space-x-36 items-center justify-end">
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-6 items-center justify-end flex-1 h-full pl-9 pr-8 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img className="w-1/5 h-12 rounded-lg" src={Help} />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900">
                  24*7 calls and help desk
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Providing solutions through calls
                </p>
              </div>
            </div>
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-5 items-center justify-end flex-1 h-full pl-12 pr-5 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img className="w-14 h-14 rounded-lg" src={SMS} />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900">
                  SMS services for contact
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Send your queries through SMS
                </p>
              </div>
            </div>
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-5 items-center justify-end flex-1 h-full pl-12 pr-5 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img className="w-14 h-14 rounded-lg" src={Image} />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900">
                  Voice assistent System
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Get voice assisted solution
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

class HelpCard extends Component {
  render() {
    return (
      <section className="bg-gray-100 py-10">
        <div className="grid place-items-center mt-14 ">
          <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">
            NEED HELP?
          </p>
          <p className="text-xl font-medium text-center text-gray-500 ">
            We open the door to thousands of farmers worldwide. Ask your queries
            and get the best solution instantly. There are two ways to get the
            solutions.
          </p>
        </div>
        <div className="grid place-items-center mt-14 mb-20">
          <div className="flex space-x-20">
            <div className="flex flex-row m-2">
              <img className="w-14 h-14 rounded-lg mr-4" src={Call} />
              <div className="flex flex-column flex-wrap w-40">
                <p className="">Give krashak a call </p>
                <p className="text-green-600">9876644566</p>
              </div>
            </div>
            <div className="flex flex-row m-2">
              <img className="w-14 h-14 rounded-lg mr-4" src={SMS} />
              <div className="flex flex-column flex-wrap w-40">
                <p className="">Drop your query to </p>
                <p className="text-green-600">9876644566</p>
              </div>
            </div>
            <div className="flex flex-row m-2">
              <img className="w-14 h-14 rounded-lg mr-4" src={Help} />
              <div className="flex flex-column flex-wrap w-40">
                <p className="">Use the voice bot</p>
                <p
                  className="text-green-600 cursor-pointer"
                  onClick={() => this.navigation.navigate("/voice")}
                >
                  click here
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

const Body = () => {
  const navigate = useNavigate();
  return (
    <div className="body">
      <div className="background-image grid place-items-center my-6">
        <div className="">
          <p className="text-2xl  font-bold text-center text-white uppercase mb-4">
            Farmers' Help Center
          </p>
          <p className="text-6xl font-medium text-center text-green-600 max-w-md mb-4">
            KRASHAK.AI
          </p>
          <p className="text-2xl font-bold text-center text-white uppercase">
            #WeAreFarmers'Voice
          </p>
        </div>
      </div>
      <CardBar />
      <HelpCard />
      <section className="flex flex-col py-5">
        <div className="grid place-items-center my-14 ">
          <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">
            FEATURES EXPLORED
          </p>
          <p className="text-xl font-medium text-center text-gray-500 max-w-md">
            {" "}
            Take a look at our features
          </p>
        </div>
        <img src="home_image.jpeg"></img>
      </section>
    </div>
  );
};

export default Body;
