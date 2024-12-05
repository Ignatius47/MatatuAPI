import { useState } from 'react';
import { useQuery } from 'react-query';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';
import LoadingSpinner from '../components/LoadingSpinner';
import { debounce } from 'lodash';

function RouteSearch({ apiUrl, initialSearch = '', resultsPerPage = 10 }) {
  const [searchTerm, setSearchTerm] = useState(initialSearch);
  const [debouncedTerm, setDebouncedTerm] = useState(initialSearch);
  const [page, setPage] = useState(1);

  const handleSearchChange = debounce((term) => {
    setDebouncedTerm(term);
    setPage(1); // Reset to first page for new searches
  }, 300);

  const { data, isLoading, isError, error } = useQuery(
    ['routes', debouncedTerm, page],
    async () => {
      const response = await axios.get(apiUrl, {
        params: {
          search: debouncedTerm,
          page,
          limit: resultsPerPage,
        },
      });
      return response.data;
    },
    { enabled: debouncedTerm.length > 0 }
  );

  return (
    <div className="max-w-4xl mx-auto">
      {/* Header Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="mb-8"
      >
        <h1 className="text-3xl font-bold text-gray-900 mb-4">Find Routes</h1>
        <div className="relative">
          <input
            type="text"
            placeholder="Search routes..."
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              handleSearchChange(e.target.value);
            }}
            className="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
          />
          <MagnifyingGlassIcon className="absolute right-3 top-2.5 h-5 w-5 text-gray-400" />
        </div>
      </motion.div>

      {/* Loading State */}
      {isLoading && (
        <div className="text-center py-8">
          <LoadingSpinner />
        </div>
      )}

      {/* Error State */}
      {isError && (
        <div className="text-center py-8 text-red-500">
          <p>Something went wrong: {error.message}</p>
        </div>
      )}

      {/* Results Section */}
      <AnimatePresence>
        {!isLoading && !isError && (
          <motion.div layout className="space-y-4">
            {data?.routes?.length > 0 ? (
              <>
                {data.routes.map((route) => (
                  <motion.div
                    key={route.id}
                    layout
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: 20 }}
                    transition={{ duration: 0.3, ease: 'easeInOut' }}
                    className="bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow"
                  >
                    <h2 className="text-xl font-semibold mb-2">
                      Route {route.route_number} - {route.name}
                    </h2>
                    <p className="text-gray-600 mb-2">{route.description}</p>
                    <div className="text-sm text-gray-500">
                      Base fare: KES {route.base_fare}
                    </div>
                  </motion.div>
                ))}
                {/* Pagination Controls */}
                <div className="flex justify-between items-center mt-4">
                  <button
                    onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
                    disabled={page === 1}
                    className="px-4 py-2 bg-gray-200 rounded disabled:opacity-50"
                  >
                    Previous
                  </button>
                  <span>
                    Page {page} of {data.totalPages || 1}
                  </span>
                  <button
                    onClick={() => setPage((prev) => prev + 1)}
                    disabled={page === data.totalPages}
                    className="px-4 py-2 bg-gray-200 rounded disabled:opacity-50"
                  >
                    Next
                  </button>
                </div>
              </>
            ) : (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                transition={{ duration: 0.3 }}
                className="text-center text-gray-500"
              >
                No routes found. Try a different search term.
              </motion.div>
            )}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export default RouteSearch;