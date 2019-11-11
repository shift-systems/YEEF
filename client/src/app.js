import React from 'react';
import ReactDom from 'react-dom';

const Profile = props => {
  return (
    <>
      <h1>This is a profgile</h1>
    </>
  );
};

class Dashbord extends React.Component {
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

ReactDom.render(<Dashbord />, document.getElementById('app'));
