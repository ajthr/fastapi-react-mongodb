import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import './index.css';

import Home from './pages/Home'

ReactDOM.render(
    <Router>
      <Switch>
        <Route path='/' component={Home} exact />
      </Switch>
    </Router>,
  document.getElementById('root')
);
