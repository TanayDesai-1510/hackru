import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import TopBar from './components/TopBar';
import LandingPage from './components/LandingPage';
import SignInPage from './components/SignInPage';
import Form from './components/Form';
import Display from './components/Display';

function App() {
  // Define a state to track authentication status
  const [authenticated, setAuthenticated] = useState(false);

  // Callback function to handle sign-in
  const handleSignIn = () => {
    setAuthenticated(true);
  };

  return (
    <div className="App">
      <TopBar />
      <Routes>
        <Route exact path="/" element={<LandingPage />} />
        {/* Pass onSignIn callback to SignInPage */}
        <Route path="/signin" element={<SignInPage onSignIn={handleSignIn} />} />
        <Route path="/form" element={<Form />} />
      </Routes>
      <Display />
    </div>
  );
}

export default App;
