import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header className="bg-gray-800 text-white p-4 flex items-center justify-around ">
      <div>
        <Link to="/">
          <h1 className="text-4xl font-bold">PitchLens</h1>
        </Link>
      </div>
      <div>
        <nav className="text-lg">
          <div className="max-w-6xl mx-auto flex justify-between items-center">
            <div>
              <Link
                to="/"
                className="mr-4 hover:text-blue-500 duration-300 transition-colors"
              >
                Home
              </Link>
              <Link
                to="/compare"
                className="hover:text-blue-500 duration-300 transition-colors"
              >
                Compare
              </Link>
            </div>
          </div>
        </nav>
      </div>
    </header>
  );
};

export default Header;
