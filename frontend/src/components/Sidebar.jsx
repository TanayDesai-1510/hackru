import React from 'react';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import { Hidden, styled } from '@mui/material';

const drawerWidth = 240;

const StyledDrawer = styled(Drawer)(({ theme }) => ({
  [theme.breakpoints.up('md')]: {
    width: drawerWidth,
    flexShrink: 0,
    '& .MuiDrawer-paper': {
      width: drawerWidth,
      boxSizing: 'border-box',
    },
  },
}));

const Sidebar = () => {
  return (
    <>
      {/* Sidebar for larger screens (md and up) */}
      <Hidden smDown implementation="css">
        <StyledDrawer
          variant="permanent"
          anchor="left"
        >
          <List>
            <ListItem button>
              <ListItemText primary="Dashboard" />
            </ListItem>
            <ListItem button>
              <ListItemText primary="Recommendation" />
            </ListItem>
          </List>
        </StyledDrawer>
      </Hidden>
      {/* Sidebar for smaller screens (sm and below) */}
      <Hidden mdUp implementation="css">
        <Drawer
          variant="temporary"
          anchor="left"
        >
          <List>
            <ListItem button>
              <ListItemText primary="Dashboard" />
            </ListItem>
            <ListItem button>
              <ListItemText primary="Recommendation" />
            </ListItem>
          </List>
        </Drawer>
      </Hidden>
    </>
  );
};

export default Sidebar;
