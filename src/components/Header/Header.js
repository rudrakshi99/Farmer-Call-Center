import React from "react";
import "./Header.css";
import { useNavigate } from "react-router-dom";
import logo from "../img/logo.png";

const Header = () => {
  const navigate = useNavigate();

  return (
    <div className="h-16 inPhone">
      <div className="flex content-center">
        <div className="flex items-center cursor-pointer ml-auto lg:ml-32">
          <img
            onClick={() => navigate("/")}
            src={logo}
            className="logoWeb"
            alt=""
          />
          <h3 className="text-md font-bold opacity-[.70]">Krashak.AI</h3>
        </div>
        <div className="flex-2 w-5/12 mx-auto">
          <ul className="flex mt-4 items-around">
            <li
              onClick={() => navigate("/")}
              className="text-lg cursor-pointer font-semibold text-[#219653] hover:opacity-90 lg:ml-7 ml-6 mr-1.5"
            >
              Home
            </li>
            <li
              className="text-lg cursor-pointer font-semibold text-[#219653] hover:opacity-90 ml-6 mr-1.5"
              onClick={() => navigate("/voice")}
            >
              Voice Help
            </li>
            <li
              className="text-lg cursor-pointer font-semibold text-[#219653] hover:opacity-90 ml-6 mr-1.5"
              onClick={() => navigate("/crop")}
            >
              Crop Recommendation
            </li>
            <li
              onClick={() => navigate("/fertilizer")}
              className="text-lg cursor-pointer font-semibold text-[#219653] hover:opacity-90 ml-6 mr-1.5"
            >
              Fertilizer Recommendation
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Header;
