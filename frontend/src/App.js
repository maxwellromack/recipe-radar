import './App.css';
import Hero from './components/Hero';
import Login from './components/Login';
import Register from './components/Register';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        {/* Define your routes here */}
        <Route path="/" element={<Hero />} /> {/* Render Hero component as main page */}
        <Route path="/login" element={<Login />} /> {/* Render Login component when URL is /login */}
        <Route path="/register" element={<Register />} /> {/* Render Register component when URL is /register */}
      </Routes>
    </Router>
  );
}

export default App;