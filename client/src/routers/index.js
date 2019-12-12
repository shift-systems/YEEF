import React from 'react';

import { Router, Route, Switch } from 'react-router-dom';
import createHistory from 'history/createBrowserHistory';
import Dashboard from '../components/Dashboard';
import PrivateRout from './PrivateRoute';
import PublicRoute from './PublicRoute';
import LoginPage from '../containers/LoginPage';
import SavingsPage from '../containers/SavingsPage';
import SignupPage from '../containers/SignupPage';
import Burner from '../components/Burner';

export const history = createHistory();

const AppRouter = () => (
  <Router history={history}>
    <Switch>
      <PublicRoute path="/burner" component={Burner} exact={true} />
      <PublicRoute path="/signup" component={SignupPage} />
      <PublicRoute path="/login" component={LoginPage} />
      <PrivateRout path="/dashboard" component={Dashboard} exact={true} />
      <PrivateRout path="/save" component={SavingsPage} />
    </Switch>
  </Router>
);

export default AppRouter;
