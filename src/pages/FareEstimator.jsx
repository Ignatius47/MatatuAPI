import { useState, useEffect } from 'react';
import { useQuery } from 'react-query';
import { motion } from 'framer-motion';
import axios from 'axios';
import { BanknotesIcon } from '@heroicons/react/24/outline';
import toast from 'react-hot-toast';

function FareEstimator() {
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');
  const [selectedRoute, setSelectedRoute] = useState('');
  const [routeStops, setRouteStops] = useState([]);

  const { data: routes, isLoading: loadingRoutes, isError: routesError } = useQuery('routes', async () => {
    const response = await axios.get('/api/routes/');
    return response.data;
  });

  useEffect(() => {
    if (selectedRoute) {
      const fetchStops = async () => {
        try {
          const response = await axios.get(`/api/routes/${selectedRoute}/stops/`);
          setRouteStops(response.data);
        } catch (error) {
          console.error('Error fetching stops:', error);
        }
      };
      fetchStops();
    }
  }, [selectedRoute]);

  const { data: fareEstimate, isLoading: estimating, isError: fareError } = useQuery(
    ['fareEstimate', selectedRoute, origin, destination],
    async () => {
      if (!selectedRoute || !origin || !destination) return null;
      const response = await axios.get(
        `/api/routes/${selectedRoute}/estimate_fare/?origin=${origin}&destination=${destination}`
      );
      return response.data;
    },
    {
      enabled: !!(selectedRoute && origin && destination),
      onError: () => {
        toast.error('Unable to estimate fare');
      }
    }
  );

  if (routesError || fareError) {
    return <div className="text-center text-red-600">Error fetching data. Please try again later.</div>;
  }

  if (loadingRoutes) {
    return <div className="text-center text-gray-600">Loading routes...</div>;
  }

  return (
    <div className="max-w-4xl mx-auto p-6">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white rounded-lg shadow-lg p-8"
      >
        <h1 className="text-3xl font-extrabold text-gray-800 mb-6 text-center">Fare Estimator</h1>

        <div className="grid gap-6">
          {/* Route Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Select Route</label>
            <select
              value={selectedRoute}
              onChange={(e) => setSelectedRoute(e.target.value)}
              className="w-full p-3 rounded-md border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-500"
            >
              <option value="">Select a route...</option>
              {routes?.length > 0 ? (
                routes.map((route) => (
                  <option key={route.id} value={route.id}>
                    Route {route.route_number} - {route.name}
                  </option>
                ))
              ) : (
                <option disabled>No routes available</option>
              )}
            </select>
          </div>

          {/* Origin Stop Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Origin Stop</label>
            <select
              value={origin}
              onChange={(e) => setOrigin(e.target.value)}
              className="w-full p-3 rounded-md border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-500"
            >
              <option value="">Select origin...</option>
              {routeStops?.length > 0 ? (
                routeStops.map((stop) => (
                  <option key={stop.id} value={stop.id}>
                    {stop.name}
                  </option>
                ))
              ) : (
                <option disabled>No stops available</option>
              )}
            </select>
          </div>

          {/* Destination Stop Selection */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Destination Stop</label>
            <select
              value={destination}
              onChange={(e) => setDestination(e.target.value)}
              className="w-full p-3 rounded-md border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-500"
            >
              <option value="">Select destination...</option>
              {routeStops?.length > 0 ? (
                routeStops.map((stop) => (
                  <option key={stop.id} value={stop.id}>
                    {stop.name}
                  </option>
                ))
              ) : (
                <option disabled>No stops available</option>
              )}
            </select>
          </div>
        </div>

        {/* Fare Estimate */}
        {estimating ? (
          <div className="text-center py-8">
            <BanknotesIcon className="h-10 w-10 text-emerald-500 animate-pulse mx-auto mb-4" />
            <p className="text-xl text-gray-600">Calculating fare...</p>
          </div>
        ) : fareEstimate && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="bg-emerald-50 p-6 rounded-lg shadow-md"
          >
            <h2 className="text-xl font-semibold text-emerald-700 mb-4">Fare Estimate</h2>
            <p className="text-lg text-gray-700">
              Estimated Fare: <strong className="text-emerald-700">{fareEstimate.fare}</strong>
            </p>
            <p className="text-sm text-gray-500">Currency: {fareEstimate.currency}</p>
          </motion.div>
        )}
      </motion.div>
    </div>
  );
}

export default FareEstimator;