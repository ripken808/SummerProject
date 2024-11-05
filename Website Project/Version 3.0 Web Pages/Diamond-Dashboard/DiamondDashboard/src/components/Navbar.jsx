import { useEffect, useState } from "react";
import logo from "../assets/images/logo.png";
import TeamDropdown from "./TeamDropdown";
import AccountDropdown from "./AccountDropdown";
import { Link } from "react-router-dom";
import TimeDisplay from "./TimeDisplay";

const Navbar = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("session_token");
    setIsAuthenticated(!!token);
  }, []);

  return (
    <nav className="bg-blue-900 border-b border-blue-500 w-full fixed top-0 left-0 z-50">
      <div className="flex h-20 items-center justify-between px-4">
        {/* Left-aligned logo and title */}
        <div className="flex items-center justify-start w-1/3">
          <Link className="flex items-center" to="/">
            <img className="h-10 w-auto" src={logo} alt="React Jobs" />
            <span className="hidden md:block text-white text-2xl font-bold ml-2">
              Diamond Dashboard
            </span>
          </Link>
        </div>

        {/* Centered Time Display */}
        <div className="flex justify-center items-center w-1/3">
          <TimeDisplay className="text-white text-center bg-blue-800 px-3 py-1 rounded-md text-sm" />
        </div>

        {/* Right-aligned dropdown and button */}
        <div className="flex items-center space-x-2 justify-end w-1/3">
          <TeamDropdown />
          {isAuthenticated ? (
            <Link
              to="/user"
              className="text-white bg-black hover:bg-gray-900 hover:text-white rounded-md px-3 py-2"
            >
              User
            </Link>
          ) : (
            <AccountDropdown />
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
