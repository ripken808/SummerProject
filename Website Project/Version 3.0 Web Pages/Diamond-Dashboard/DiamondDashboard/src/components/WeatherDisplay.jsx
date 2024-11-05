import React, { useEffect, useState } from "react";
import OriolesStadium from "../assets/stadiums/Orioles-Stadium.png";
import RedSoxStadium from "../assets/stadiums/RedSox-Stadium.png";
import YankeesStadium from "../assets/stadiums/Yankees-Stadium.png";
import RaysStadium from "../assets/stadiums/Rays-Stadium.png";
import BlueJaysStadium from "../assets/stadiums/BlueJays-Stadium.png";
import WhiteSoxStadium from "../assets/stadiums/WhiteSox-Stadium.png";
import GuardiansStadium from "../assets/stadiums/Guardians-Stadium.png";
import TigersStadium from "../assets/stadiums/Tigers-Stadium.png";
import RoyalsStadium from "../assets/stadiums/Royals-Stadium.png";
import TwinsStadium from "../assets/stadiums/Twins-Stadium.png";
import AstrosStadium from "../assets/stadiums/Astros-Stadium.png";
import AngelsStadium from "../assets/stadiums/Angels-Stadium.png";
import AthleticsStadium from "../assets/stadiums/Athletics-Stadium.png";
import MarinersStadium from "../assets/stadiums/Mariners-Stadium.png";
import RangersStadium from "../assets/stadiums/Rangers-Stadium.png";
import BravesStadium from "../assets/stadiums/Braves-Stadium.png";
import MarlinsStadium from "../assets/stadiums/Marlins-Stadium.png";
import MetsStadium from "../assets/stadiums/Mets-Stadium.png";
import PhilliesStadium from "../assets/stadiums/Phillies-Stadium.png";
import NationalsStadium from "../assets/stadiums/Nationals-Stadium.png";
import CubsStadium from "../assets/stadiums/Cubs-Stadium.png";
import RedsStadium from "../assets/stadiums/Reds-Stadium.png";
import BrewersStadium from "../assets/stadiums/Brewers-Stadium.png";
import PiratesStadium from "../assets/stadiums/Pirates-Stadium.png";
import CardinalsStadium from "../assets/stadiums/Cardinals-Stadium.png";
import DiamondbacksStadium from "../assets/stadiums/Diamondbacks-Stadium.png";
import RockiesStadium from "../assets/stadiums/Rockies-Stadium.png";
import DodgersStadium from "../assets/stadiums/Dodgers-Stadium.png";
import PadresStadium from "../assets/stadiums/Padres-Stadium.png";
import GiantsStadium from "../assets/stadiums/Giants-Stadium.png";

// Map team names to stadium images
const stadiumImages = {
  Orioles: OriolesStadium,
  RedSox: RedSoxStadium,
  Yankees: YankeesStadium,
  Rays: RaysStadium,
  BlueJays: BlueJaysStadium,
  WhiteSox: WhiteSoxStadium,
  Guardians: GuardiansStadium,
  Tigers: TigersStadium,
  Royals: RoyalsStadium,
  Twins: TwinsStadium,
  Astros: AstrosStadium,
  Angels: AngelsStadium,
  Athletics: AthleticsStadium,
  Mariners: MarinersStadium,
  Rangers: RangersStadium,
  Braves: BravesStadium,
  Marlins: MarlinsStadium,
  Mets: MetsStadium,
  Phillies: PhilliesStadium,
  Nationals: NationalsStadium,
  Cubs: CubsStadium,
  Reds: RedsStadium,
  Brewers: BrewersStadium,
  Pirates: PiratesStadium,
  Cardinals: CardinalsStadium,
  Diamondbacks: DiamondbacksStadium,
  Rockies: RockiesStadium,
  Dodgers: DodgersStadium,
  Padres: PadresStadium,
  Giants: GiantsStadium,
};

// Map team names to stadium coordinates and names
const stadiumCoordinates = {
  Orioles: {
    name: "Oriole Park at Camden Yards",
    latitude: 39.2856,
    longitude: -76.6216,
  },
  RedSox: { name: "Fenway Park", latitude: 42.3467, longitude: -71.0972 },
  Yankees: { name: "Yankee Stadium", latitude: 40.8296, longitude: -73.9262 },
  Rays: { name: "Tropicana Field", latitude: 27.7683, longitude: -82.6534 },
  BlueJays: { name: "Rogers Centre", latitude: 43.6415, longitude: -79.3894 },
  WhiteSox: {
    name: "Guaranteed Rate Field",
    latitude: 41.83,
    longitude: -87.6339,
  },
  Guardians: {
    name: "Progressive Field",
    latitude: 41.4962,
    longitude: -81.6852,
  },
  Tigers: { name: "Comerica Park", latitude: 42.339, longitude: -83.0485 },
  Royals: { name: "Kauffman Stadium", latitude: 39.0517, longitude: -94.4804 },
  Twins: { name: "Target Field", latitude: 44.9817, longitude: -93.2777 },
  Astros: { name: "Minute Maid Park", latitude: 29.7573, longitude: -95.3555 },
  Angels: { name: "Angel Stadium", latitude: 33.8003, longitude: -117.8827 },
  Athletics: {
    name: "RingCentral Coliseum",
    latitude: 37.7516,
    longitude: -122.2005,
  },
  Mariners: { name: "T-Mobile Park", latitude: 47.5914, longitude: -122.3325 },
  Rangers: { name: "Globe Life Field", latitude: 32.7513, longitude: -97.082 },
  Braves: { name: "Truist Park", latitude: 33.8908, longitude: -84.4678 },
  Marlins: { name: "loanDepot Park", latitude: 25.7781, longitude: -80.2195 },
  Mets: { name: "Citi Field", latitude: 40.7571, longitude: -73.8458 },
  Phillies: {
    name: "Citizens Bank Park",
    latitude: 39.9061,
    longitude: -75.1665,
  },
  Nationals: { name: "Nationals Park", latitude: 38.873, longitude: -77.0074 },
  Cubs: { name: "Wrigley Field", latitude: 41.9484, longitude: -87.6553 },
  Reds: {
    name: "Great American Ball Park",
    latitude: 39.0974,
    longitude: -84.5072,
  },
  Brewers: {
    name: "American Family Field",
    latitude: 43.028,
    longitude: -87.9712,
  },
  Pirates: { name: "PNC Park", latitude: 40.4469, longitude: -80.0057 },
  Cardinals: { name: "Busch Stadium", latitude: 38.6226, longitude: -90.1928 },
  Diamondbacks: {
    name: "Chase Field",
    latitude: 33.4455,
    longitude: -112.0667,
  },
  Rockies: { name: "Coors Field", latitude: 39.7559, longitude: -104.9942 },
  Dodgers: { name: "Dodger Stadium", latitude: 34.0739, longitude: -118.24 },
  Padres: { name: "Petco Park", latitude: 32.7076, longitude: -117.157 },
  Giants: { name: "Oracle Park", latitude: 37.7786, longitude: -122.3893 },
};

const WeatherDisplay = () => {
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedTeam, setSelectedTeam] = useState(null);

  const getSelectedTeamFromCookie = () => {
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith("selectedTeam="))
      ?.split("=")[1];
    return cookieValue;
  };

  const fetchWeather = () => {
    if (!selectedTeam || !stadiumCoordinates[selectedTeam]) {
      setLoading(false);
      return;
    }

    const { latitude, longitude } = stadiumCoordinates[selectedTeam];
    setLoading(true);

    fetch(`http://127.0.0.1:8000/api/weather?lat=${latitude}&lon=${longitude}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setWeather(data);
        setError(null); // Clear any previous errors
        setLoading(false);
      })
      .catch((error) => {
        setError("Error fetching weather data");
        setLoading(false);
      });
  };

  useEffect(() => {
    const team = getSelectedTeamFromCookie();
    if (team) {
      setSelectedTeam(team);
      fetchWeather();

      const intervalId = setInterval(fetchWeather, 60000);
      return () => clearInterval(intervalId);
    } else {
      setLoading(false);
    }
  }, [selectedTeam]);

  if (!selectedTeam || !stadiumImages[selectedTeam]) {
    return null;
  }

  const stadiumName = stadiumCoordinates[selectedTeam].name;

  return (
    <div
      className="relative bg-cover bg-center h-[250px] w-full mt-20"
      style={{
        backgroundImage: `url(${stadiumImages[selectedTeam]})`,
      }}
    >
      <div className="absolute inset-0 bg-black bg-opacity-50 flex flex-col justify-center items-center p-4 rounded-lg z-10">
        <h2 className="text-xl font-bold mb-2 text-white">
          Current Weather at {stadiumName}
        </h2>

        {loading ? (
          <div className="flex justify-center items-center">
            <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-blue-500"></div>
          </div>
        ) : error ? (
          <p className="text-red-500">{error}</p>
        ) : weather ? (
          <>
            <p className="text-md text-white">{weather.city}</p>
            <p className="text-3xl font-bold text-white">
              {weather.temperature}°F
            </p>
            <p className="text-md capitalize text-white">{weather.weather}</p>
          </>
        ) : (
          <p className="text-red-500">No weather data available</p>
        )}
      </div>
    </div>
  );
};

export default WeatherDisplay;
