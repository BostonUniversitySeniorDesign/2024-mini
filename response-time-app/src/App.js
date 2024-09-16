// src/App.js
import React, { useState, useEffect } from "react";
import { onAuthStateChanged } from "firebase/auth";
import { auth } from "./firebase";
import SignUp from "./components/SignUp";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";
import NavBar from "./components/NavBar";

const App = () => {
  const [user, setUser] = useState(null);
  const [authMode, setAuthMode] = useState("login"); // 'login' or 'signup'

  useEffect(() => {
    // Monitor authentication state
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
    });
    return unsubscribe;
  }, []);

  const toggleAuthMode = () => {
    setAuthMode(authMode === "login" ? "signup" : "login");
  };

  if (user) {
    return <Dashboard user={user} />;
  } else {
    return (
      <>
        <NavBar user={user} />
        {user ? (
          <Dashboard user={user} />
        ) : authMode === "login" ? (
          <Login toggleAuthMode={toggleAuthMode} />
        ) : (
          <SignUp toggleAuthMode={toggleAuthMode} />
        )}
      </>
    );
  };
};

export default App;
