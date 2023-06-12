import { BrowserRouter, Routes, Route, Link, Outlet } from 'react-router-dom'
import './App.css';
import Landing from './pages/Landing';
import Login from './pages/Login'
import Register from './pages/Register'


function App() {
  return(
    <div className='App' >
      <BrowserRouter>
        <Routes>
          <Route path = "/" element = {<Landing />}/>
          <Route path = "login" element = {<Login />}/>
          <Route path = "register" element = {<Register />}/>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App;
