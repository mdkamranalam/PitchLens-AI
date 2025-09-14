import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home.jsx";
import Analyze from "./pages/Analyze.jsx";
import Compare from "./pages/Compare.jsx";
import Header from "./sections/Header.jsx";
import Footer from "./sections/Footer.jsx";

function App() {
  return (
    <div className="font-mono">
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/analyze/:pitchId" element={<Analyze />} />
        <Route path="/compare" element={<Compare />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
