import React, { Component } from 'react';
import { connect } from 'react-redux';
import { startLogin } from '../actions/auth';
import LoginForm from '../components/LoginForm';
import Burner from '../components/Burner';

class LoginPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      email: '',
      password: '',
      errors: ''
    };
  }

  handleChange = e => {
    e.persist();
    this.setState(() => ({ [e.target.name]: e.target.value }));
  };

  handleSubmit = e => {
    e.preventDefault();
    const userData = this.state;
    delete userData.errors;
    this.props.startLogin(userData);
  };

  componentWillReceiveProps(props) {
    const { user, history } = props;
    if (user) {
      localStorage.setItem('yeef_token', props.user.token);
      history.push('/dashboard');
    }
  }

  render() {
    return (
      <div className="burner-box">
        <LoginForm
          handleChange={this.handleChange}
          handleSubmit={this.handleSubmit}
          state={this.state}
          error={this.props.errors}
        />
        <Burner />
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  startLogin: data => dispatch(startLogin(data))
});

const mapStateToProps = state => {
  console.log(state.auth, 'from login page');
  return {
    errors: state.auth.errors,
    user: state.auth.user
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(LoginPage);
