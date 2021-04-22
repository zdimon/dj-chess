import React from 'react';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import { Link, BrowserRouter } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

function Navbar() {
    const classes = useStyles();
    return (
        <AppBar position="static">
        <Toolbar>
            <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <MenuIcon />
            </IconButton>
            <Typography variant="h6" className={classes.title}>
            Chess game
            </Typography>
            
            <Button 
                variant="contained" 
                color="primary" 
                component={Link} 
                to={'/chess'} >
                    Chess
                </Button>
                
                <Button 
                variant="contained" 
                color="secondary" 
                component={Link} 
                to={'/login'} >
                    Login
                </Button>


        </Toolbar>
        </AppBar>
    )
}

export default Navbar;