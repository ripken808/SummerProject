import React, { useEffect, useState } from "react";
import TweetData from "./TweetData";
import XCool from "../assets/images/XCool.png";

// Import all team logos from the correct path
import OriolesLogo from "../assets/teams/Orioles.png";
import RedSoxLogo from "../assets/teams/RedSox.png";
import YankeesLogo from "../assets/teams/Yankees.png";
import RaysLogo from "../assets/teams/Rays.png";
import BlueJaysLogo from "../assets/teams/BlueJays.png";
import WhiteSoxLogo from "../assets/teams/WhiteSox.png";
import GuardiansLogo from "../assets/teams/Guardians.png";
import TigersLogo from "../assets/teams/Tigers.png";
import RoyalsLogo from "../assets/teams/Royals.png";
import TwinsLogo from "../assets/teams/Twins.png";
import AstrosLogo from "../assets/teams/Astros.png";
import AngelsLogo from "../assets/teams/Angels.png";
import AthleticsLogo from "../assets/teams/Athletics.png";
import MarinersLogo from "../assets/teams/Mariners.png";
import RangersLogo from "../assets/teams/Rangers.png";
import BravesLogo from "../assets/teams/Braves.png";
import MarlinsLogo from "../assets/teams/Marlins.png";
import MetsLogo from "../assets/teams/Mets.png";
import PhilliesLogo from "../assets/teams/Phillies.png";
import NationalsLogo from "../assets/teams/Nationals.png";
import CubsLogo from "../assets/teams/Cubs.png";
import RedsLogo from "../assets/teams/Reds.png";
import BrewersLogo from "../assets/teams/Brewers.png";
import PiratesLogo from "../assets/teams/Pirates.png";
import CardinalsLogo from "../assets/teams/Cardinals.png";
import DiamondbacksLogo from "../assets/teams/Diamondbacks.png";
import RockiesLogo from "../assets/teams/Rockies.png";
import DodgersLogo from "../assets/teams/Dodgers.png";
import PadresLogo from "../assets/teams/Padres.png";
import GiantsLogo from "../assets/teams/Giants.png";

const TweetsContainer = () => {
  const [tweets, setTweets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchTweets = () => {
    setLoading(true); // Set loading to true when fetching starts
    fetch("http://127.0.0.1:8000/api/team/Yankees")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setTweets(data);
        setLoading(false); // Set loading to false when data is received
      })
      .catch((error) => {
        setError(error);
        setLoading(false); // Set loading to false on error
      });
  };

  useEffect(() => {
    fetchTweets(); // Initial fetch
    const intervalId = setInterval(fetchTweets, 60000); // Fetch every 10 seconds

    return () => clearInterval(intervalId); // Clear interval on unmount
  }, []);

  return (
    <div className="w-full md:w-1/3 mx-auto mt-8">
      {/* Logo Section */}
      <div className="flex items-center justify-center bg-black p-4 rounded-t-lg">
        <a
          href="https://twitter.com/Yankees"
          target="_blank"
          rel="noopener noreferrer"
          className="focus:outline-none"
        >
          <img
            src={XCool}
            alt="X Logo"
            className="h-20 w-auto cursor-pointer animate-pulse"
          />
        </a>
      </div>

      {/* Tweet Display Section with scroll */}
      <div className="border-black border-8 rounded-b-lg overflow-y-auto max-h-[80vh] bg-white">
        {loading ? (
          <div className="flex justify-center items-center h-full relative">
            <div className="animate-spin rounded-full h-32 w-32 border-t-8 border-b-8 border-blue-500"></div>
            <img
              src={YankeesLogo}
              alt="X Logo"
              className="h-20 w-auto absolute"
            />
          </div>
        ) : error ? (
          <p className="text-red-500 text-center">Error: {error.message}</p>
        ) : tweets.length > 0 ? (
          tweets.map((tweet, index) => <TweetData key={index} tweet={tweet} />)
        ) : (
          <p className="text-center">No tweets available</p>
        )}
      </div>
    </div>
  );
};

export default TweetsContainer;
