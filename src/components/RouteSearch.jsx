import { useQuery } from 'react-query';
import { fetchRoutes } from '../api/routes';

export default function RouteSearch({ searchTerm }) {
  const { data, error, isLoading } = useQuery(
    ['routes', searchTerm], 
    () => fetchRoutes(searchTerm), 
    { enabled: !!searchTerm } // Prevent query from running with empty searchTerm
  );

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <ul>
      {data?.data.map((route) => (
        <li key={route.id}>{route.name}</li>
      ))}
    </ul>
  );
}
