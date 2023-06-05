import React from 'react';
import 'tailwindcss/tailwind.css';
import Typed from 'typed.js';

const Hero = () => {
  const el = React.useRef(null);

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
    <div className='max-w-[800px] mt-[-96px] w-full h-screen mx-auto text-center flex flex-col justify-center'>
      <p className='text-[#00df9a] font-bold p-2'>
        CREATE RECIPES WITH RECIPE RADAR
      </p>
      <h1 className='md:text-7xl sm:text-6xl text-4xl font-bold md:py-6'>
        Recipes from data.
      </h1>
      <div className='flex justify-center items-center'>
        <p className='md:text-5xl sm:text-4xl text-xl font-bold py-4'>
          Fast, creative recipes for
        </p>
        <span
          className='md:text-5xl sm:text-4xl text-xl font-bold md:pl-4 pl-2'
          ref={el}
          style={{ height: '4.5rem' }} // Set a fixed height for the container
        />
      </div>
      <p className='md:text-2xl text-xl font-bold text-gray-500'>
        Use your ingredients to create custom recipes.
      </p>
      <div className='flex justify-center'>
        <button className='bg-[#00df9a] w-[200px] rounded-md font-medium my-6 mx-2 py-3 text-black'>
          Get Started
        </button>
        <button className='bg-[#00df9a] w-[200px] rounded-md font-medium my-6 mx-2 py-3 text-black'>
          Login
        </button>
      </div>
    </div>
  );
};

export default Hero;
