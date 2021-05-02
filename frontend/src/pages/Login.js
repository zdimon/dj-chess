import React , { useState, useEffect } from 'react';
import GoogleLogin from 'react-google-login';
import Request from '../Request';
import {config} from '../config';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { Redirect } from 'react-router-dom'; 

function Login(props) {

  const [email, setEmail] = useState('');
  const [redirect, setRedirect] = useState(false);

  const changeEmail = (evt) => {
    setEmail(evt.target.value);
  }

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
        setRedirect(true);
        props.handleLogin();
        
      })
      
  }

  const responseGoogle = (response) => {
    console.log(response);
    var data = {
      email: response.profileObj.email,
      name: response.profileObj.givenName,
      firstName: response.profileObj.givenName
    }
    console.log(props);
    var r = new Request();
    r.post('chess/login/',data)
    .then((payload) => {
       console.log(payload);
       localStorage.setItem('token',payload.token);
       localStorage.setItem('username',payload.user.publicname);
       localStorage.setItem('login',payload.user.username);
       props.onLogin();
    });
  }

  return (
    <div className="Chess" >
       <h1>Login</h1>

       {
         redirect? 
         <Redirect to={`/games`} />
         :
         ''
       }

       <TextField 
            value={email}
            id="standard-basic" 
            onChange={changeEmail}
            label="enter your name" />
          <Button 
            variant="contained" 
            color="primary" 
            onClick = {doLogin}
            >
                        Sign In
          </Button>
       <GoogleLogin
        clientId={config.googleKey}
        buttonText="Login"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
        cookiePolicy={'single_host_origin'}
      />

    </div>
  );
}

export default Login;
