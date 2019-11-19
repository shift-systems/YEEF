import React from 'react';

import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Dashboard from '../components/Dashboard';

const AppRouter = () => (
  <BrowserRouter>
    <Switch>
      <Route path="/" component={Dashboard} />
    </Switch>
  </BrowserRouter>
);

export default AppRouter;
