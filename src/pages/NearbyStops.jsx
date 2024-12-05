import { useState, useEffect } from 'react';
import { useQuery } from 'react-query';
import { motion } from 'framer-motion';
import axios from 'axios';
import { MapPinIcon } from '@heroicons/react/24/outline';
import toast from 'react-hot-toast';
import MapView from '../components/map/MapView';
import MapMarker from '../components/map/MapMarker';
import StopCard from '../components/stops/StopCard';
import LoadingSpinner from '../components/ui/LoadingSpinner';
import PageTransition from '../components/layout/PageTransition';

function NearbyStops() {
  const [location, setLocation] = useState(null);
  const [selectedStop, setSelectedStop] = useState(null);
  const [viewport, setViewport] = useState({
    latitude: -1.2921,
    longitude: 36.8219,
    zoom: 12
  });

  useEffect(() => {
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const newLocation = {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
          };
          setLocation(newLocation);
          setViewport({
            ...newLocation,
            zoom: 14
          });
        },
        () => {
          toast.error('Unable to get your location');
        }
      );
    }
  }, []);

  const { data: nearbyStops, isLoading } = useQuery(
    ['nearbyStops', location],
    async () => {
      if (!location) return null;
      const response = await axios.get(
        `/api/stops/nearby/?latitude=${location.latitude}&longitude=${location.longitude}&radius=1000`
      );
      return response.data;
    },
    { enabled: !!location }
  );

  return (
    <PageTransition>
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <h1 className="text-3xl font-bold neon-text mb-4">Nearby Stops</h1>

          <div className="glass-panel p-4 mb-8">
            <MapView
              viewport={viewport}
              onViewportChange={setViewport}
              style={{ height: 500 }}
            >
              {nearbyStops?.map((stop) => (
                <MapMarker
                  key={stop.id}
                  latitude={stop.latitude}
                  longitude={stop.longitude}
                  onClick={() => setSelectedStop(stop)}
                />
              ))}
              {location && (
                <MapMarker
                  latitude={location.latitude}
                  longitude={location.longitude}
                  color="blue"
                  tooltip="Your Location"
                />
              )}
            </MapView>
          </div>

          {isLoading ? (
            <div className="text-center py-8">
              <LoadingSpinner />
              <p className="mt-4 text-gray-400">Finding stops near you...</p>
            </div>
          ) : (
            <div className="grid md:grid-cols-2 gap-4">
              {nearbyStops?.map((stop) => (
                <StopCard
                  key={stop.id}
                  stop={stop}
                  onClick={() => {
                    setSelectedStop(stop);
                    setViewport({
                      latitude: stop.latitude,
                      longitude: stop.longitude,
                      zoom: 15
                    });
                  }}
                />
              ))}
            </div>
          )}
        </motion.div>
      </div>
    </PageTransition>
  );
}

export default NearbyStops;