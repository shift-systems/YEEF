import React, { Component } from 'react';



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
        <p>This is the Profile Page</p>
      </>
    );
  }
}

export default Dashboard;
