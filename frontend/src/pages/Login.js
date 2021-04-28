import React , { useState, useEffect } from 'react';
import GoogleLogin from 'react-google-login';
import Request from '../Request';
import {config} from '../config';

function Login(props) {
  console.log('Login comp');

  const responseGoogle = (response) => {
    // console.log(response);
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
       props.onLogin();
    });
  }

  return (
    <div className="Chess" >
       <h1>Login</h1>
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
