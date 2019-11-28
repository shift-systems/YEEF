import React from 'react';

import { Router, Route, Switch } from 'react-router-dom';
import createHistory from 'history/createBrowserHistory';
import Dashboard from '../components/Dashboard';
import PrivateRout from './PrivateRoute';
import PublicRoute from './PublicRoute';
import SavingsSummary from '../components/SummaryArea';
import LoginPage from '../components/LoginPage';
import SavingsPage from '../containers/SavingsPage';

export const history = createHistory();

const AppRouter = () => (
  <Router history={history}>
    <Switch>
      <PublicRoute path="/login" component={LoginPage} />
      <PrivateRout path="/dashboard" component={Dashboard} exact={true} />
      <PrivateRout path="/save" component={SavingsPage} />
    </Switch>
  </Router>
);

export default AppRouter;
