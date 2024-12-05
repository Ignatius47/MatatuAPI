import { useCallback } from 'react';
import Map, { NavigationControl } from 'react-map-gl';
import 'mapbox-gl/dist/mapbox-gl.css';

const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN;

const defaultMapStyle = {
  width: '100%',
  height: 400,
  borderRadius: '0.5rem',
};

function MapView({ viewport, onViewportChange, style = {}, children }) {
  const handleMove = useCallback(evt => {
    onViewportChange(evt.viewport);
  }, [onViewportChange]);

  return (
    <Map
      {...viewport}
      onMove={handleMove}
      style={{ ...defaultMapStyle, ...style }}
      mapStyle="mapbox://styles/mapbox/dark-v11"
      mapboxAccessToken={MAPBOX_TOKEN}
    >
      <NavigationControl position="top-right" />
      {children}
    </Map>
  );
}

export default MapView;