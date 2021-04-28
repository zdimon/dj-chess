import React, { useState, useEffect } from 'react';

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

function Navbar(props) {
    const classes = useStyles();
    const [username, setUsername] = useState(false);
    useEffect(() => { 
      if(localStorage.getItem('username')) {
        setUsername(localStorage.getItem('username'));
      } 
    }, [])

    var logout = () => {
      console.log('Logout');
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      props.onLogout();
    }
    return (
        <AppBar position="static">
        <Toolbar>
            <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <MenuIcon />
            </IconButton>
            {
               props.isAuth? 
               <Typography variant="h6" className={classes.title}>
                Welcome {username}
               </Typography>
               :
               <Typography variant="h6" className={classes.title}>
                Please Sign in.
               </Typography>
            }

            
            
                
                { props.isAuth? 
                <>
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
                onClick={logout} >
                    Logout
                </Button>
                </>
                :
                <Button 
                variant="contained" 
                color="secondary" 
                component={Link} 
                to={'/login'} >
                    Login
                </Button>                
                
                }
                


        </Toolbar>
        </AppBar>
    )
}

export default Navbar;