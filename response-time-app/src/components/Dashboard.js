// src/components/Dashboard.js
import React, { useEffect, useState } from "react";
import { signOut } from "firebase/auth";
import { collection, query, orderBy, onSnapshot } from "firebase/firestore";
import { auth, firestore } from "../firebase";
import {
  Container,
  Typography,
  Button,
  Box,
  Card,
  CardContent,
  Grid,
} from "@mui/material";

const Dashboard = ({ user }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const q = query(
      collection(firestore, "users", user.uid, "response_times"),
      orderBy("timestamp", "desc")
    );

    const unsubscribe = onSnapshot(q, (snapshot) => {
      const newData = snapshot.docs.map((doc) => doc.data());
      setData(newData);
    });

    return unsubscribe;
  }, [user.uid]);

  const logOut = () => {
    signOut(auth);
  };

  return (
    <Container>
      <Box sx={{ mt: 4, mb: 2, display: "flex", justifyContent: "space-between" }}>
        <Typography variant="h5">Welcome, {user.email}</Typography>
        <p>Your User ID (UID): {user.uid}</p>
        <Button variant="contained" color="secondary" onClick={logOut}>
          Log Out
        </Button>
      </Box>
      <Typography variant="h6" gutterBottom>
        Your Response Times:
      </Typography>
      {data.length > 0 ? (
        <Grid container spacing={2}>
          {data.map((entry, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <Card variant="outlined">
                <CardContent>
                  <Typography variant="subtitle1" gutterBottom>
                    Game {index + 1}
                  </Typography>
                  <Typography variant="body2">
                    <strong>Average Time:</strong> {entry.average_time} ms
                  </Typography>
                  <Typography variant="body2">
                    <strong>Min Time:</strong> {entry.min_time} ms
                  </Typography>
                  <Typography variant="body2">
                    <strong>Max Time:</strong> {entry.max_time} ms
                  </Typography>
                  <Typography variant="body2">
                    <strong>Score:</strong> {entry.score}
                  </Typography>
                  <Typography variant="body2">
                    <strong>Timestamp:</strong>{" "}
                    {new Date(
                      entry.timestamp.seconds * 1000
                    ).toLocaleString()}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      ) : (
        <Typography>No data available.</Typography>
      )}
    </Container>
  );
};

export default Dashboard;
