import React, { useState } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import TopBar from './components/TopBar';
import LandingPage from './components/LandingPage';
import SignInPage from './components/SignInPage';
import Form from './components/Form';
import Display from './components/Display';
import Sidebar from './components/Sidebar'; // Import Sidebar component
import Dashboard from './components/Dashboard';
import { useMyContext } from './Context';
function App() {
  // Define a state to track authentication status
  const [authenticated, setAuthenticated] = useState(false);

  // Callback function to handle sign-in
  const handleSignIn = () => {
    setAuthenticated(true);
  };
  const {signIn} = useMyContext();

  return (
    <div className="App">
      <TopBar/>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        {/* Pass onSignIn callback to SignInPage */}
        <Route path="/signin" element={<SignInPage onSignIn={handleSignIn} />} />
        {/* Private route for authenticated users */}
        {/* {authenticated ? (
          <>
            <Route path="/form" element={<Form />} />
            <Route path="/display" element={<Display />} />
            <Route path="/sidebar" element={<Sidebar />} />
          </>
        ) : (
          // Redirect to sign-in page if not authenticated
          <Route path="/sidebar" element={<Navigate to="/signin" />} />
        )} */}

        <Route path="/form" element={<Form/>} />
        <Route path="/display" element={< Display/>} />
        {/* <Route path="/sidebar" element={< Sidebar/>}/> */}
        <Route path="/dashboard" element={< Dashboard/>}/>

      </Routes>
    </div>
  );
}

export default App;
