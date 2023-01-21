//import * as firebase from 'firebase';
import firebase from "firebase/compat/app";
//import "firebase/firestore";
import "firebase/compat/firestore";
//import "firebase/auth";
import "firebase/compat/auth";

const firebaseConfig = {
  //from firebase site
};

let app;
// if we didnt initializse the app then =>
if(firebase.apps.length === 0){
   app=firebase.initializeApp(firebaseConfig);
}
else{ //else just use the firebase app
    app=firebase.app();
}


const db = app.firestore();
const auth=firebase.auth();

export {db, auth};

//export default app;