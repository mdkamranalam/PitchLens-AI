import React from "react";

function CompareView({ pitches }) {
  return (
    <div className="max-w-6xl mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Compare Pitches</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full table-auto">
          <thead>
            <tr className="bg-gray-100">
              <th className="px-4 py-2 text-left">Company</th>
              <th className="px-4 py-2 text-left">Team</th>
              <th className="px-4 py-2 text-left">Market</th>
              <th className="px-4 py-2 text-left">Product/Traction</th>
              <th className="px-4 py-2 text-left">Funding</th>
              <th className="px-4 py-2 text-left">Team Size</th>
              <th className="px-4 py-2 text-left">Location</th>
              <th className="px-4 py-2 text-left">Industry</th>
            </tr>
          </thead>
          <tbody>
            {pitches.map((pitch) => (
              <tr key={pitch.pitch_id} className="border-t">
                <td className="px-4 py-2">
                  {pitch.enriched_data.company_name}
                </td>
                <td className="px-4 py-2">
                  {pitch.sections.team.substring(0, 50)}...
                </td>
                <td className="px-4 py-2">
                  {pitch.sections.market.substring(0, 50)}...
                </td>
                <td className="px-4 py-2">
                  {pitch.sections.product_traction.substring(0, 50)}...
                </td>
                <td className="px-4 py-2">
                  {pitch.enriched_data.funding_raised}
                </td>
                <td className="px-4 py-2">{pitch.enriched_data.team_size}</td>
                <td className="px-4 py-2">{pitch.enriched_data.location}</td>
                <td className="px-4 py-2">{pitch.enriched_data.industry}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default CompareView;
