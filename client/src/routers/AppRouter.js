import React from 'react';

import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Dashboard from '../components/Dashboard';
import Login from '../components/Login';

const AppRouter = () => (
  <BrowserRouter>
    <Switch>
      <Route path="/" component={Login} />
      <Route path="/dashboard" component={Dashboard}  />
    </Switch>
  </BrowserRouter>
);

export default AppRouter;
