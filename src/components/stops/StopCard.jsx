import { MapPinIcon } from '@heroicons/react/24/outline';
import { motion } from 'framer-motion';
import Card from '../ui/Card';

function StopCard({ stop, onClick }) {
  return (
    <Card onClick={onClick} className="cursor-pointer">
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="space-y-2"
      >
        <h2 className="text-lg font-semibold neon-text">{stop.name}</h2>
        {stop.description && (
          <p className="text-sm text-gray-400">{stop.description}</p>
        )}
        <div className="flex items-center text-sm text-gray-500">
          <MapPinIcon className="h-4 w-4 mr-1" />
          <span>
            {stop.latitude.toFixed(4)}, {stop.longitude.toFixed(4)}
          </span>
        </div>
      </motion.div>
    </Card>
  );
}

export default StopCard;