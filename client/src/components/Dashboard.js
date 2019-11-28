import React, { Component } from 'react';
import SummaryArea from './SummaryArea';
import SavingsFilter from './SavingsFilter';
import SavingsList from '../containers/SavingsList';

const Dashboard = () => (
  <div>
    <SummaryArea />
    <SavingsFilter />
    <SavingsList />
  </div>
);

export default Dashboard;
