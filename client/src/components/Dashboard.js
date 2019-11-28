import React, { Component } from 'react';

import Profile from './Profile';

class Dashboard extends Component {
  constructor(props) {
    super(props);

    this.state = {
      savings: 4000
    };
  }

  render() {
    return (
      <>
        <Profile />
      </>
    );
  }
}

export default Dashboard;
