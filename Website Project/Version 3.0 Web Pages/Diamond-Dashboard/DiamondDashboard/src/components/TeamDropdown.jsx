import React, { useState } from "react";

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

const TeamDropdown = () => {
  // List of MLB teams with their corresponding logo imports
  const mlbTeamsWithLogos = {
    "American League East": [
      { name: "Baltimore Orioles", logo: OriolesLogo, id: "Orioles" },
      { name: "Boston Red Sox", logo: RedSoxLogo, id: "RedSox" },
      { name: "New York Yankees", logo: YankeesLogo, id: "Yankees" },
      { name: "Tampa Bay Rays", logo: RaysLogo, id: "Rays" },
      { name: "Toronto Blue Jays", logo: BlueJaysLogo, id: "BlueJays" },
    ],
    "American League Central": [
      { name: "Chicago White Sox", logo: WhiteSoxLogo, id: "WhiteSox" },
      { name: "Cleveland Guardians", logo: GuardiansLogo, id: "Guardians" },
      { name: "Detroit Tigers", logo: TigersLogo, id: "Tigers" },
      { name: "Kansas City Royals", logo: RoyalsLogo, id: "Royals" },
      { name: "Minnesota Twins", logo: TwinsLogo, id: "Twins" },
    ],
    "American League West": [
      { name: "Houston Astros", logo: AstrosLogo, id: "Astros" },
      { name: "Los Angeles Angels", logo: AngelsLogo, id: "Angels" },
      { name: "Oakland Athletics", logo: AthleticsLogo, id: "Athletics" },
      { name: "Seattle Mariners", logo: MarinersLogo, id: "Mariners" },
      { name: "Texas Rangers", logo: RangersLogo, id: "Rangers" },
    ],
    "National League East": [
      { name: "Atlanta Braves", logo: BravesLogo, id: "Braves" },
      { name: "Miami Marlins", logo: MarlinsLogo, id: "Marlins" },
      { name: "New York Mets", logo: MetsLogo, id: "Mets" },
      { name: "Philadelphia Phillies", logo: PhilliesLogo, id: "Phillies" },
      { name: "Washington Nationals", logo: NationalsLogo, id: "Nationals" },
    ],
    "National League Central": [
      { name: "Chicago Cubs", logo: CubsLogo, id: "Cubs" },
      { name: "Cincinnati Reds", logo: RedsLogo, id: "Reds" },
      { name: "Milwaukee Brewers", logo: BrewersLogo, id: "Brewers" },
      { name: "Pittsburgh Pirates", logo: PiratesLogo, id: "Pirates" },
      { name: "St. Louis Cardinals", logo: CardinalsLogo, id: "Cardinals" },
    ],
    "National League West": [
      {
        name: "Arizona Diamondbacks",
        logo: DiamondbacksLogo,
        id: "Diamondbacks",
      },
      { name: "Colorado Rockies", logo: RockiesLogo, id: "Rockies" },
      { name: "Los Angeles Dodgers", logo: DodgersLogo, id: "Dodgers" },
      { name: "San Diego Padres", logo: PadresLogo, id: "Padres" },
      { name: "San Francisco Giants", logo: GiantsLogo, id: "Giants" },
    ],
  };

  const [isHovered, setIsHovered] = useState(false);

  // Function to handle team selection and set the cookie
  const handleTeamSelection = (teamId) => {
    // Set the cookie for selected team
    document.cookie = `selectedTeam=${teamId}; path=/;`;

    // Refresh the page to update components with the new cookie value
    window.location.reload();
  };

  return (
    <div className="relative inline-block text-left">
      {/* Dropdown Button */}
      <div
        className="inline-block bg-red-800 text-white px-4 py-2 rounded-md cursor-pointer"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        MLB Teams
        {isHovered && (
          <div className="absolute right-0 mt-2 bg-white shadow-lg rounded-md p-6 w-[1000px]">
            {/* Grid layout for teams with logos */}
            <div className="grid grid-cols-3 gap-4">
              {Object.keys(mlbTeamsWithLogos).map((division, divisionIndex) => (
                <div key={divisionIndex} className="text-left">
                  {/* Division Header */}
                  <div className="font-bold text-blue-600 text-lg mb-2">
                    {division}
                  </div>
                  <ul className="space-y-2">
                    {mlbTeamsWithLogos[division]
                      .sort((a, b) => a.name.localeCompare(b.name))
                      .map((team, teamIndex) => (
                        <li
                          key={teamIndex}
                          className="flex items-center space-x-2 cursor-pointer"
                          onClick={() => handleTeamSelection(team.id)}
                        >
                          {/* Team logo */}
                          <img
                            src={team.logo}
                            alt={`${team.name} logo`}
                            className="h-6 w-6"
                          />
                          {/* Team name */}
                          <span className="text-gray-800 hover:text-blue-500 transition-colors duration-200">
                            {team.name}
                          </span>
                        </li>
                      ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default TeamDropdown;
