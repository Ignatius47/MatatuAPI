import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { Toaster } from 'react-hot-toast';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import RouteSearch from './pages/RouteSearch';
import NearbyStops from './pages/NearbyStops';
import FareEstimator from './pages/FareEstimator';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-background">
          {/* Background Gradient */}
          <div className="fixed inset-0 bg-gradient-to-b from-secondary-900/20 to-background pointer-events-none" />

          {/* Navbar with responsiveness */}
          <Navbar />

          <main className="container mx-auto px-4 py-8 sm:px-6 lg:px-8 xl:px-12 relative">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/routes" element={<RouteSearch />} />
              <Route path="/nearby" element={<NearbyStops />} />
              <Route path="/fare-estimate" element={<FareEstimator />} />
            </Routes>
          </main>

          {/* Toast Notifications */}
          <Toaster
            position="bottom-right"
            toastOptions={{
              style: {
                background: 'var(--color-surface)',
                color: 'var(--color-text)',
                borderRadius: '0.5rem',
                border: '1px solid rgba(255, 255, 255, 0.1)',
              },
            }}
          />
        </div>
      </Router>
    </QueryClientProvider>
  );
}

export default App;
