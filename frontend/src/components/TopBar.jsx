import React, { useState } from 'react';
import { AppBar, Toolbar, IconButton, Drawer, List, ListItem, Typography, useMediaQuery } from '@mui/material';
import { styled } from '@mui/material/styles';
import { Link } from 'react-router-dom';
import MenuIcon from '@mui/icons-material/Menu';
import { useMyContext } from '../Context';
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

const StyledMenuIcon = styled(MenuIcon)({
  color: '#000000', // black color
});

const LinkWrapper = styled('div')({
  display: 'flex',
  alignItems: 'center',
});

const StyledLink = styled(Link)({
  marginRight: '10px',
  textDecoration: 'none', // Remove default underline
  color: '#cc0033', // Text color
  '&:hover': {
    textDecoration: 'underline', // Underline on hover
  },
});

const TopBar = () => {
  const [openDrawer, setOpenDrawer] = useState(false);
  const isMobile = useMediaQuery('(max-width:600px)');

  const {signIn} = useMyContext();

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
          {isMobile && (
            <IconButton
              color="inherit"
              aria-label="open drawer"
              edge="end"
              onClick={handleDrawerOpen}
              sx={{ display: { md: 'none' } }} // Hide on medium and larger screens
            >
              <StyledMenuIcon />
            </IconButton>
          )}
          {!isMobile && (
            <LinkWrapper>
              { signIn && <><StyledLink to="/dashboard">
                <Typography variant="body1">Dashboard</Typography>
              </StyledLink>
              <StyledLink to="/recommendation">
                <Typography variant="body1">Recommendation</Typography>
              </StyledLink> </>}
              { !signIn && <StyledLink to="/signin">
                <Typography variant="body1">Sign In</Typography>
              </StyledLink> }
            </LinkWrapper>
          )}
        </Toolbar>
      </StyledAppBar>
      <Drawer anchor="right" open={openDrawer} onClose={handleDrawerClose}>
        <List>
          <ListItem onClick={handleDrawerClose} component={Link} to="/dashboard">
            <Typography variant="body1">Dashboard</Typography>
          </ListItem>
          <ListItem onClick={handleDrawerClose} component={Link} to="/recommendation">
            <Typography variant="body1">Recommendation</Typography>
          </ListItem>
          <ListItem onClick={handleDrawerClose} component={Link} to="/signin">
            <Typography variant="body1">Sign In</Typography>
          </ListItem>
          {/* Add more menu items as needed */}
        </List>
      </Drawer>
    </React.Fragment>
  );
};

export default TopBar;
