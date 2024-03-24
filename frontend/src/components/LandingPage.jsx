import React from 'react';
import { Typography, Button } from '@mui/material';
import { styled } from '@mui/material/styles';
import { keyframes } from '@mui/styled-engine';
import { Link } from "react-router-dom"

const fadeIn = keyframes`
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
`;

const Container = styled('div')({
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  height: 'calc(100vh - 400px)', // Adjusted to fit below the top bar (assuming the top bar height is 64px)
  textAlign: 'center',
  paddingTop: '20px', // Add additional padding for spacing
});

const Heading = styled(Typography)({
  fontSize: '3rem',
  fontWeight: 'bold',
  animation: `${fadeIn} 1s ease-in-out`,
});

const Description = styled(Typography)({
  fontSize: '1.5rem',
  animation: `${fadeIn} 1s ease-in-out`,
  marginBottom: '2rem',
});

const ButtonWrapper = styled('div')({
  animation: `${fadeIn} 1s ease-in-out`,
});

const LandingPage = () => {
  return (
    <Container>
      <Heading variant="h1">Your one and only course recommender</Heading>
      <Description variant="body1">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer adipiscing erat eget risus sollicitudin pellentesque et non erat.
      </Description>
      <ButtonWrapper>
        <Button variant="contained" style={{backgroundColor: '#cc0033'}} component={Link} to="/form">
          Get Started
        </Button>
      </ButtonWrapper>
    </Container>
  );
};

export default LandingPage;
