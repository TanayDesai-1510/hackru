import React from 'react';
import { Typography, Button } from '@mui/material';
import { styled } from '@mui/material/styles';
import { keyframes } from '@mui/styled-engine';
import { Link } from "react-router-dom";
import TopBar from './TopBar';
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
  height: 'calc(100vh - 150px)', // Adjusted to fit below the top bar (assuming the top bar height is 64px)
  textAlign: 'center',
  paddingTop: '20px', // Add additional padding for spacing
});

const ContentWrapper = styled('div')({
  display: 'flex',
  flexWrap: 'wrap', // Allow wrapping on smaller screens
  alignItems: 'center',
  justifyContent: 'space-between', // Add space between text and image
  maxWidth: '800px', // Limit the width of the content
  margin: '20px', // Add margin around the content
});

const AnimatedRecommender = styled('span')({
  animation: `${fadeIn} 1s ease-in-out`,
  color: '#cc0033', // Set color to #cc0033
});

const TextWrapper = styled('div')({
  flex: '1', // Take remaining space
  marginBottom: '20px', // Add space below text
});

const ImageWrapper = styled('div')({
  flex: '1', // Take remaining space
  order: 1, // Make the image appear first in the flex container on smaller screens
  position: 'relative', // Position the image for hover effect
  '&:hover img': {
    transform: 'scale(1.05)', // Reduce the scale factor for less animation
  },
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
  marginRight: '10px'
});

const Image = styled('img')({
  width: '100%', // Ensure the image fills its container
  transition: 'transform 0.3s ease-in-out', // Add transition for smooth hover effect
});

const ButtonWrapper = styled('div')({
  animation: `${fadeIn} 1s ease-in-out`,
});

const LandingPage = () => {
  return (
    <>
    <Container>
      <Heading variant="h1">Your one and only course <AnimatedRecommender>recommender</AnimatedRecommender></Heading>
      <ContentWrapper>
        <TextWrapper>
          <Description variant="body1">
            Feeling overwhelmed by course options at Rutgers? We've got you covered! Find the perfect classes catered to your profile! Let's take the stress out of course selection.
          </Description>
          <ButtonWrapper>
            <Button variant="contained" style={{backgroundColor: '#cc0033'}} component={Link} to="/form">
              Get Started
            </Button>
          </ButtonWrapper>
        </TextWrapper>
        <ImageWrapper>
          <Image src="/assets/confused.jpg" alt="Confused" />
        </ImageWrapper>
      </ContentWrapper>
    </Container>
    </>
  );
};

export default LandingPage;
