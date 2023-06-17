import React from 'react';
import 'tailwindcss/tailwind.css';
import { useNavigate } from 'react-router-dom';

const Login = () => {
	const [user, setUsername] = useState('');
	const [pass, setPassword] = useState('');

	const userChange = event => {
		setUsername(event.target.value);
	}

	const passChange = event => {
		setPassword(event.target.value);
	}
	const navigate = useNavigate();

	const handleLogin = () => {
		navigate('/recipiemain');
	};

	return (
		<div className="relative flex flex-col justify-center min-h-screen overflow-hidden">
			<div className="w-full p-6 m-auto bg-white rounded-md shadow-xl shadow-purple-600 ring ring-2 ring-purple-600 lg:max-w-xl">
				<h1 className="text-3xl font-semibold text-center text-purple-700">
					Sign in
				</h1>
				<form className="mt-6">
					<div className="mb-2">
						<label
							htmlFor="email"
							className="block text-sm font-semibold text-gray-800">
							Email
						</label>
						<input
							type="email"
							className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
						/>
					</div>
					<div className="mb-2">
						<label
							htmlFor="password"
							className="block text-sm font-semibold text-gray-800">
							Password
						</label>
						<input
							type="password"
							className="block w-full px-4 py-2 mt-2 text-purple-700 bg-white border rounded-md focus:border-purple-400 focus:ring-purple-300 focus:outline-none focus:ring focus:ring-opacity-40"
						/>
					</div>
					<a
						href="#"
						className="text-xs text-purple-600 hover:underline">
						Forgot Password?
					</a>
					<div className="mt-6">
						<button
							className="w-full px-4 py-2 tracking-wide text-white transition-colors duration-200 transform bg-purple-700 rounded-md hover:bg-purple-600 focus:outline-none focus:bg-purple-600"
							onClick={handleLogin} // Update onClick event handler 
						>
							Login
						</button>
					</div>
				</form>

				<p className="mt-8 text-xs font-light text-center text-gray-700">
					{" "}
					Don't have an account?{" "}
					<a
						href="/register"
						className="font-medium text-purple-600 hover:underline">
						Sign up
					</a>
				</p>
			</div>
		</div>
	);
};

export default Login;
