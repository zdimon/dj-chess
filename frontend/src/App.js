import './App.css'; 

import Chess from './pages/Chess';
import Login from './pages/Login';
import Navbar from './components/Navbar';

import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";


function App() {

  return (
    <div className="App" >
          <Router>
            <Navbar />
            <Switch>
              
              <Route path="/login" component={Login} />
              <Route path="/chess" component={Chess} />
              <Route path="/" component={Chess} />
            </Switch>
          </Router>
    </div>
  );
}

export default App;
