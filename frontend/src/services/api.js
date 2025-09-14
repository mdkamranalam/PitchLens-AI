import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const uploadPitch = (formData) => {
  return axios.post(`${API_URL}/upload`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};

export const getAnalysis = (pitchId) => {
  return axios.get(`${API_URL}/analysis/${pitchId}`);
};

export const comparePitches = (pitchIds) => {
  return axios.get(`${API_URL}/compare`, { params: { pitch_ids: pitchIds } });
};
