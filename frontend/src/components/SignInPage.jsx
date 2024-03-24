import React, { useState } from 'react';
import { Typography, TextField, Button, Paper } from '@mui/material';
import { styled } from '@mui/material/styles';

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

  const handleSubmit = (e) => {
    e.preventDefault();
    // Dummy authentication logic (netId validation)
    if (netId.trim() === '') {
      setError('Please enter your Net ID');
      return;
    }

    // You can implement real authentication logic here
    // For now, let's assume any non-empty Net ID is valid

    // Call the callback function passed from the parent
    onSignIn();

    // Clear the form fields
    setNetId('');
    setPassword('');
    setError('');
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
          <Button type="submit" variant="contained" sx={{ backgroundColor: '#cc0033', mt: 2 }}>
            Sign In
          </Button>
        </form>
      </CardContainer>
    </Container>
  );
};

export default SignInPage;
