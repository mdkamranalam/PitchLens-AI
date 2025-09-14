import React from "react";
import { useNavigate } from "react-router-dom";
import UploadForm from "../components/UploadForm";

function Home() {
  const navigate = useNavigate();

  const handleUploadSuccess = (data) => {
    navigate(`/analyze/${data.pitch_id}`);
  };

  return (
    <div className="min-h-screen bg-gray-200 flex items-center justify-center px-4">
      <div className="text-center">
        <p className="text-lg text-gray-600 mb-8 px-2">
          Analyze startup pitch decks and generate actionable insights for
          venture capitalists.
        </p>
        <UploadForm onUploadSuccess={handleUploadSuccess} />
      </div>
    </div>
  );
}

export default Home;
