import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { MapIcon, CalculatorIcon, MapPinIcon } from '@heroicons/react/24/outline';

// Feature data can be fetched or passed as props for flexibility.
const featureData = [
  {
    icon: MapIcon,
    title: 'Find Routes',
    description: 'Search and explore matatu routes across Nairobi',
    link: '/routes',
    color: 'text-blue-500',
  },
  {
    icon: MapPinIcon,
    title: 'Nearby Stops',
    description: 'Discover matatu stops near your location',
    link: '/nearby',
    color: 'text-green-500',
  },
  {
    icon: CalculatorIcon,
    title: 'Fare Estimator',
    description: 'Calculate fare estimates for your journey',
    link: '/fare-estimate',
    color: 'text-yellow-500',
  },
];

function Home({ features = featureData, animationSettings = {} }) {
  const defaultAnimation = {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
    transition: { delay: 0.2 },
    ...animationSettings, // Allow customization via props
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <motion.div {...defaultAnimation} className="text-center mb-16">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-200 mb-4">
          Welcome to Matatu Transit
        </h1>
        <p className="text-xl text-gray-600 dark:text-gray-400">
          Your guide to navigating Nairobi's public transport system
        </p>
      </motion.div>

      <div className="grid md:grid-cols-3 gap-8">
        {features.map((feature, index) => (
          <motion.div
            key={feature.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.2 }}
          >
            <Link
              to={feature.link}
              className="block p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow"
            >
              <feature.icon
                className={`h-12 w-12 ${feature.color} mb-4`}
                aria-hidden="true"
              />
              <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-200 mb-2">
                {feature.title}
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                {feature.description}
              </p>
            </Link>
          </motion.div>
        ))}
      </div>
    </div>
  );
}

export default Home;
