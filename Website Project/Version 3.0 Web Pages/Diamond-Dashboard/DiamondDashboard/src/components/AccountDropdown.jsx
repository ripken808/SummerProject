import React, { useState } from "react";
import { Link } from "react-router-dom";
import profileImage from "../assets/images/user.png";

const AccountDropdown = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  return (
    <div className="relative inline-block text-left">
      {/* Dropdown Button */}
      <button
        onClick={toggleDropdown}
        className="relative w-12 h-12 rounded-full border-2 border-gray-300 overflow-hidden focus:outline-none shadow-lg transition duration-300 ease-in-out hover:animate-pulse"
      >
        {/* Blinking Ring on Hover */}
        <span
          className={`absolute inset-0 rounded-full ${
            isDropdownOpen
              ? "animate-ping ring-4 ring-blue-500 ring-opacity-50"
              : ""
          }`}
        ></span>

        {/* Profile Image */}
        <img
          src={profileImage}
          alt="Profile Icon"
          className="w-full h-full object-cover"
        />
      </button>

      {/* Dropdown Menu */}
      {isDropdownOpen && (
        <div
          className="absolute right-0 mt-2 bg-white border border-gray-300 rounded-md shadow-lg w-48"
          onMouseLeave={() => setIsDropdownOpen(false)}
        >
          <ul className="py-2">
            <li>
              <Link
                to="/LogIn"
                className="block px-4 py-2 text-gray-800 hover:bg-gray-100 transition duration-150 ease-in-out"
                onClick={() => setIsDropdownOpen(false)}
              >
                Log In
              </Link>
            </li>
            <li>
              <Link
                to="/CreateAccount"
                className="block px-4 py-2 text-gray-800 hover:bg-gray-100 transition duration-150 ease-in-out"
                onClick={() => setIsDropdownOpen(false)}
              >
                Create Account
              </Link>
            </li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default AccountDropdown;
