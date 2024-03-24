import React, { createContext, useContext, useState } from 'react';

// Create a context
const ThemeContext = createContext();
export const useMyContext = () => {
  return useContext(ThemeContext);
};

// Create a custom hook to use the context

// Create a provider component
export const ThemeProvider = ({ children }) => {
  const [signIn, setIsSignIn] = useState(false);
  const [netId, setNetId] = useState(null);
  

  return (
    <ThemeContext.Provider value={{ signIn, setIsSignIn, netId, setNetId }}>
      {children}
    </ThemeContext.Provider>
  );
};
