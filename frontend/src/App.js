import React from 'react';
import './App.css';

import MyNavBar from './components/MyNavbar';

import LandingPage from './pages/LandingPage';
import SignUpPage from './pages/SignUpPage';
import LogInPage from './pages/LogInPage';

import {BrowserRouter as Router} from 'react-router-dom';
import {Switch} from 'react-router-dom';
import {Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Router>
        <MyNavBar showBtn="true"/>
        <Switch>
          <Route path='/login'>
            <LogInPage />
          </Route>
          <Route path="/signup">
            {/* TODO store showBtn state in redux */}
            {/* <MyNavBar showBtn="false"/> */}
            < SignUpPage />
          </Route>
          <Route path="/">
            {/* TODO store showBtn state in redux */}
            {/* <MyNavBar showBtn="true"/> */}
            <LandingPage/>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
