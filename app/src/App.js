import React from 'react';
import { auth, provider } from './firebaseConfig';
import { signInWithPopup } from 'firebase/auth';

const App = () => {
  const handleGoogleLogin = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      console.log('User Info:', user);
      // Here you can add the user to Firestore or handle user data as needed
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div className="App">
      <h1>Gmail Login with Firebase</h1>
      <button onClick={handleGoogleLogin}>Login with Google</button>
    </div>
  );
};

export default App;