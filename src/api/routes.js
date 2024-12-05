// src/api/routes.js
import axios from 'axios';

// Set the base URL for Axios
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
});

// Fetch routes based on a search term
export const fetchRoutes = (searchTerm) => {
  return apiClient.get('/routes', { params: { search: searchTerm } });
};
