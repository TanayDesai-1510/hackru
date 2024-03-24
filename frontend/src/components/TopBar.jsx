import React, { useState } from 'react';
import { AppBar, Toolbar, Button, IconButton, Drawer, List, ListItem, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import { Link } from 'react-router-dom';
import MenuIcon from '@mui/icons-material/Menu';

const StyledAppBar = styled(AppBar)({
  backgroundColor: '#ffffff', // white background color
});

const LogoContainer = styled('div')({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center', // Center horizontally
  flex: '1', // Take remaining space
});

const LogoImage = styled('img')({
  maxWidth: 250,
  height: 'auto',
  cursor: 'pointer', // Add pointer cursor for indicating clickability
});

const SignInButtonContainer = styled('div')({
  marginLeft: 'auto', // Push the button to the right
});

const StyledMenuIcon = styled(MenuIcon)({
  color: '#000000', // black color
});

const StyledSignInButton = styled(Button)({
  backgroundColor: '#cc0033', // custom background color
});

const TopBar = () => {
  const [openDrawer, setOpenDrawer] = useState(false);

  const handleDrawerOpen = () => {
    setOpenDrawer(true);
  };

  const handleDrawerClose = () => {
    setOpenDrawer(false);
  };

  return (
    <React.Fragment>
      <StyledAppBar position="static">
        <Toolbar>
          <LogoContainer>
            <Link to="/"> {/* Wrap the LogoImage with Link component */}
              <LogoImage src="/assets/my-rutgers-logo-light-new.png" alt="ScarletSelector" />
            </Link>
          </LogoContainer>
          <SignInButtonContainer>
            <IconButton
              color="inherit"
              aria-label="open drawer"
              edge="end"
              onClick={handleDrawerOpen}
              sx={{ display: { md: 'none' } }} // Hide on medium and larger screens
            >
              <StyledMenuIcon />
            </IconButton>
            <Button component={Link} to="/signin" variant="contained" style={{ backgroundColor: '#cc0033' }} sx={{ display: { xs: 'none', md: 'block' } }}>
              <Typography variant="body1" sx={{ fontSize: { xs: '0.8rem', md: '1rem' } }}>Sign In</Typography>
            </Button>
          </SignInButtonContainer>
        </Toolbar>
      </StyledAppBar>
      <Drawer anchor="right" open={openDrawer} onClose={handleDrawerClose}>
        <List>
          <ListItem button onClick={handleDrawerClose} component={Link} to="/signin">
            <StyledSignInButton variant="contained" color="primary">
              <Typography sx={{ fontSize: '1rem' }}>Sign In</Typography>
            </StyledSignInButton>
          </ListItem>
          {/* Add more menu items as needed */}
        </List>
      </Drawer>
    </React.Fragment>
  );
};

export default TopBar;
