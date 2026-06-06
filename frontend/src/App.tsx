import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './auth/KeycloakProvider';
import { PrivateRoute } from './auth/PrivateRoute';
import Dashboard from './pages/Dashboard';
import Terminal from './pages/Terminal';
import Shifts from './pages/Shifts';
import Unauthorized from './pages/Unauthorized';

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/unauthorized" element={<Unauthorized />} />
          <Route path="/" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
          <Route path="/terminal" element={<PrivateRoute requiredRole="Cashier"><Terminal /></PrivateRoute>} />
          <Route path="/shifts" element={<PrivateRoute requiredRole="ShiftLead"><Shifts /></PrivateRoute>} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
