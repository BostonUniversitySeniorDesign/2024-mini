const functions = require("firebase-functions");
const admin = require("firebase-admin");
const express = require("express");
const cors = require("cors");

admin.initializeApp();

const app = express();
app.use(cors({origin: true}));
app.use(express.json());

// Middleware to check the device API key
const validateApiKey = (req, res, next) => {
  const authHeader = req.headers.authorization;
  const apiKey =
    authHeader && authHeader.split(" ")[1];

  if (apiKey === functions.config().api.device_key) {
    next();
  } else {
    res.status(401).send("Unauthorized");
  }
};

// Endpoint to upload data
app.post("/upload_data", validateApiKey, async (req, res) => {
    const data = req.body;
    const userId = data.user_id;
  
    console.log("Received data:", data);
  
    if (!userId) {
      console.log("User ID is missing.");
      return res.status(400).send("User ID is required");
    }
  
    try {
      await admin
        .firestore()
        .collection("users")
        .doc(userId)
        .collection("response_times")
        .add({
          response_times: data.response_times,
          average_time: data.avg_time,
          min_time: data.min_time,
          max_time: data.max_time,
          misses: data.misses,
          total_flashes: data.total_flashes,
          score: data.score,
          timestamp: admin.firestore.FieldValue.serverTimestamp(),
        });
      console.log("Data uploaded successfully for user:", userId);
      res.status(200).send("Data uploaded successfully");
    } catch (error) {
      console.error("Error uploading data:", error);
      res.status(500).send("Internal Server Error");
    }
  });
  

exports.api = functions.https.onRequest(app);
