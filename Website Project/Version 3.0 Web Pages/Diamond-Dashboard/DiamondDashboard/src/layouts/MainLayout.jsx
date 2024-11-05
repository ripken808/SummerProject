import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
import ThemeSwitch from "../components/ThemeSwitch";

const MainLayout = () => {
  return (
    <>
      <Navbar />
      <Outlet />
      <ThemeSwitch />
    </>
  );
};

export default MainLayout;
