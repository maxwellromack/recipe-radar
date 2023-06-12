import React , { useState } from 'react';
import 'tailwindcss/tailwind.css';

function Register() {
    const [user, setUsername] = useState('');
    const [pass, setPassword] = useState('');

    const userChange = event => {
        setUsername(event.target.value);
    }

    const passChange = event => {
        setPassword(event.target.value);
    }

    async function handleClick() {
        try {
            const payload = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    username: user,
                    password: pass
                })
            };

            const response = await fetch('auth/register', payload);
            const jsonData = await response.json();
            console.log(jsonData);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    return (
        <div className="w-screen h-screen flex bg-[#00df9a]">
        <div className="bg-white overflow-hidden">
            <div className="flex grid grid-cols-[60%_40%]">
            <div className="p-8 mx-auto w-[70vw] h-screen">
                <div className="grid flex flex-grid place-items-top w-fit">
                <div className="w-fit h-fit flex lg:flex-1">
                    <a href="/#" className="-m-1.5 p-1.5">
                    <span className="sr-only">RecipeRadar</span>
                    </a>
                </div>
                <div className="w-1/2 place-self-stretch mt-[5rem]">
                    <div className="mx-auto">
                    <p className="mt-2 w-screen text-start text-6xl font-semibold tracking-loose text-black">This is the register page:<br /><span className="text-6xl font-bold">It is not the login page</span></p>
                    <p className="my-10 text-start mx-auto text-3xl tracking-loose text-gray-800">Stop asking if this is the login page.</p>
                    </div>
                </div>
                </div>
            </div>
            <div className="mx-auto w-full grid place-items-center">
                <div className="rounded-xl shadow-lg p-8 bg-[#00df9a]">
                <div className="p-4 flex flex-col justify-center bg-white h-full">
                    <form className="md:max-w-lg mx-auto">
                    <label className="block mb-4">
                        <p className="mb-2 text-gray-900 font-semibold leading-normal">Username</p>
                        <input
                        className="px-4 py-3.5 w-full text-gray-400 font-medium placeholder-gray-400 bg-white outline-none border border-gray-300 rounded-lg focus:ring focus:ring-indigo-300"
                        id="username"
                        name="username"
                        type="text"
                        autoComplete="username"
                        placeholder="Enter username"
                        onChange={userChange}
                        value={user}
                        />
                    </label>
                    <label className="block mb-5">
                        <p className="mb-2 text-gray-900 font-semibold leading-normal">Password</p>
                        <input
                        className="px-4 py-3.5 w-full text-gray-400 font-medium placeholder-gray-400 bg-white outline-none border border-gray-300 rounded-lg focus:ring focus:ring-indigo-300"
                        id="password"
                        name="password"
                        type="text"
                        autoComplete="current-password"
                        placeholder="Password"
                        onChange={passChange}
                        value={pass}
                        />
                    </label>
                    <button className="mb-9 py-4 px-9 w-full text-white font-semibold border border-[#00df9a] rounded-xl shadow-4xl focus:ring focus:ring-indigo-300 bg-[#00df9a] hover:bg-[#008c6b] transition ease-in-out duration-200" type="submit" onClick={handleClick}>
                        Register
                    </button>
                    </form>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    );
};

export default Register;
