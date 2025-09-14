import React, { useState } from "react";
import { comparePitches } from "../services/api";
import CompareView from "../components/CompareView";

function Compare() {
  const [pitchIds, setPitchIds] = useState("");
  const [pitches, setPitches] = useState([]);
  const [error, setError] = useState("");

  const handleCompare = async (e) => {
    e.preventDefault();
    if (!pitchIds) {
      setError("Please enter pitch IDs");
      return;
    }

    try {
      const response = await comparePitches(pitchIds);
      setPitches(response.data);
      setError("");
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to compare pitches");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md mb-8">
        <h2 className="text-2xl font-bold mb-4 text-gray-800">
          Compare Pitches
        </h2>
        <form onSubmit={handleCompare}>
          <input
            type="text"
            value={pitchIds}
            onChange={(e) => setPitchIds(e.target.value)}
            placeholder="Enter pitch IDs (comma-separated)"
            className="w-full p-2 border rounded-md mb-4"
          />
          {error && <p className="text-red-500 text-sm mb-2">{error}</p>}
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700"
          >
            Compare
          </button>
        </form>
      </div>
      {pitches.length > 0 && <CompareView pitches={pitches} />}
    </div>
  );
}

export default Compare;
