import React, { useEffect, useState } from "react";

// Define time zones for each MLB team
const mlbStadiumTimeZones = {
  Orioles: "America/New_York",
  RedSox: "America/New_York",
  Yankees: "America/New_York",
  Rays: "America/New_York",
  BlueJays: "America/Toronto",
  WhiteSox: "America/Chicago",
  Guardians: "America/New_York",
  Tigers: "America/Detroit",
  Royals: "America/Chicago",
  Twins: "America/Chicago",
  Astros: "America/Chicago",
  Angels: "America/Los_Angeles",
  Athletics: "America/Los_Angeles",
  Mariners: "America/Los_Angeles",
  Rangers: "America/Chicago",
  Braves: "America/New_York",
  Marlins: "America/New_York",
  Mets: "America/New_York",
  Phillies: "America/New_York",
  Nationals: "America/New_York",
  Cubs: "America/Chicago",
  Reds: "America/New_York",
  Brewers: "America/Chicago",
  Pirates: "America/New_York",
  Cardinals: "America/Chicago",
  Diamondbacks: "America/Phoenix",
  Rockies: "America/Denver",
  Dodgers: "America/Los_Angeles",
  Padres: "America/Los_Angeles",
  Giants: "America/Los_Angeles",
};

// Define stadium lcoation for each MLB team
const mlbLocations = {
  Orioles: "Baltimore",
  RedSox: "Boston",
  Yankees: "New York",
  Rays: "Tampa Bay",
  BlueJays: "Toronto",
  WhiteSox: "Chicago",
  Guardians: "Cleveland",
  Tigers: "Detroit",
  Royals: "Kansas City",
  Twins: "Minneapolis",
  Astros: "Houston",
  Angels: "Anaheim",
  Athletics: "Oakland",
  Mariners: "Seattle",
  Rangers: "Arlington",
  Braves: "Atlanta",
  Marlins: "Miami",
  Mets: "New York",
  Phillies: "Philadelphia",
  Nationals: "Washington",
  Cubs: "Chicago",
  Reds: "Cincinnati",
  Brewers: "Milwaukee",
  Pirates: "Pittsburgh",
  Cardinals: "St. Louis",
  Diamondbacks: "Phoenix",
  Rockies: "Denver",
  Dodgers: "Los Angeles",
  Padres: "San Diego",
  Giants: "San Francisco",
};

const TimeDisplay = ({ className }) => {
  const [currentTime, setCurrentTime] = useState("");
  const [selectedTeam, setSelectedTeam] = useState(null);

  // Retrieve the selected team from cookies
  const getSelectedTeamFromCookie = () => {
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith("selectedTeam="))
      ?.split("=")[1];
    return cookieValue;
  };

  useEffect(() => {
    const team = getSelectedTeamFromCookie();
    setSelectedTeam(team);

    if (team && mlbStadiumTimeZones[team]) {
      const timeZone = mlbStadiumTimeZones[team];

      // Function to update time every second
      const updateTime = () => {
        const now = new Date();
        const formatter = new Intl.DateTimeFormat("en-US", {
          timeZone,
          hour: "2-digit",
          minute: "2-digit",
          hour12: true,
        });
        setCurrentTime(formatter.format(now));
      };

      updateTime(); // Set initial time
      const intervalId = setInterval(updateTime, 1000); // Update every second

      // Cleanup interval on component unmount
      return () => clearInterval(intervalId);
    } else {
      setCurrentTime("Select a team to view the time");
    }
  }, [selectedTeam]);

  const stadiumName = selectedTeam
    ? mlbLocations[selectedTeam]
    : "Selected Stadium";

  return (
    <div className={className}>
      <p className="text-lg font-semibold">
        Time in {stadiumName}: {currentTime}
      </p>
    </div>
  );
};

export default TimeDisplay;
