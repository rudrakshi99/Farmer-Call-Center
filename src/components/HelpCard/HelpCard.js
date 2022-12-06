import { Component } from "react";
import SMS from "../img/sms.png";
import Help from "../img/help-desk.png";
import Call from "../img/phone-call.png";

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
              <img
                className="w-14 h-14 rounded-lg mr-4"
                src={Call}
                alt="call"
              />
              <div className="flex flex-column flex-wrap w-40">
                <p className="">Give krashak a call </p>
                <p className="text-green-600">9876644566</p>
              </div>
            </div>
            <div className="flex flex-row m-2">
              <img className="w-14 h-14 rounded-lg mr-4" src={SMS} alt="SMS" />
              <div className="flex flex-column flex-wrap w-40">
                <p className="">Drop your query </p>
                <p
                  className="text-green-600 cursor-pointer"
                  onClick={() => {
                    window.location.href = "/sms";
                  }}
                >
                  here to get SMS
                </p>
              </div>
            </div>
            <div className="flex flex-row m-2">
              <img
                className="w-14 h-14 rounded-lg mr-4"
                src={Help}
                alt="help"
              />
              <div className="flex flex-column flex-wrap w-40">
                <p className="">Use the voice bot</p>
                <p
                  className="text-green-600 cursor-pointer"
                  onClick={() => {
                    window.location.href = "/voice";
                  }}
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

export default HelpCard;
