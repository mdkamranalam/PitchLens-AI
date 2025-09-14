import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { getAnalysis } from "../services/api";
import ReportView from "../components/ReportView";

function Analyze() {
  const { pitchId } = useParams();
  const [pitch, setPitch] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchPitch = async () => {
      try {
        const response = await getAnalysis(pitchId);
        setPitch(response.data);
      } catch (err) {
        setError(err.response?.data?.detail || "Failed to load analysis");
      }
    };
    fetchPitch();
  }, [pitchId]);

  if (error) {
    return <div className="text-red-500 text-center mt-8">{error}</div>;
  }

  if (!pitch) {
    return <div className="text-center mt-8">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <ReportView pitch={pitch} />
    </div>
  );
}

export default Analyze;
