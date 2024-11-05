import React, { useState, useEffect } from "react";
import { FiSun, FiMoon } from "react-icons/fi"; // Import icons from react-icons

const ThemeSwitch = () => {
  const [darkMode, setDarkMode] = useState(false);

  // Toggle the dark mode
  const toggleTheme = () => {
    setDarkMode(!darkMode);
  };

  // Apply background color depending on the theme
  useEffect(() => {
    if (darkMode) {
      document.body.style.backgroundColor = "#1B1B1B"; // Dark mode background
    } else {
      document.body.style.backgroundColor = "#ffffff"; // Light mode background
    }
  }, [darkMode]);

  return (
    <div className="fixed bottom-4 left-4 p-4">
      {/* Switch container */}
      <label
        htmlFor="themeSwitch"
        className="relative inline-flex items-center cursor-pointer group"
      >
        {/* Hidden checkbox for accessibility */}
        <input
          type="checkbox"
          id="themeSwitch"
          className="sr-only" // Hide the checkbox visually
          checked={darkMode}
          onChange={toggleTheme}
        />
        {/* Switch background and gradient border on hover */}
        <div
          className={`w-20 h-10 rounded-full p-1 transition-all duration-500 ease-in-out shadow-lg ${
            darkMode
              ? "bg-gray-800 border border-gray-700"
              : "bg-yellow-300 border border-yellow-400"
          } group-hover:border-transparent group-hover:bg-gradient-to-r group-hover:from-indigo-500 group-hover:to-pink-500 relative`}
        >
          {/* Glow effect on hover */}
          <div
            className="absolute inset-0 rounded-full bg-transparent transition duration-300 ease-in-out group-hover:bg-opacity-20 group-hover:bg-purple-500"
            style={{
              boxShadow: darkMode
                ? "0 0 10px rgba(255, 255, 255, 0.2)"
                : "0 0 10px rgba(0, 0, 0, 0.2)",
            }}
          ></div>

          {/* Ball inside the switch */}
          <div
            className={`w-8 h-8 rounded-full shadow-md transform transition-all duration-500 ease-in-out flex items-center justify-center ${
              darkMode ? "translate-x-10 bg-gray-900" : "translate-x-0 bg-white"
            }`}
          >
            {/* Sun or Moon icon */}
            {darkMode ? (
              <FiMoon className="text-yellow-300 text-xl" /> // Moon Icon
            ) : (
              <FiSun className="text-yellow-500 text-xl" /> // Sun Icon
            )}
          </div>
        </div>
      </label>
    </div>
  );
};

export default ThemeSwitch;
