import React, { Component } from 'react';
import SignupForm from '../components/SignupForm';
import { isMoment } from 'moment';
import Burner from '../components/Burner';
import { connect } from 'react-redux';
import { startSignup } from '../actions/auth';

class SignupPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: '',
      email: '',
      confirmEmail: '',
      mobile_number: '',
      password: '',
      errors: ''
    };
  }
  onUsernameChange = e => {
    const username = e.target.value;
    if (!username || username.match(/^[A-Za-z]+$/)) {
      this.setState(() => ({ username }));
    }
  };

  onMobileNumberChange = e => {
    const mobile_number = e.target.value;
    if (!mobile_number || mobile_number.match(/^\d{1,}(\.\d{0,2})?$/)) {
      this.setState(() => ({ mobile_number }));
    }
  };

  onEmailChange = e => {
    e.persist();
    this.setState(() => ({ [e.target.name]: e.target.value }));
  };

  onPasswordChange = e => {
    const password = e.target.value;
    this.setState(() => ({ password }));
  };

  componentWillReceiveProps(props) {
    const { errors, user, history } = props;
    if (user && user.id) {
      history.push('/login');
    } else if (errors && Object.keys(errors).length >= 1) {
      const emailError = errors.email && errors.email[0];
      const mobileNumberError = errors.mobile_number && errors.mobile_number[0];
      const all_errors = [emailError, mobileNumberError];
      this.setState(() => ({ errors: all_errors }));
    }
  }

  handleSubmit = e => {
    e.preventDefault();
    const user_data = this.state;
    this.props.startSignup(user_data);
  };
  render() {
    return (
      <div className="burner-box">
        <SignupForm
          handleSubmit={this.handleSubmit}
          onPasswordChange={this.onPasswordChange}
          onEmailChange={this.onEmailChange}
          onMobileNumberChange={this.onMobileNumberChange}
          onUsernameChange={this.onUsernameChange}
          state={this.state}
          errors={this.state.errors}
        />
        <Burner />
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  startSignup: data => dispatch(startSignup(data))
});

const mapStateToProps = state => {
  console.log(state);
  return {
    errors: state.auth.errors,
    user: state.auth.user
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SignupPage);
