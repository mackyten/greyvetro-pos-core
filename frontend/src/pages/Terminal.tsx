import { useState } from 'react';
import apiClient from '../api/client';

export default function Terminal() {
  const [result, setResult] = useState<unknown>(null);

  async function processTransaction() {
    const res = await apiClient.post('/api/transactions', { amount: 100 });
    setResult(res.data);
  }

  return (
    <div>
      <h1>POS Terminal</h1>
      <button onClick={processTransaction}>Process Transaction</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
