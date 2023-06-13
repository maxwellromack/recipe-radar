import React from 'react';
import 'tailwindcss/tailwind.css';
import Typed from 'typed.js';
import { useNavigate } from 'react-router-dom';
import { ArrowRightIcon } from '@heroicons/react/solid';
import customLogo from '../images/logo.svg';

const Landing = () => {
  const el = React.useRef(null);
  const navigate = useNavigate();

  React.useEffect(() => {
    const typed = new Typed(el.current, {
      strings: ['CHEFS!', 'COOKS', 'YOU'],
      typeSpeed: 100,
      loop: true,
    });

    return () => {
      typed.destroy();
    };
  }, []);

  return (
    <div className="w-screen h-screen bg-gradient-to-tr from-[#f9f4ff] via-[#e4defc] to-[#ffffff] flex flex-col justify-center items-center relative">
      <a
        href="/login" // Updated link to navigate to "/login"
        className="absolute top-4 right-8 flex items-center text-sm font-semibold leading-6 text-gray-900"
        style={{ marginLeft: '-1rem' }}>
        Log in <ArrowRightIcon className="h-5 w-5 ml-1" />
      </a>
      <div className="absolute top-4 left-4">
        <img src={customLogo} alt="Logo" className="h-10 w-10" />
      </div>
     
      <p className="text-purple-600 font-bold p-2">CREATE RECIPES WITH RECIPE RADAR</p>
      <h1 className="md:text-7xl sm:text-6xl text-4xl font-bold md:py-6">
        Recipes from data.
      </h1>
      <div className="flex justify-center items-center">
        <p className="md:text-5xl sm:text-4xl text-xl font-bold py-4 text-purple-600">
          Fast, creative recipes for
        </p>
        <span
          className="md:text-5xl sm:text-4xl text-xl font-bold md:pl-4 pl-2"
          ref={el}
          style={{ height: '4.5rem' }} // Set a fixed height for the container
        />
      </div>
      <p className="md:text-2xl text-xl font-bold text-gray-500">
        Use your ingredients to create custom recipes.
      </p>
      <div className="flex justify-center">
        <button
          className="bg-purple-600 hover:bg-gradient-to-tr hover:from-purple-700 hover:via-purple-600 hover:to-purple-500 w-[200px] rounded-md font-medium my-6 mx-2 py-3 text-white"
          onClick={() => navigate('/register')}
        >
          Get Started
        </button>
        <button
          className="bg-purple-600 hover:bg-gradient-to-tr hover:from-purple-700 hover:via-purple-600 hover:to-purple-500 w-[200px] rounded-md font-medium my-6 mx-2 py-3 text-white"
          onClick={() => navigate('/login')}
        >
          Login
        </button>
      </div>
    </div>
  );
};

export default Landing;
