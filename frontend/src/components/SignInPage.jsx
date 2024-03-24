import React, { useState } from 'react';
import { Typography, TextField, Button, Paper } from '@mui/material';
import { styled } from '@mui/material/styles';
import {useNavigate} from "react-router-dom";
import { useMyContext } from '../Context';

const Container = styled('div')({
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'flex-start',
  height: '80vh',
  textAlign: 'center',
  marginTop: '20vh'
});

const CardContainer = styled(Paper)({
  padding: '20px',
  width: '80%', // Increased width
  maxWidth: '400px', // Maximum width
  border: '2px solid #ccc', // Increased border
  borderRadius: '8px', // Rounded corners
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
});

const SignInPage = ({ onSignIn }) => {
  const [netId, setNetId] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const navigate = useNavigate();

  const {setIsSignIn, setNetId:setGlobalNetId} = useMyContext();

  const handleSubmit = async(e) => {
    e.preventDefault();
    // Dummy authentication logic (netId validation)
    const formData = {
      netId, password
    }
    // try {
    //   const res = await fetch('http://127.0.0.1:5000/dashboard',{
    //     method: 'POST',
    //     headers: {
    //     'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(formData),
    //   });
    //   if (!res.ok) {
    //     throw new Error('Error: $(res.status)')
    //   }
    //   const result = await res.json();
    //   console.log('Success', result);
      
    // } catch (error) {
    //   console.error('Error during form submission: ', error);
    // }
      setIsSignIn(true);
      setGlobalNetId(netId);
      navigate("/dashboard/" + netId);
  };

  return (
    <Container>
      <CardContainer elevation={3}>
        <Typography variant="h4" gutterBottom>
          Sign In
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Net ID"
            variant="outlined"
            margin="normal"
            fullWidth
            value={netId}
            onChange={(e) => setNetId(e.target.value)}
            error={error !== ''}
            helperText={error}
          />
          <TextField
            label="Password"
            variant="outlined"
            margin="normal"
            fullWidth
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button type="submit" variant="contained" sx={{ backgroundColor: '#cc0033', mt: 2 }} onClick={handleSubmit}>
            Sign In
          </Button>
        </form>
      </CardContainer>
    </Container>
  );
};

export default SignInPage;