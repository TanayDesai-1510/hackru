import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import { ThemeProvider } from './Context';

const root = document.getElementById('root');

ReactDOM.createRoot(root).render(
  <ThemeProvider>
  <BrowserRouter>
    <App />
  </BrowserRouter>
  </ThemeProvider>
);
