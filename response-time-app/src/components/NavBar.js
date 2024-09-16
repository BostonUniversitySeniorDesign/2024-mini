// src/components/NavBar.js
import React from "react";
import { AppBar, Toolbar, Typography, Button } from "@mui/material";
import { signOut } from "firebase/auth";
import { auth } from "../firebase";

const NavBar = ({ user }) => {
  const logOut = () => {
    signOut(auth);
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Response Time App
        </Typography>
        {user && (
          <Button color="inherit" onClick={logOut}>
            Logout
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
