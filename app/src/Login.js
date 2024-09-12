import React from 'react';
import { auth, provider } from './firebaseConfig';
import { signInWithPopup } from 'firebase/auth';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const navigate = useNavigate();

    const handleLogin = async () => {
        try {
            await signInWithPopup(auth, provider);
            navigate('/notes', {});
        } catch (error) {
            console.error('Login Error: ', error);
        }
    };

    return (
        <div className="Login">
            <h1>Login with Google</h1>
            <button onClick={handleLogin}>Login with Google</button>
        </div>
    );
};

export default Login;