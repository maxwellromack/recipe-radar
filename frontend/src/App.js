import './App.css';
import EditRecipe from './pages/EditRecipe';
import Landing from './pages/Landing';
import Login from './pages/Login';
import RecipeMain from './pages/RecipeMain';
import Register from './pages/Register';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        {/* Define your routes here */}
        <Route path="/" element={<Landing />} /> {/* Render Hero component as main page */}
        <Route path="/login" element={<Login />} /> {/* Render Login component when URL is /login */}
        <Route path="/register" element={<Register />} /> {/* Render Register component when URL is /register */}
        <Route path="/recipemain" element={<RecipeMain />} /> {/* Render Register component when URL is /register */}
        <Route path="/editrecipe" element={<EditRecipe />} /> {/* Render Register component when URL is /register */}
      </Routes>
    </Router>
  );
}

export default App;
