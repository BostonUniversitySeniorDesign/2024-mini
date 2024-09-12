// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCxsXcoGFTYOna8DhIdxpo4DpQ1-Q7aBX8",
    authDomain: "ec463-mini-app.firebaseapp.com",
    projectId: "ec463-mini-app",
    storageBucket: "ec463-mini-app.appspot.com",
    messagingSenderId: "775318854082",
    appId: "1:775318854082:web:6dc195feeecf7c783dde5b"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();
export const db = getFirestore(app);