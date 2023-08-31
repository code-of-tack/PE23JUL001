import firebase from "firebase/app";
import "firebase/auth";

export const auth = firebase.initializeApp( {
  apiKey: "AIzaSyBtMtwkc1k3EWnAp7vmyy8esO4J9J5Zi20",
  authDomain: "unichat-94379.firebaseapp.com",
  projectId: "unichat-94379",
  storageBucket: "unichat-94379.appspot.com",
  messagingSenderId: "663357406389",
  appId: "1:663357406389:web:90c38a8ae214d1ceb752fc"
  }).auth();