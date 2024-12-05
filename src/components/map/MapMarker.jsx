import { Marker } from 'react-map-gl';
import { MapPinIcon } from '@heroicons/react/24/outline';

function MapMarker({ latitude, longitude, onClick }) {
  return (
    <Marker latitude={latitude} longitude={longitude}>
      <button
        onClick={onClick}
        className="transform -translate-x-1/2 -translate-y-1/2 hover:scale-110 transition-transform"
      >
        <MapPinIcon className="h-8 w-8 text-primary-500 neon-glow" />
      </button>
    </Marker>
  );
}

export default MapMarker;