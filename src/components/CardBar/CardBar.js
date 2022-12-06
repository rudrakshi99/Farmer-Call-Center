import { Component } from "react";
import Image from "../img/voice-message.png";
import SMS from "../img/sms.png";
import Help from "../img/help-desk.png";

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
                <img className="w-1/5 h-12 rounded-lg" src={Help} alt="help" />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900 text-center">
                  24*7 calls and help desk
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Providing solutions through calls
                </p>
              </div>
            </div>
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-6 items-center justify-end flex-1 h-full pl-9 pr-8 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img className="w-14 h-14 rounded-lg" src={SMS} alt="SMS" />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900 text-center">
                  SMS services for contact
                </p>
                <p className="opacity-70 w-56 h-1/5 text-base text-center">
                  Send your queries through SMS
                </p>
              </div>
            </div>
            <div className="w-1/4 h-full">
              <div className="inline-flex flex-col space-y-6 items-center justify-end flex-1 h-full pl-9 pr-8 pt-8 pb-11 bg-white border rounded border-black border-opacity-10">
                <img
                  src={Image}
                  className="w-14 h-14 rounded-lg"
                  alt="voice assistance"
                />
                <p className="w-56 h-7 text-lg font-semibold text-gray-900 text-center">
                  Voice assistant System
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

export default CardBar;
