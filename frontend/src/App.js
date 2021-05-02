import './App.css'; 
import React, { useState, useEffect } from 'react';
import Chess from './pages/Chess';
import Login from './pages/Login';
import Navbar from './components/Navbar';
import Invite from './pages/Invite';
import Games from './pages/Games';
import { Redirect } from 'react-router'

import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";


function App() {
  const [isAuth, setIsAuth] = useState(false);
  useEffect(() => { 
    if(localStorage.getItem('token')) {
      setIsAuth(true);
    } 
  }, [])
  var doLogout = () => {
    setIsAuth(false);
  }

  var doLogin = () => {
    setIsAuth(true);
  }

  return (
    <div className="App" >
          <Router>
            <Navbar isAuth={isAuth} onLogout={doLogout}  />
            <Switch>
            <Route path="/board/:id" render={(props) => <Invite handleLogin={doLogin} {...props} />}>
               
            </Route> 
              
              <Route path="/login" render= {
                () => {
                  return isAuth ? (
                    <Chess />
                  ) : (
                    <Login handleLogin={doLogin} onLogin={doLogin} />
                  )
                }
              } />
              <Route path="/chess" render= {
                () => {
                  return isAuth ? (
                    <Chess />
                  ) : (
                    <Redirect to="/login"/>
                  )
                }
              } />

              <Route path="/games" render= {
                () => {
                  return isAuth ? (
                    <Games />
                  ) : (
                    <Redirect to="/login"/>
                  )
                }
              } />
                
              
              <Route path="/" render= {
                () => {
                  return isAuth ? (
                    <Chess />
                  ) : (
                    <Redirect to="/login"/>
                  )
                }
              } />
            </Switch>
          </Router>
    </div>
  );
}

export default App;
