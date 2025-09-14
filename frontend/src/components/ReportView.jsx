import React from "react";

function ReportView({ pitch }) {
  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">
        {pitch.enriched_data.company_name}
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h3 className="text-xl font-semibold mb-2">Sections</h3>
          <div className="mb-4">
            <h4 className="font-medium">Team</h4>
            <p className="text-gray-600">{pitch.sections.team}</p>
          </div>
          <div className="mb-4">
            <h4 className="font-medium">Market</h4>
            <p className="text-gray-600">{pitch.sections.market}</p>
          </div>
          <div className="mb-4">
            <h4 className="font-medium">Product/Traction</h4>
            <p className="text-gray-600">{pitch.sections.product_traction}</p>
          </div>
        </div>
        <div>
          <h3 className="text-xl font-semibold mb-2">Enriched Data</h3>
          <p>
            <strong>Funding Raised:</strong>{" "}
            {pitch.enriched_data.funding_raised}
          </p>
          <p>
            <strong>Team Size:</strong> {pitch.enriched_data.team_size}
          </p>
          <p>
            <strong>Location:</strong> {pitch.enriched_data.location}
          </p>
          <p>
            <strong>Industry:</strong> {pitch.enriched_data.industry}
          </p>
          <p>
            <strong>Uploaded:</strong>{" "}
            {new Date(pitch.created_at).toLocaleString()}
          </p>
        </div>
      </div>
      <div className="mt-6">
        <h3 className="text-xl font-semibold mb-2">AI Analysis</h3>
        <div className="mb-4">
          <h4 className="font-medium">Summary</h4>
          <p className="text-gray-600">
            {pitch.analysis.summary || "No summary available"}
          </p>
        </div>
        <div className="mb-4">
          <h4 className="font-medium">SWOT Analysis</h4>
          {pitch.analysis.swot ? (
            <ul className="list-disc pl-5 text-gray-600">
              <li>
                <strong>Strengths:</strong> {pitch.analysis.swot.strengths}
              </li>
              <li>
                <strong>Weaknesses:</strong> {pitch.analysis.swot.weaknesses}
              </li>
              <li>
                <strong>Opportunities:</strong>{" "}
                {pitch.analysis.swot.opportunities}
              </li>
              <li>
                <strong>Threats:</strong> {pitch.analysis.swot.threats}
              </li>
            </ul>
          ) : (
            <p className="text-gray-600">No SWOT analysis available</p>
          )}
        </div>
        <div className="mb-4">
          <h4 className="font-medium">Risks</h4>
          {pitch.analysis.risks && pitch.analysis.risks.length > 0 ? (
            <ul className="list-disc pl-5 text-gray-600">
              {pitch.analysis.risks.map((risk, index) => (
                <li key={index}>{risk}</li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-600">No risks identified</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default ReportView;
