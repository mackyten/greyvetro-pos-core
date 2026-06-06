import { useEffect, useState } from 'react';
import apiClient from '../api/client';

export default function Shifts() {
  const [shifts, setShifts] = useState<unknown[]>([]);

  useEffect(() => {
    apiClient.get('/api/shifts').then((res) => setShifts(res.data));
  }, []);

  return (
    <div>
      <h1>Shift Management</h1>
      <pre>{JSON.stringify(shifts, null, 2)}</pre>
    </div>
  );
}
