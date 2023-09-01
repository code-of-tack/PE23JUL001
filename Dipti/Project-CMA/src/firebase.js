import firebase from "firebase/app";
import "firebase/auth";

export const auth = firebase.initializeApp( {
  apiKey: process.env.FIREBASE_APIKEY,
  authDomain: "unichat-94379.firebaseapp.com",
  projectId: "unichat-94379",
  storageBucket: "unichat-94379.appspot.com",
  messagingSenderId: "663357406389",
  appId: "1:663357406389:web:90c38a8ae214d1ceb752fc"
  }).auth();
