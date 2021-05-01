import React , { useState, useEffect } from 'react';
import GoogleLogin from 'react-google-login';
import Request from '../Request';
import {config} from '../config';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { Link } from "react-router-dom";
import {
  BrowserRouter as Router,
} from "react-router-dom";


function Invite(props) {
  


  useEffect(() => { 
    localStorage.setItem('board',props.match.params.id);
  }, [])

  const [email, setEmail] = useState('');
  const [isAuth, setIsAuth] = useState(false);
  const doLogin = () => {
    const data = {
      email: email
    }
      var r = new Request();
      r.post('chess/login/byemail', data)
      .then((payload) => {
        localStorage.setItem('token',payload.token);
        localStorage.setItem('username',payload.username);
        localStorage.setItem('login',payload.username);
        setIsAuth(true);
        props.handleLogin();
        r.get(`chess/add/agressor/${props.match.params.id}`).then((payload) => {
          console.log(payload);
        })
      })
      
  }

  const changeEmail = (evt) => {
    setEmail(evt.target.value);
  }
  
  return (
    <div className="Invite" >
      {
        !isAuth?
        <>
          <h1>Invitation to play from </h1>
          <p>
              What is your email?
          </p> 
          <TextField 
            value={email}
            id="standard-basic" 
            onChange={changeEmail}
            label="enter your email" />
          <Button 
            variant="contained" 
            color="primary" 
            onClick = {doLogin}
            >
                        Sign In
          </Button>
        </>
        :
        <>
          
            <Button 
              variant="contained" 
              color="primary" 
              to={'/chess'}
              component={Link} 
              >
                Start the game!
            </Button>
         
        </>
      }


    </div>
  );
}

export default Invite;
